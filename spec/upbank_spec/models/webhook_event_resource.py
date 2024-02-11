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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from upbank_spec.models.webhook_event_resource_attributes import WebhookEventResourceAttributes
from upbank_spec.models.webhook_event_resource_relationships import WebhookEventResourceRelationships
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WebhookEventResource(BaseModel):
    """
    Provides the event data used in asynchronous webhook event callbacks to subscribed endpoints. Webhooks events have defined `eventType`s and may optionally relate to other resources within the Up API. 
    """ # noqa: E501
    type: StrictStr = Field(description="The type of this resource: `webhook-events`")
    id: StrictStr = Field(description="The unique identifier for this event. This will remain constant across delivery retries. ")
    attributes: WebhookEventResourceAttributes
    relationships: WebhookEventResourceRelationships
    __properties: ClassVar[List[str]] = ["type", "id", "attributes", "relationships"]

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
        """Create an instance of WebhookEventResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relationships
        if self.relationships:
            _dict['relationships'] = self.relationships.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WebhookEventResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "attributes": WebhookEventResourceAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "relationships": WebhookEventResourceRelationships.from_dict(obj.get("relationships")) if obj.get("relationships") is not None else None
        })
        return _obj

