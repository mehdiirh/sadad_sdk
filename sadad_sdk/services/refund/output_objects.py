from sadad_sdk.core.objects import ResponseBase
from sadad_sdk.utils.decorators import recover_methods

from dataclasses_json import dataclass_json, LetterCase, Undefined

from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class OnlyRefundIdResponse(ResponseBase):
    """
    Responses that only have refund_id ( beside status codes and messages ) as
    response data, will inherit from this class
    """
    refund_id: int


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class ListRefundData:

    refund_id: int
    retrieval_ref_no: str
    amount: float
    terminal_id: str
    system_trace_no: str
    refund_amount: float
    token: str
    transfer_method: str
    refund_status: str
    refund_response_message: str
    create_date: datetime
    transfer_date: datetime
    transfer_id: str
    transfer_trans_no: str
    desc_account: str
    desc_card: str
    order_id: str
    status_title: str
    response_title: str
    bank_message: str
    error_message: str
    description: str


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class ListRefundHistoryData:

    refund_id: int
    status: str
    response_message: str
    action: str
    request_id: str
    client_ip: str
    create_date: datetime


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RefundDetails(ResponseBase):

    refund_id: int
    retrieval_ref_no: str
    amount: float
    terminal_id: str
    system_trace_no: str
    refund_amount: float
    token: str
    transfer_method: str
    refund_status: str
    refund_response_message: str
    create_date: datetime
    transfer_date: datetime
    transfer_id: str
    transfer_trans_no: str
    desc_account: str
    desc_card: str
    status_title: str
    response_title: str
    bank_message: str
    error_message: str
    description: str


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class ListRefundResponse(ResponseBase):

    refunds: list[ListRefundData] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class HistoryRefundResponse(ResponseBase):

    refund_histories: list[ListRefundHistoryData] = field(default_factory=list)


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class InquiryRefundResponse(ResponseBase):

    refund_id: int
    retrieval_ref_no: str
    amount: int
    terminal_id: str
    system_trace_no: str
    token: str
    refund_amount: int
    transfer_time: datetime
    refund_status: str
    refund_response_message: str
    error_message: str
    description: str


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RegisterRefundResponse(OnlyRefundIdResponse):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmRefundResponse(OnlyRefundIdResponse):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class CancelRefundResponse(OnlyRefundIdResponse):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RetryRefundResponse(OnlyRefundIdResponse):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RegisterWithNewCardRefundResponse(OnlyRefundIdResponse):
    ...
