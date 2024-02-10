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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from au_open_banking_spec.models.banking_account_detail_v3_all_of_features_inner import BankingAccountDetailV3AllOfFeaturesInner
from au_open_banking_spec.models.banking_credit_card_account import BankingCreditCardAccount
from au_open_banking_spec.models.banking_loan_account_v2 import BankingLoanAccountV2
from au_open_banking_spec.models.banking_product_deposit_rate import BankingProductDepositRate
from au_open_banking_spec.models.banking_product_fee import BankingProductFee
from au_open_banking_spec.models.banking_product_lending_rate_v2 import BankingProductLendingRateV2
from au_open_banking_spec.models.banking_term_deposit_account import BankingTermDepositAccount
from au_open_banking_spec.models.common_physical_address import CommonPhysicalAddress
from typing import Optional, Set
from typing_extensions import Self

class BankingAccountDetailV3AllOf(BaseModel):
    """
    BankingAccountDetailV3AllOf
    """ # noqa: E501
    bsb: Optional[StrictStr] = Field(default=None, description="The unmasked BSB for the account. Is expected to be formatted as digits only with leading zeros included and no punctuation or spaces")
    account_number: Optional[StrictStr] = Field(default=None, description="The unmasked account number for the account. Should not be supplied if the account number is a PAN requiring PCI compliance. Is expected to be formatted as digits only with leading zeros included and no punctuation or spaces", alias="accountNumber")
    bundle_name: Optional[StrictStr] = Field(default=None, description="Optional field to indicate if this account is part of a bundle that is providing additional benefit to the customer", alias="bundleName")
    specific_account_u_type: Optional[StrictStr] = Field(default=None, description="The type of structure to present account specific fields.", alias="specificAccountUType")
    term_deposit: Optional[List[BankingTermDepositAccount]] = Field(default=None, alias="termDeposit")
    credit_card: Optional[BankingCreditCardAccount] = Field(default=None, alias="creditCard")
    loan: Optional[BankingLoanAccountV2] = None
    deposit_rate: Optional[StrictStr] = Field(default=None, description="current rate to calculate interest earned being applied to deposit balances as it stands at the time of the API call", alias="depositRate")
    lending_rate: Optional[StrictStr] = Field(default=None, description="The current rate to calculate interest payable being applied to lending balances as it stands at the time of the API call", alias="lendingRate")
    deposit_rates: Optional[List[BankingProductDepositRate]] = Field(default=None, description="Fully described deposit rates for this account based on the equivalent structure in Product Reference", alias="depositRates")
    lending_rates: Optional[List[BankingProductLendingRateV2]] = Field(default=None, description="Fully described lending rates for this account based on the equivalent structure in Product Reference", alias="lendingRates")
    features: Optional[List[BankingAccountDetailV3AllOfFeaturesInner]] = Field(default=None, description="Array of features of the account based on the equivalent structure in Product Reference with the following additional field")
    fees: Optional[List[BankingProductFee]] = Field(default=None, description="Fees and charges applicable to the account based on the equivalent structure in Product Reference")
    addresses: Optional[List[CommonPhysicalAddress]] = Field(default=None, description="The addresses for the account to be used for correspondence")
    __properties: ClassVar[List[str]] = ["bsb", "accountNumber", "bundleName", "specificAccountUType", "termDeposit", "creditCard", "loan", "depositRate", "lendingRate", "depositRates", "lendingRates", "features", "fees", "addresses"]

    @field_validator('specific_account_u_type')
    def specific_account_u_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['creditCard', 'loan', 'termDeposit']):
            raise ValueError("must be one of enum values ('creditCard', 'loan', 'termDeposit')")
        return value

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
        """Create an instance of BankingAccountDetailV3AllOf from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in term_deposit (list)
        _items = []
        if self.term_deposit:
            for _item in self.term_deposit:
                if _item:
                    _items.append(_item.to_dict())
            _dict['termDeposit'] = _items
        # override the default output from pydantic by calling `to_dict()` of credit_card
        if self.credit_card:
            _dict['creditCard'] = self.credit_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loan
        if self.loan:
            _dict['loan'] = self.loan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in deposit_rates (list)
        _items = []
        if self.deposit_rates:
            for _item in self.deposit_rates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['depositRates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lending_rates (list)
        _items = []
        if self.lending_rates:
            for _item in self.lending_rates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lendingRates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item in self.features:
                if _item:
                    _items.append(_item.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fees (list)
        _items = []
        if self.fees:
            for _item in self.fees:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankingAccountDetailV3AllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bsb": obj.get("bsb"),
            "accountNumber": obj.get("accountNumber"),
            "bundleName": obj.get("bundleName"),
            "specificAccountUType": obj.get("specificAccountUType"),
            "termDeposit": [BankingTermDepositAccount.from_dict(_item) for _item in obj["termDeposit"]] if obj.get("termDeposit") is not None else None,
            "creditCard": BankingCreditCardAccount.from_dict(obj["creditCard"]) if obj.get("creditCard") is not None else None,
            "loan": BankingLoanAccountV2.from_dict(obj["loan"]) if obj.get("loan") is not None else None,
            "depositRate": obj.get("depositRate"),
            "lendingRate": obj.get("lendingRate"),
            "depositRates": [BankingProductDepositRate.from_dict(_item) for _item in obj["depositRates"]] if obj.get("depositRates") is not None else None,
            "lendingRates": [BankingProductLendingRateV2.from_dict(_item) for _item in obj["lendingRates"]] if obj.get("lendingRates") is not None else None,
            "features": [BankingAccountDetailV3AllOfFeaturesInner.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "fees": [BankingProductFee.from_dict(_item) for _item in obj["fees"]] if obj.get("fees") is not None else None,
            "addresses": [CommonPhysicalAddress.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None
        })
        return _obj


