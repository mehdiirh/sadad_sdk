from sadad_sdk.services import RefundService, PaymentService


class Sadad:
    def __init__(
        self,
        vpg_key: str,
        merchant_id: str = None,
        terminal_id: int = None,
        rsa_key_location: str = None,
    ):
        self.__vpg_key = vpg_key
        self.__merchant_id = merchant_id
        self.__terminal_id = terminal_id
        self.__rsa_key_location = rsa_key_location

    @property
    def refund(self) -> RefundService:
        if not self.__rsa_key_location:
            raise AttributeError("RSA key is required for refund service")
        if not self.__merchant_id or not self.__terminal_id:
            raise AttributeError(
                "merchant_id and terminal_id are required for refund service"
            )

        return RefundService(self.__vpg_key, self.__rsa_key_location)

    @property
    def payment(self) -> PaymentService:
        if not self.__merchant_id or not self.__terminal_id:
            raise AttributeError(
                "merchant_id and terminal_id are required for payment service"
            )

        return PaymentService(self.__vpg_key, self.__merchant_id, self.__terminal_id)
