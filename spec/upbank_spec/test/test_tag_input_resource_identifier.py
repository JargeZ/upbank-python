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

from upbank_spec.models.tag_input_resource_identifier import TagInputResourceIdentifier

class TestTagInputResourceIdentifier(unittest.TestCase):
    """TagInputResourceIdentifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagInputResourceIdentifier:
        """Test TagInputResourceIdentifier
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagInputResourceIdentifier`
        """
        model = TagInputResourceIdentifier()
        if include_optional:
            return TagInputResourceIdentifier(
                type = '',
                id = ''
            )
        else:
            return TagInputResourceIdentifier(
                type = '',
                id = '',
        )
        """

    def testTagInputResourceIdentifier(self):
        """Test TagInputResourceIdentifier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
