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

from upbank_spec.models.list_accounts_response_links import ListAccountsResponseLinks

class TestListAccountsResponseLinks(unittest.TestCase):
    """ListAccountsResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAccountsResponseLinks:
        """Test ListAccountsResponseLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAccountsResponseLinks`
        """
        model = ListAccountsResponseLinks()
        if include_optional:
            return ListAccountsResponseLinks(
                prev = '',
                next = ''
            )
        else:
            return ListAccountsResponseLinks(
                prev = '',
                next = '',
        )
        """

    def testListAccountsResponseLinks(self):
        """Test ListAccountsResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
