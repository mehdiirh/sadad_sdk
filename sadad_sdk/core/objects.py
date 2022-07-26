import dataclasses
from datetime import datetime
from typing import Type

from dataclasses_json import DataClassJsonMixin
from dataclasses_json.api import Json, A
from dataclasses_json.utils import _is_optional, _hasargs

from sadad_sdk.utils.config import RESPONSE_DATETIME_FORMAT, REQUEST_DATE_FORMAT


def exclude_if_none(value):
    return value is None


@dataclasses.dataclass
class ParamsBase(DataClassJsonMixin):
    def __new__(cls, *args, **kwargs):
        cls.sign_params()
        return super().__new__(cls)

    def _to_dict(self, encode_json=False):
        _data = super().to_dict(encode_json=encode_json)

        for key, value in _data.items():
            if issubclass(type(value), datetime):
                _data[key] = datetime.strftime(value, REQUEST_DATE_FORMAT)

        return _data

    @staticmethod
    def sign_params():
        """
        Return required keys for signature
        """
        raise NotImplementedError

    def sign_values(self):
        """
        Attach values divided by semicolon [ ; ]

        Returns:
            str: A formatted string for signature
        """

        data = self.to_dict()
        values = [str(data[key]) for key in self.sign_params()]
        return ";".join(values)


@dataclasses.dataclass
class ResponseBase(DataClassJsonMixin):

    @classmethod
    def _from_dict(cls: Type[A], kvs: Json, *, infer_missing=False) -> A:
        letter_case = cls.dataclass_json_config.get('letter_case')  # get LetterCase if it exists

        for field in dataclasses.fields(cls):
            is_datetime = False
            if _is_optional(field.type):
                if _hasargs(field.type, datetime):
                    is_datetime = True
            elif issubclass(field.type, datetime):
                is_datetime = True

            if is_datetime:
                field_name = letter_case(field.name) if callable(letter_case) else field.name
                value = kvs.get(field_name)
                if value and (not isinstance(value, datetime)):
                    kvs[field_name] = datetime.strptime(value, RESPONSE_DATETIME_FORMAT)

        _data = super().from_dict(kvs, infer_missing=infer_missing)
        return _data
