# coding: utf-8

"""
    Up API

    The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from upbank_spec.api.categories_api import CategoriesApi


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CategoriesApi()

    def tearDown(self) -> None:
        pass

    def test_categories_get(self) -> None:
        """Test case for categories_get

        List categories
        """
        pass

    def test_categories_id_get(self) -> None:
        """Test case for categories_id_get

        Retrieve category
        """
        pass

    def test_transactions_transaction_id_relationships_category_patch(self) -> None:
        """Test case for transactions_transaction_id_relationships_category_patch

        Categorize transaction
        """
        pass


if __name__ == '__main__':
    unittest.main()
