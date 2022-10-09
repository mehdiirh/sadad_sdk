from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json, LetterCase, Undefined

from sadad_sdk.core.objects import ResponseBase
from sadad_sdk.utils import create_payment_url_from_token
from sadad_sdk.utils.decorators import recover_methods


@dataclass
class BasePaymentResponse(ResponseBase):

    res_code: int
    description: str


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestPaymentResponse(BasePaymentResponse):

    token: Optional[str] = None

    @property
    def payment_url(self):
        return create_payment_url_from_token(self.token)


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class VerifyPaymentResponse(BasePaymentResponse):

    amount: int
    retrival_ref_no: Optional[str]
    system_trace_no: Optional[str]
    order_id: Optional[int]

