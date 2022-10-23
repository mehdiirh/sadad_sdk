from base64 import b64encode, b64decode
from hashlib import sha256

import requests
from Crypto.Cipher import DES3
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad

from sadad_sdk.core.objects import ParamsBase
from sadad_sdk.utils.config import BASE_URL, REQUEST_HEADERS


class SadadBase:

    uri_path = ""

    def __init__(
        self,
        vpg_key: str,
        merchant_id: str = None,
        terminal_id: int = None,
        rsa_key_location: str = None,
        proxies: dict = None,
    ):
        """
        All Sadad services must inherit from this class. it creates an instance to use Sadad services

        Args:
            vpg_key: Terminal VPG key
            merchant_id: Merchant ID
            terminal_id: Terminal ID
            rsa_key_location: RSA key file location
            proxies: HTTP/SOCKS proxy to send requests with
        """

        self._vpg_key = b64decode(vpg_key)
        self._merchant_id = merchant_id
        self._terminal_id = terminal_id
        self.proxies = proxies

        if rsa_key_location is not None:
            with open(rsa_key_location, "r") as key:
                self._rsa_key = RSA.import_key(key.read())
        else:
            self._rsa_key = None

        self.base_url = BASE_URL + "/" + self.uri_path

    def _create_sign_data(self, values: str):

        cipher_encrypt = DES3.new(self._vpg_key, DES3.MODE_ECB)

        sign_data = pad(values.encode("utf-8"), 8, style="pkcs7")
        encrypted_text = cipher_encrypt.encrypt(sign_data)
        encrypted_text = b64encode(encrypted_text).decode("utf-8")

        return encrypted_text

    def _create_sign(self, values):

        values = values.encode("utf8")

        hashed_values = int.from_bytes(sha256(values).digest(), "big")
        sign = pow(hashed_values, self._rsa_key.d, self._rsa_key.n)
        sign = hex(sign).encode("utf8")
        sign = b64encode(sign)
        return sign

    def _get_headers(self, values: str):
        headers = REQUEST_HEADERS.copy()
        if self._vpg_key:
            headers["Sign-Data"] = self._create_sign_data(values)
        if self._rsa_key:
            headers["Sign"] = self._create_sign(values)
        return headers

    def _send(
        self, uri: str = "", params: ParamsBase = None, pass_headers: bool = True
    ):
        url = self.base_url + uri

        data = None
        if params is not None:
            data = params.to_json()

        headers = None
        if pass_headers:
            sign_data = params.sign_values()
            headers = self._get_headers(sign_data)

        response = None
        last_response_code = None
        for _ in range(3):

            try:
                response = requests.post(
                    url, headers=headers, data=data, proxies=self.proxies, timeout=5
                )
                last_response_code = response.status_code
            except:
                continue

            if response.ok:
                break

        if not response:
            raise ConnectionError(
                {
                    "status_code": last_response_code,
                    "code": "connection_error",
                    "message": "there was a problem establishing connection with sadad",
                }
            )

        return response.json()
