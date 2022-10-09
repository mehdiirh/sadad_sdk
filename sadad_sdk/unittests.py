from dataclasses import dataclass
from datetime import datetime
from unittest import TestCase

from dataclasses_json import dataclass_json, LetterCase

from sadad_sdk.core.objects import ParamsBase, ResponseBase
from sadad_sdk.services.refund.output_objects import BaseRefundResponse
from sadad_sdk.utils.config import REQUEST_DATE_FORMAT, RESPONSE_DATETIME_FORMAT
from sadad_sdk.utils.decorators import recover_methods
from utils import create_payment_url_from_token
from utils.config import PAYMENT_URL


class TestResponseBaseObject(TestCase):
    def test_base_refund_response_status_and_response_message_attrs(self):

        # test BaseRefundResponse requires "status" and "response_message" by default
        self.assertRaises(TypeError, BaseRefundResponse, status=200)
        self.assertRaises(TypeError, BaseRefundResponse, response_message="message")

    def test_base_refund_response_initializing_and_functionality(self):
        try:
            instance = BaseRefundResponse(status=200, response_message="message")
        except Exception as e:
            self.fail(f"BaseRefundResponse() raised {e} unexpectedly")

        # test if response is valid if status and response message is passed
        self.assertIsInstance(instance, ResponseBase)

        self.assertEqual(
            sorted(instance.to_dict()),
            sorted({"status": 200, "response_message": "message"}),
        )

    def test_recover_methods_decorator_on_from_dict_method(self):

        self.assertTrue(hasattr(ResponseBase, "_from_dict"))

        # these should not be equal before recovering methods
        self.assertNotEqual(ResponseBase._from_dict, ResponseBase.from_dict)

        # test recover methods decorator
        recover_methods(ResponseBase)
        self.assertEqual(ResponseBase._from_dict, ResponseBase.from_dict)

    def test_base_refund_response_datetime_convertor(self):
        @recover_methods
        @dataclass_json(letter_case=LetterCase.PASCAL)
        @dataclass
        class BaseRefundResponseConverted(BaseRefundResponse):
            from_date: datetime

        time = datetime.now()
        str_time = time.strftime(RESPONSE_DATETIME_FORMAT)

        data = {"Status": 200, "ResponseMessage": "message", "FromDate": str_time}

        instance = BaseRefundResponseConverted.from_dict(data)

        self.assertIsInstance(instance.from_date, datetime)
        self.assertEqual(
            instance.from_date, datetime.strptime(str_time, RESPONSE_DATETIME_FORMAT)
        )

        dict_data = instance.to_dict()

        self.assertEqual(
            dict_data["FromDate"], datetime.strptime(str_time, RESPONSE_DATETIME_FORMAT)
        )


class TestParamsBaseObject(TestCase):
    @classmethod
    def setUp(cls) -> None:
        @recover_methods
        @dataclass_json(letter_case=LetterCase.PASCAL)
        @dataclass
        class ParamsBaseConverted(ParamsBase):
            @staticmethod
            def sign_params():
                return ["FromDate", "terminalId"]

            from_date: datetime
            terminal_id: str = "terminal_id"

        time = datetime.now()

        cls.converted_class = ParamsBaseConverted
        cls.time = time
        cls.str_time = time.strftime(REQUEST_DATE_FORMAT)

    def test_base_params_object_raise_not_implemented_error(self):
        self.assertRaises(NotImplementedError, ParamsBase)

    def test_base_params_child_attrs(self):
        self.assertRaises(TypeError, ResponseBase, terminal_id="message")

    def test_base_params_initializing_and_functionality(self):
        try:
            instance = self.converted_class(from_date=self.time)
        except Exception as e:
            self.fail(f"ParamsBase() raised {e} unexpectedly")

        # test if params object is valid if args is passed properly
        self.assertIsInstance(instance, ParamsBase)

        self.assertEqual(instance.from_date, self.time)

        self.assertEqual(
            sorted(instance.to_dict()),
            sorted({"FromDate": self.str_time, "TerminalId": "terminal_id"}),
        )

    def test_recover_methods_decorator_on_to_dict_method(self):
        self.assertTrue(hasattr(ParamsBase, "_to_dict"))

        # these should not be equal before recovering methods
        self.assertNotEqual(ParamsBase._to_dict, ParamsBase.to_dict)

        self.assertEqual(self.converted_class._to_dict, self.converted_class.to_dict)


class TestUtilsAndTools(TestCase):
    def test_create_payment_url_from_token(self):
        token = "TOKEN"

        self.assertEqual(
            create_payment_url_from_token(token), PAYMENT_URL.format(token)
        )
