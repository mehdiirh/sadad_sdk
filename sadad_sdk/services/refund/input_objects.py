from sadad_sdk.core.objects import ParamsBase, exclude_if_none
from sadad_sdk.utils.decorators import recover_methods

from dataclasses_json import dataclass_json, config, LetterCase, Undefined

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class OnlyRefundIdParam(ParamsBase):
    """
    Endpoints that only need refund_id as params, will inherit from this class
    """

    @staticmethod
    def sign_params():
        return ["RefundId"]

    refund_id: int


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RegisterRefundParams(ParamsBase):
    @staticmethod
    def sign_params():
        return [
            "RetrievalRefNo",
            "Amount",
            "TerminalId",
            "SystemTraceNo",
            "RefundAmount",
            "Token",
        ]

    retrieval_ref_no: str
    amount: int
    terminal_id: str
    system_trace_no: str
    refund_amount: int
    token: str
    transfer_method: Optional[int] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class ListRefundParams(ParamsBase):
    @staticmethod
    def sign_params():
        return ["TerminalId", "FromDate", "ToDate"]

    terminal_id: str
    from_date: datetime
    to_date: datetime
    page: int
    count: int
    retrieval_ref_no: Optional[str] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    refund_status_code: Optional[int] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    card_no: Optional[str] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    refund_amount_from: Optional[int] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    refund_amount_to: Optional[int] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    order_id: Optional[str] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RegisterWithNewCardRefundParams(ParamsBase):
    @staticmethod
    def sign_params():
        return ["RefundId", "CardNo"]

    refund_id: int
    card_no: str


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmRefundParams(OnlyRefundIdParam):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class CancelRefundParams(OnlyRefundIdParam):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class InqueryRefundParams(OnlyRefundIdParam):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RetryRefundParams(OnlyRefundIdParam):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class DetailRefundParams(OnlyRefundIdParam):
    ...


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class HistoryRefundParams(OnlyRefundIdParam):
    ...
