from sadad_sdk.services.refund import input_objects as inp, output_objects as out
from sadad_sdk.core.sadad import SadadBase

from datetime import datetime
from typing import Optional, Literal


class RefundService(SadadBase):

    uri_path = "v1/refund"

    def register(
        self,
        retrieval_ref_no: str,
        amount: int,
        system_trace_no: str,
        refund_amount: str,
        token: str,
        transfer_method: Literal[1, 2] = 1,
    ) -> out.RegisterRefundResponse:
        """
        Register new refund request

        Args:
            retrieval_ref_no: Transaction reference number
            amount: Transaction amount (original amount)
            system_trace_no: Transaction tracking code
            refund_amount: The refund amount (must be smaller than or equal to the original amount)
            token: Transaction token
            transfer_method: Refund's transfer method ( 1: to account | 2 : to card )

        Returns:
            RegisterRefundResponse
        """

        params = inp.RegisterRefundParams(
            retrieval_ref_no=retrieval_ref_no,
            amount=amount,
            terminal_id=self._terminal_id,
            system_trace_no=system_trace_no,
            refund_amount=refund_amount,
            token=token,
            transfer_method=transfer_method,
        )

        response = self._send("/Register", params)
        return out.RegisterRefundResponse.from_json(response)

    def refunds_list(
        self,
        from_date: datetime,
        to_date: datetime,
        page: int = 1,
        count: int = 30,
        retrieval_ref_no: Optional[str] = None,
        refund_status_code: Optional[int] = None,
        card_no: Optional[str] = None,
        refund_amount_from: Optional[int] = None,
        refund_amount_to: Optional[int] = None,
        order_id: Optional[str] = None,
    ) -> out.ListRefundResponse:
        """
        Get a list of all refunds

        Args:
            from_date: AD start datetime
            to_date: AD end datetime
            page: Page number
            count: Count of elements per page
            retrieval_ref_no: Transaction reference number [Optional]
            refund_status_code: Refund's status code [Optional]
            card_no: Card number [Optional]
            refund_amount_from: Refund amount minimum [Optional]
            refund_amount_to: Refund amount maximum [Optional]
            order_id: Order ID [Optional]

        Returns:
            ListRefundResponse

        """
        params = inp.ListRefundParams(
            terminal_id=self._terminal_id,
            from_date=from_date,
            to_date=to_date,
            page=page,
            count=count,
            retrieval_ref_no=retrieval_ref_no,
            refund_status_code=refund_status_code,
            card_no=card_no,
            refund_amount_from=refund_amount_from,
            refund_amount_to=refund_amount_to,
            order_id=order_id,
        )

        response = self._send("/Register", params)
        return out.ListRefundResponse.from_json(response)

    def register_with_new_card(
        self, refund_id: int, card_no: str
    ) -> out.RegisterWithNewCardRefundResponse:
        """
        Register refund request to a new card

        Args:
            refund_id: The refund ID
            card_no: The card number

        Returns:
            RegisterWithNewCardRefundResponse
        """

        params = inp.RegisterWithNewCardRefundParams(
            refund_id=refund_id, card_no=card_no
        )
        response = self._send("/history", params)
        return out.RegisterWithNewCardRefundResponse.from_json(response)

    def confirm(self, refund_id: int) -> out.ConfirmRefundResponse:
        """
        Confirm a registered refund

        Args:
            refund_id: The refund ID

        Returns:
            ConfirmRefundResponse
        """

        params = inp.ConfirmRefundParams(refund_id=refund_id)
        response = self._send("/Confirm", params)
        return out.RegisterRefundResponse.from_json(response)

    def cancel(self, refund_id: int) -> out.CancelRefundResponse:
        """
        Cancel a registered refund

        Args:
            refund_id: The refund ID

        Returns:
            CancelRefundResponse

        """
        params = inp.CancelRefundParams(refund_id=refund_id)
        response = self._send("/Cancel", params)
        return out.CancelRefundResponse.from_json(response)

    def retry(self, refund_id: int) -> out.RetryRefundResponse:
        """
        Retry a failed refund

        Args:
            refund_id: The refund ID

        Returns:
            RetryRefundResponse
        """

        params = inp.RetryRefundParams(refund_id=refund_id)
        response = self._send("/Confirm", params)
        return out.RetryRefundResponse.from_json(response)

    def inquiry(self, refund_id: int) -> out.InquiryRefundResponse:
        """
        Inquiry refund status

        Args:
            refund_id: The refund ID

        Returns:
            InquiryRefundResponse
        """

        params = inp.InqueryRefundParams(refund_id=refund_id)
        response = self._send("/Inquery", params)
        return out.InquiryRefundResponse.from_json(response)

    def detail(self, refund_id: int) -> out.RefundDetails:
        """
        Refund details

        Args:
            refund_id: The refund ID

        Returns:
            RefundDetails
        """

        params = inp.DetailRefundParams(refund_id=refund_id)
        response = self._send("/detail", params)
        return out.RefundDetails.from_json(response)

    def history(self, refund_id: int) -> out.HistoryRefundResponse:
        """
        Details of operations performed on the refund transaction

        Args:
            refund_id: The refund ID

        Returns:
            HistoryRefundResponse
        """

        params = inp.HistoryRefundParams(refund_id=refund_id)
        response = self._send("/history", params)
        return out.HistoryRefundResponse.from_json(response)
