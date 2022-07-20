from sadad_sdk.core.objects import ParamsBase
from sadad_sdk.utils.config import BASE_URL, REQUEST_HEADERS

from Crypto.Cipher import DES3
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad

from base64 import b64encode, b64decode
from hashlib import sha256
import requests


class SadadBase:

    uri_path = ""

    def __init__(self, VPG_KEY: str, RSA_KEY_LOCATION: str):
        self.__vpg_key = b64decode(VPG_KEY)  # private and protected variable
        self.base_url = BASE_URL + "/" + self.uri_path
        with open(RSA_KEY_LOCATION, "r") as key:
            self.__rsa_key = RSA.import_key(key.read())  # private and protected variable

    def _create_sign_data(self, values: str):

        cipher_encrypt = DES3.new(self.__vpg_key, DES3.MODE_ECB)

        sign_data = pad(values.encode("utf-8"), 8, style="pkcs7")
        encrypted_text = cipher_encrypt.encrypt(sign_data)
        encrypted_text = b64encode(encrypted_text).decode("utf-8")

        return encrypted_text

    def _create_sign(self, values):

        values = values.encode("utf8")

        hashed_values = int.from_bytes(sha256(values).digest(), "big")
        sign = pow(hashed_values, self.__rsa_key.d, self.__rsa_key.n)
        sign = hex(sign).encode("utf8")
        sign = b64encode(sign)
        return sign

    def _get_headers(self, values: str):
        headers = REQUEST_HEADERS.copy()
        headers["Sign-Data"] = self._create_sign_data(values)
        headers["Sign"] = self._create_sign(values)
        print(headers)
        return headers

    def _send(self, uri: str = "", params: ParamsBase = None):
        url = self.base_url + uri

        data = None
        if params is not None:
            data = params.to_json()

        sign_data = params.sign_values()
        headers = self._get_headers(sign_data)

        response = None
        last_response_code = None
        for _ in range(3):

            try:
                response = requests.post(url, headers=headers, data=data, timeout=5)
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
