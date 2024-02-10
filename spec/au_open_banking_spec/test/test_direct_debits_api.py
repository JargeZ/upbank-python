# coding: utf-8

"""
    CDR Banking API

    Consumer Data Standards APIs created by the Data Standards Body (DSB), with the Data Standards Chair as the decision maker to meet the needs of the Consumer Data Right

    The version of the OpenAPI document: 1.29.0
    Contact: contact@consumerdatastandards.gov.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from au_open_banking_spec.api.direct_debits_api import DirectDebitsApi


class TestDirectDebitsApi(unittest.TestCase):
    """DirectDebitsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DirectDebitsApi()

    def tearDown(self) -> None:
        pass

    def test_list_direct_debits(self) -> None:
        """Test case for list_direct_debits

        Get Direct Debits For Account
        """
        pass

    def test_list_direct_debits_bulk(self) -> None:
        """Test case for list_direct_debits_bulk

        Get Bulk Direct Debits
        """
        pass

    def test_list_direct_debits_specific_accounts(self) -> None:
        """Test case for list_direct_debits_specific_accounts

        Get Direct Debits For Specific Accounts
        """
        pass


if __name__ == '__main__':
    unittest.main()