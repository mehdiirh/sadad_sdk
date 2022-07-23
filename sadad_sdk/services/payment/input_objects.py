from sadad_sdk.core.objects import ParamsBase, exclude_if_none
from sadad_sdk.utils.decorators import recover_methods

from dataclasses_json import dataclass_json, config, LetterCase, Undefined

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Literal


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class MultiplexingRow:

    iban_number: str
    value: str


@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class MultiplexingData:

    type: Literal["Amount", "Percentage"] = "Percentage"
    multiplexing_rows: list[MultiplexingRow] = field(default_factory=list)


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestPaymentParams(ParamsBase):
    @staticmethod
    def sign_params():
        return [
            "TerminalId",
            "OrderId",
            "Amount",
        ]

    merchant_id: str
    terminal_id: str
    amount: int
    order_id: int
    local_date_time: datetime
    return_url: str
    sign_data: str = ''
    additional_data: Optional[str] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    multiplexing_data: Optional[MultiplexingData] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    user_id: Optional[int] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )
    application_name: Optional[str] = field(
        metadata=config(exclude=exclude_if_none), default=None
    )


@recover_methods
@dataclass_json(letter_case=LetterCase.PASCAL, undefined=Undefined.EXCLUDE)
@dataclass
class VerifyPaymentParams(ParamsBase):

    @staticmethod
    def sign_params():
        return ["Token"]

    token: str
    sign_data: str = ''
