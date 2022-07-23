from sadad_sdk.services import RefundService


class Sadad:

    def __init__(self, VPG_KEY: str = None, RSA_KEY_LOCATION: str = None):
        self.__vpg_key = VPG_KEY
        self.__rsa_key_location = RSA_KEY_LOCATION

    @property
    def refund(self) -> RefundService:
        if not self.__vpg_key or not self.__rsa_key_location:
            raise AttributeError("Both VPG and RSA keys are required for refund service")

        return RefundService(self.__vpg_key, self.__rsa_key_location)
