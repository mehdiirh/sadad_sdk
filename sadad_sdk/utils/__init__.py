from .config import PAYMENT_URL


def create_payment_url_from_token(token):
    return PAYMENT_URL.format(token)
