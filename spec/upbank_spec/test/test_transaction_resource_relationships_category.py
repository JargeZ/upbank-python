# coding: utf-8

"""
    Up API

    The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from upbank_spec.models.transaction_resource_relationships_category import TransactionResourceRelationshipsCategory

class TestTransactionResourceRelationshipsCategory(unittest.TestCase):
    """TransactionResourceRelationshipsCategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionResourceRelationshipsCategory:
        """Test TransactionResourceRelationshipsCategory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionResourceRelationshipsCategory`
        """
        model = TransactionResourceRelationshipsCategory()
        if include_optional:
            return TransactionResourceRelationshipsCategory(
                data = upbank_spec.models.category_resource_relationships_parent_data.CategoryResource_relationships_parent_data(
                    type = '', 
                    id = '', ),
                links = upbank_spec.models.transaction_resource_relationships_category_links.TransactionResource_relationships_category_links(
                    self = '', 
                    related = '', )
            )
        else:
            return TransactionResourceRelationshipsCategory(
                data = upbank_spec.models.category_resource_relationships_parent_data.CategoryResource_relationships_parent_data(
                    type = '', 
                    id = '', ),
        )
        """

    def testTransactionResourceRelationshipsCategory(self):
        """Test TransactionResourceRelationshipsCategory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
