# coding: utf-8

"""
    Up API

    The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from upbank_spec.models.money_object import MoneyObject
from upbank_spec.models.round_up_object_boost_portion import RoundUpObjectBoostPortion
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RoundUpObject(BaseModel):
    """
    Provides information about how a Round Up was applied, such as whether or not a boost was included in the Round Up. 
    """ # noqa: E501
    amount: MoneyObject
    boost_portion: Optional[RoundUpObjectBoostPortion] = Field(alias="boostPortion")
    __properties: ClassVar[List[str]] = ["amount", "boostPortion"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RoundUpObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of boost_portion
        if self.boost_portion:
            _dict['boostPortion'] = self.boost_portion.to_dict()
        # set to None if boost_portion (nullable) is None
        # and model_fields_set contains the field
        if self.boost_portion is None and "boost_portion" in self.model_fields_set:
            _dict['boostPortion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RoundUpObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": MoneyObject.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "boostPortion": RoundUpObjectBoostPortion.from_dict(obj.get("boostPortion")) if obj.get("boostPortion") is not None else None
        })
        return _obj

