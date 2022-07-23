from sadad_sdk.core.objects import ResponseBase
from sadad_sdk.utils.decorators import recover_methods

from dataclasses_json import dataclass_json, LetterCase, Undefined

from dataclasses import dataclass


@dataclass
class BasePaymentResponse(ResponseBase):

    res_code: int
    description: str


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestPaymentResponse(BasePaymentResponse):

    token: str


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class VerifyPaymentResponse(BasePaymentResponse):

    amount: int
    retrival_ref_no: str
    system_trace_no: str
    order_id: int

