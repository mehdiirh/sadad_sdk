from sadad_sdk.services import RefundService, PaymentService


class Sadad:
    def __init__(
        self,
        vpg_key: str,
        merchant_id: str = None,
        terminal_id: int = None,
        rsa_key_location: str = None,
        proxies: dict = None,
    ):
        """
        Create a sadad client. it creates an instance to use Sadad services

        Args:
            vpg_key: Terminal VPG key
            merchant_id: Merchant ID
            terminal_id: Terminal ID
            rsa_key_location: RSA key file location
            proxies: HTTP/SOCKS proxy to send requests with
        """

        self.__vpg_key = vpg_key
        self.__merchant_id = merchant_id
        self.__terminal_id = terminal_id
        self.__rsa_key_location = rsa_key_location
        self.__proxies = proxies

    @property
    def refund(self) -> RefundService:
        if not self.__rsa_key_location:
            raise AttributeError("RSA key is required for refund service")
        if not self.__merchant_id or not self.__terminal_id:
            raise AttributeError(
                "merchant_id and terminal_id are required for refund service"
            )

        return RefundService(
            vpg_key=self.__vpg_key,
            rsa_key_location=self.__rsa_key_location,
            proxies=self.__proxies,
        )

    @property
    def payment(self) -> PaymentService:
        if not self.__merchant_id or not self.__terminal_id:
            raise AttributeError(
                "merchant_id and terminal_id are required for payment service"
            )

        return PaymentService(
            vpg_key=self.__vpg_key,
            merchant_id=self.__merchant_id,
            terminal_id=self.__terminal_id,
            proxies=self.__proxies,
        )
