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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from upbank_spec.models.money_object import MoneyObject
from upbank_spec.models.transaction_resource_attributes_cashback import TransactionResourceAttributesCashback
from upbank_spec.models.transaction_resource_attributes_foreign_amount import TransactionResourceAttributesForeignAmount
from upbank_spec.models.transaction_resource_attributes_hold_info import TransactionResourceAttributesHoldInfo
from upbank_spec.models.transaction_resource_attributes_round_up import TransactionResourceAttributesRoundUp
from upbank_spec.models.transaction_status_enum import TransactionStatusEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TransactionResourceAttributes(BaseModel):
    """
    TransactionResourceAttributes
    """ # noqa: E501
    status: TransactionStatusEnum
    raw_text: Optional[StrictStr] = Field(description="The original, unprocessed text of the transaction. This is often not a perfect indicator of the actual merchant, but it is useful for reconciliation purposes in some cases. ", alias="rawText")
    description: StrictStr = Field(description="A short description for this transaction. Usually the merchant name for purchases. ")
    message: Optional[StrictStr] = Field(description="Attached message for this transaction, such as a payment message, or a transfer note. ")
    is_categorizable: StrictBool = Field(description="Boolean flag set to true on transactions that support the use of categories. ", alias="isCategorizable")
    hold_info: Optional[TransactionResourceAttributesHoldInfo] = Field(alias="holdInfo")
    round_up: Optional[TransactionResourceAttributesRoundUp] = Field(alias="roundUp")
    cashback: Optional[TransactionResourceAttributesCashback]
    amount: MoneyObject
    foreign_amount: Optional[TransactionResourceAttributesForeignAmount] = Field(alias="foreignAmount")
    settled_at: Optional[datetime] = Field(description="The date-time at which this transaction settled. This field will be `null` for transactions that are currently in the `HELD` status. ", alias="settledAt")
    created_at: datetime = Field(description="The date-time at which this transaction was first encountered. ", alias="createdAt")
    __properties: ClassVar[List[str]] = ["status", "rawText", "description", "message", "isCategorizable", "holdInfo", "roundUp", "cashback", "amount", "foreignAmount", "settledAt", "createdAt"]

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
        """Create an instance of TransactionResourceAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of hold_info
        if self.hold_info:
            _dict['holdInfo'] = self.hold_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of round_up
        if self.round_up:
            _dict['roundUp'] = self.round_up.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cashback
        if self.cashback:
            _dict['cashback'] = self.cashback.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of foreign_amount
        if self.foreign_amount:
            _dict['foreignAmount'] = self.foreign_amount.to_dict()
        # set to None if raw_text (nullable) is None
        # and model_fields_set contains the field
        if self.raw_text is None and "raw_text" in self.model_fields_set:
            _dict['rawText'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if hold_info (nullable) is None
        # and model_fields_set contains the field
        if self.hold_info is None and "hold_info" in self.model_fields_set:
            _dict['holdInfo'] = None

        # set to None if round_up (nullable) is None
        # and model_fields_set contains the field
        if self.round_up is None and "round_up" in self.model_fields_set:
            _dict['roundUp'] = None

        # set to None if cashback (nullable) is None
        # and model_fields_set contains the field
        if self.cashback is None and "cashback" in self.model_fields_set:
            _dict['cashback'] = None

        # set to None if foreign_amount (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_amount is None and "foreign_amount" in self.model_fields_set:
            _dict['foreignAmount'] = None

        # set to None if settled_at (nullable) is None
        # and model_fields_set contains the field
        if self.settled_at is None and "settled_at" in self.model_fields_set:
            _dict['settledAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TransactionResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "rawText": obj.get("rawText"),
            "description": obj.get("description"),
            "message": obj.get("message"),
            "isCategorizable": obj.get("isCategorizable"),
            "holdInfo": TransactionResourceAttributesHoldInfo.from_dict(obj.get("holdInfo")) if obj.get("holdInfo") is not None else None,
            "roundUp": TransactionResourceAttributesRoundUp.from_dict(obj.get("roundUp")) if obj.get("roundUp") is not None else None,
            "cashback": TransactionResourceAttributesCashback.from_dict(obj.get("cashback")) if obj.get("cashback") is not None else None,
            "amount": MoneyObject.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "foreignAmount": TransactionResourceAttributesForeignAmount.from_dict(obj.get("foreignAmount")) if obj.get("foreignAmount") is not None else None,
            "settledAt": obj.get("settledAt"),
            "createdAt": obj.get("createdAt")
        })
        return _obj


