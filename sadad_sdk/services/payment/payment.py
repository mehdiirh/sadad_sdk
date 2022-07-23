from . import input_objects as inp, output_objects as out
from sadad_sdk.core.sadad import SadadBase

from datetime import datetime
from typing import Optional, Union


class PaymentService(SadadBase):

    uri_path = "v0"

    def request(
        self,
        amount: int,
        order_id: int,
        return_url: str,
        additional_data: Optional[str] = None,
        multiplexing_data: Optional[Union[inp.MultiplexingData, dict]] = None,
        user_id: Optional[int] = None,
        application_name: Optional[str] = None,
    ) -> out.RequestPaymentResponse:

        if multiplexing_data and not isinstance(
            multiplexing_data, (dict, inp.MultiplexingData)
        ):
            raise ValueError(
                "multiplexing_data must be either a dict or an instance of MultiplexingData"
            )

        if isinstance(multiplexing_data, dict):
            multiplexing_data = inp.MultiplexingData.from_dict(multiplexing_data)

        params = inp.RequestPaymentParams(
            merchant_id=self._merchant_id,
            terminal_id=self._terminal_id,
            amount=amount,
            order_id=order_id,
            local_date_time=datetime.now(),
            return_url=return_url,
            additional_data=additional_data,
            multiplexing_data=multiplexing_data,
            user_id=user_id,
            application_name=application_name,
        )

        params.sign_data = self._create_sign_data(params.sign_values())

        response = self._send("/Request/PaymentRequest", params)
        return out.RequestPaymentResponse.from_dict(response)

    def verify(self, token: str) -> out.VerifyPaymentResponse:

        params = inp.VerifyPaymentParams(token=token)
        params.sign_data = self._create_sign_data(params.sign_values())

        response = self._send("/Advice/Verify", params)
        return out.VerifyPaymentResponse.from_dict(response)
