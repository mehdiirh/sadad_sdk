from sadad_sdk.services import RefundService


class Sadad:

    def __init__(self, VPG_KEY: str, RSA_KEY_LOCATION: str):
        self.refund = RefundService(VPG_KEY, RSA_KEY_LOCATION)
