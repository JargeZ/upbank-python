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

from upbank_spec.models.category_resource_relationships import CategoryResourceRelationships

class TestCategoryResourceRelationships(unittest.TestCase):
    """CategoryResourceRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryResourceRelationships:
        """Test CategoryResourceRelationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryResourceRelationships`
        """
        model = CategoryResourceRelationships()
        if include_optional:
            return CategoryResourceRelationships(
                parent = upbank_spec.models.category_resource_relationships_parent.CategoryResource_relationships_parent(
                    data = upbank_spec.models.category_resource_relationships_parent_data.CategoryResource_relationships_parent_data(
                        type = '', 
                        id = '', ), 
                    links = upbank_spec.models.account_resource_relationships_transactions_links.AccountResource_relationships_transactions_links(
                        related = '', ), ),
                children = upbank_spec.models.category_resource_relationships_children.CategoryResource_relationships_children(
                    data = [
                        upbank_spec.models.category_resource_relationships_children_data_inner.CategoryResource_relationships_children_data_inner(
                            type = '', 
                            id = '', )
                        ], 
                    links = upbank_spec.models.account_resource_relationships_transactions_links.AccountResource_relationships_transactions_links(
                        related = '', ), )
            )
        else:
            return CategoryResourceRelationships(
                parent = upbank_spec.models.category_resource_relationships_parent.CategoryResource_relationships_parent(
                    data = upbank_spec.models.category_resource_relationships_parent_data.CategoryResource_relationships_parent_data(
                        type = '', 
                        id = '', ), 
                    links = upbank_spec.models.account_resource_relationships_transactions_links.AccountResource_relationships_transactions_links(
                        related = '', ), ),
                children = upbank_spec.models.category_resource_relationships_children.CategoryResource_relationships_children(
                    data = [
                        upbank_spec.models.category_resource_relationships_children_data_inner.CategoryResource_relationships_children_data_inner(
                            type = '', 
                            id = '', )
                        ], 
                    links = upbank_spec.models.account_resource_relationships_transactions_links.AccountResource_relationships_transactions_links(
                        related = '', ), ),
        )
        """

    def testCategoryResourceRelationships(self):
        """Test CategoryResourceRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
