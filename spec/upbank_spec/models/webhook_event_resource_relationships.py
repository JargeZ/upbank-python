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
from upbank_spec.models.webhook_event_resource_relationships_transaction import WebhookEventResourceRelationshipsTransaction
from upbank_spec.models.webhook_event_resource_relationships_webhook import WebhookEventResourceRelationshipsWebhook
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WebhookEventResourceRelationships(BaseModel):
    """
    WebhookEventResourceRelationships
    """ # noqa: E501
    webhook: WebhookEventResourceRelationshipsWebhook
    transaction: Optional[WebhookEventResourceRelationshipsTransaction] = None
    __properties: ClassVar[List[str]] = ["webhook", "transaction"]

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
        """Create an instance of WebhookEventResourceRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of webhook
        if self.webhook:
            _dict['webhook'] = self.webhook.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WebhookEventResourceRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "webhook": WebhookEventResourceRelationshipsWebhook.from_dict(obj.get("webhook")) if obj.get("webhook") is not None else None,
            "transaction": WebhookEventResourceRelationshipsTransaction.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None
        })
        return _obj


