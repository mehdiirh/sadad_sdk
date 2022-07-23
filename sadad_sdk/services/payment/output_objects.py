from sadad_sdk.core.objects import ResponseBase
from sadad_sdk.utils.decorators import recover_methods

from dataclasses_json import dataclass_json, LetterCase, Undefined

from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class BasePaymentResponse(ResponseBase):

    res_code: int
    description: str


class RequestPaymentResponse(BasePaymentResponse):

    token: str


class VerifyPaymentResponse(BasePaymentResponse):

    amount: int
    retrival_ref_no: str
    system_trace_no: str
    order_id: int

