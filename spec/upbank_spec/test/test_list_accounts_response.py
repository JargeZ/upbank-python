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

from upbank_spec.models.list_accounts_response import ListAccountsResponse

class TestListAccountsResponse(unittest.TestCase):
    """ListAccountsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAccountsResponse:
        """Test ListAccountsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAccountsResponse`
        """
        model = ListAccountsResponse()
        if include_optional:
            return ListAccountsResponse(
                data = [
                    upbank_spec.models.account_resource.AccountResource(
                        type = '', 
                        id = '', 
                        attributes = upbank_spec.models.account_resource_attributes.AccountResource_attributes(
                            display_name = '', 
                            account_type = null, 
                            ownership_type = null, 
                            balance = null, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        relationships = upbank_spec.models.account_resource_relationships.AccountResource_relationships(
                            transactions = upbank_spec.models.account_resource_relationships_transactions.AccountResource_relationships_transactions(
                                links = upbank_spec.models.account_resource_relationships_transactions_links.AccountResource_relationships_transactions_links(
                                    related = '', ), ), ), 
                        links = upbank_spec.models.account_resource_links.AccountResource_links(
                            self = '', ), )
                    ],
                links = upbank_spec.models.list_accounts_response_links.ListAccountsResponse_links(
                    prev = '', 
                    next = '', )
            )
        else:
            return ListAccountsResponse(
                data = [
                    upbank_spec.models.account_resource.AccountResource(
                        type = '', 
                        id = '', 
                        attributes = upbank_spec.models.account_resource_attributes.AccountResource_attributes(
                            display_name = '', 
                            account_type = null, 
                            ownership_type = null, 
                            balance = null, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        relationships = upbank_spec.models.account_resource_relationships.AccountResource_relationships(
                            transactions = upbank_spec.models.account_resource_relationships_transactions.AccountResource_relationships_transactions(
                                links = upbank_spec.models.account_resource_relationships_transactions_links.AccountResource_relationships_transactions_links(
                                    related = '', ), ), ), 
                        links = upbank_spec.models.account_resource_links.AccountResource_links(
                            self = '', ), )
                    ],
                links = upbank_spec.models.list_accounts_response_links.ListAccountsResponse_links(
                    prev = '', 
                    next = '', ),
        )
        """

    def testListAccountsResponse(self):
        """Test ListAccountsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
