# coding: utf-8

"""
    CDR Banking API

    Consumer Data Standards APIs created by the Data Standards Body (DSB), with the Data Standards Chair as the decision maker to meet the needs of the Consumer Data Right

    The version of the OpenAPI document: 1.29.0
    Contact: contact@consumerdatastandards.gov.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from au_open_banking_spec.models.banking_product_additional_information_v2_additional_information_uris import BankingProductAdditionalInformationV2AdditionalInformationUris
from typing import Optional, Set
from typing_extensions import Self

class BankingProductAdditionalInformationV2(BaseModel):
    """
    Object that contains links to additional information on specific topics
    """ # noqa: E501
    overview_uri: Optional[StrictStr] = Field(default=None, description="General overview of the product. Mandatory if `additionalOverviewUris` includes one or more supporting documents.", alias="overviewUri")
    terms_uri: Optional[StrictStr] = Field(default=None, description="Terms and conditions for the product. Mandatory if `additionalTermsUris` includes one or more supporting documents.", alias="termsUri")
    eligibility_uri: Optional[StrictStr] = Field(default=None, description="Eligibility rules and criteria for the product. Mandatory if `additionalEligibilityUris` includes one or more supporting documents.", alias="eligibilityUri")
    fees_and_pricing_uri: Optional[StrictStr] = Field(default=None, description="Description of fees, pricing, discounts, exemptions and bonuses for the product. Mandatory if `additionalFeesAndPricingUris` includes one or more supporting documents.", alias="feesAndPricingUri")
    bundle_uri: Optional[StrictStr] = Field(default=None, description="Description of a bundle that this product can be part of. Mandatory if `additionalBundleUris` includes one or more supporting documents.", alias="bundleUri")
    additional_overview_uris: Optional[List[BankingProductAdditionalInformationV2AdditionalInformationUris]] = Field(default=None, description="An array of additional general overviews for the product or features of the product, if applicable. To be treated as secondary documents to the `overviewUri`. Only to be used if there is a primary `overviewUri`.", alias="additionalOverviewUris")
    additional_terms_uris: Optional[List[BankingProductAdditionalInformationV2AdditionalInformationUris]] = Field(default=None, description="An array of additional terms and conditions for the product, if applicable. To be treated as secondary documents to the `termsUri`. Only to be used if there is a primary `termsUri`.", alias="additionalTermsUris")
    additional_eligibility_uris: Optional[List[BankingProductAdditionalInformationV2AdditionalInformationUris]] = Field(default=None, description="An array of additional eligibility rules and criteria for the product, if applicable. To be treated as secondary documents to the `eligibilityUri`. Only to be used if there is a primary `eligibilityUri`.", alias="additionalEligibilityUris")
    additional_fees_and_pricing_uris: Optional[List[BankingProductAdditionalInformationV2AdditionalInformationUris]] = Field(default=None, description="An array of additional fees, pricing, discounts, exemptions and bonuses for the product, if applicable. To be treated as secondary documents to the `feesAndPricingUri`. Only to be used if there is a primary `feesAndPricingUri`.", alias="additionalFeesAndPricingUris")
    additional_bundle_uris: Optional[List[BankingProductAdditionalInformationV2AdditionalInformationUris]] = Field(default=None, description="An array of additional bundles for the product, if applicable. To be treated as secondary documents to the `bundleUri`. Only to be used if there is a primary `bundleUri`.", alias="additionalBundleUris")
    __properties: ClassVar[List[str]] = ["overviewUri", "termsUri", "eligibilityUri", "feesAndPricingUri", "bundleUri", "additionalOverviewUris", "additionalTermsUris", "additionalEligibilityUris", "additionalFeesAndPricingUris", "additionalBundleUris"]

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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BankingProductAdditionalInformationV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in additional_overview_uris (list)
        _items = []
        if self.additional_overview_uris:
            for _item in self.additional_overview_uris:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalOverviewUris'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_terms_uris (list)
        _items = []
        if self.additional_terms_uris:
            for _item in self.additional_terms_uris:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalTermsUris'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_eligibility_uris (list)
        _items = []
        if self.additional_eligibility_uris:
            for _item in self.additional_eligibility_uris:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalEligibilityUris'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_fees_and_pricing_uris (list)
        _items = []
        if self.additional_fees_and_pricing_uris:
            for _item in self.additional_fees_and_pricing_uris:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalFeesAndPricingUris'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_bundle_uris (list)
        _items = []
        if self.additional_bundle_uris:
            for _item in self.additional_bundle_uris:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalBundleUris'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankingProductAdditionalInformationV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "overviewUri": obj.get("overviewUri"),
            "termsUri": obj.get("termsUri"),
            "eligibilityUri": obj.get("eligibilityUri"),
            "feesAndPricingUri": obj.get("feesAndPricingUri"),
            "bundleUri": obj.get("bundleUri"),
            "additionalOverviewUris": [BankingProductAdditionalInformationV2AdditionalInformationUris.from_dict(_item) for _item in obj["additionalOverviewUris"]] if obj.get("additionalOverviewUris") is not None else None,
            "additionalTermsUris": [BankingProductAdditionalInformationV2AdditionalInformationUris.from_dict(_item) for _item in obj["additionalTermsUris"]] if obj.get("additionalTermsUris") is not None else None,
            "additionalEligibilityUris": [BankingProductAdditionalInformationV2AdditionalInformationUris.from_dict(_item) for _item in obj["additionalEligibilityUris"]] if obj.get("additionalEligibilityUris") is not None else None,
            "additionalFeesAndPricingUris": [BankingProductAdditionalInformationV2AdditionalInformationUris.from_dict(_item) for _item in obj["additionalFeesAndPricingUris"]] if obj.get("additionalFeesAndPricingUris") is not None else None,
            "additionalBundleUris": [BankingProductAdditionalInformationV2AdditionalInformationUris.from_dict(_item) for _item in obj["additionalBundleUris"]] if obj.get("additionalBundleUris") is not None else None
        })
        return _obj


