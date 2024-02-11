# coding: utf-8

"""
    Up API

    The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionStatusEnum(str, Enum):
    """
    Specifies which stage of processing a transaction is currently at. Currently returned values are `HELD` and `SETTLED`. When a transaction is held, its account’s `availableBalance` is affected. When a transaction is settled, its account’s `currentBalance` is affected. 
    """

    """
    allowed enum values
    """
    HELD = 'HELD'
    SETTLED = 'SETTLED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


