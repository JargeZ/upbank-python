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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from upbank_spec.models.category_resource_relationships_parent import CategoryResourceRelationshipsParent
from upbank_spec.models.transaction_resource_relationships_account import TransactionResourceRelationshipsAccount
from upbank_spec.models.transaction_resource_relationships_category import TransactionResourceRelationshipsCategory
from upbank_spec.models.transaction_resource_relationships_tags import TransactionResourceRelationshipsTags
from upbank_spec.models.transaction_resource_relationships_transfer_account import TransactionResourceRelationshipsTransferAccount
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TransactionResourceRelationships(BaseModel):
    """
    TransactionResourceRelationships
    """ # noqa: E501
    account: TransactionResourceRelationshipsAccount
    transfer_account: TransactionResourceRelationshipsTransferAccount = Field(alias="transferAccount")
    category: TransactionResourceRelationshipsCategory
    parent_category: CategoryResourceRelationshipsParent = Field(alias="parentCategory")
    tags: TransactionResourceRelationshipsTags
    __properties: ClassVar[List[str]] = ["account", "transferAccount", "category", "parentCategory", "tags"]

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
        """Create an instance of TransactionResourceRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transfer_account
        if self.transfer_account:
            _dict['transferAccount'] = self.transfer_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_category
        if self.parent_category:
            _dict['parentCategory'] = self.parent_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TransactionResourceRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": TransactionResourceRelationshipsAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "transferAccount": TransactionResourceRelationshipsTransferAccount.from_dict(obj.get("transferAccount")) if obj.get("transferAccount") is not None else None,
            "category": TransactionResourceRelationshipsCategory.from_dict(obj.get("category")) if obj.get("category") is not None else None,
            "parentCategory": CategoryResourceRelationshipsParent.from_dict(obj.get("parentCategory")) if obj.get("parentCategory") is not None else None,
            "tags": TransactionResourceRelationshipsTags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None
        })
        return _obj


