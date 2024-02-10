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

from au_open_banking_spec.models.banking_payee_detail_v2_all_of import BankingPayeeDetailV2AllOf

class TestBankingPayeeDetailV2AllOf(unittest.TestCase):
    """BankingPayeeDetailV2AllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankingPayeeDetailV2AllOf:
        """Test BankingPayeeDetailV2AllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankingPayeeDetailV2AllOf`
        """
        model = BankingPayeeDetailV2AllOf()
        if include_optional:
            return BankingPayeeDetailV2AllOf(
                payee_u_type = 'biller',
                biller = {"billerName":"billerName","crn":"crn","billerCode":"billerCode"},
                domestic = {"payeeAccountUType":"account","payId":{"identifier":"identifier","name":"name","type":"ABN"},"account":{"bsb":"bsb","accountName":"accountName","accountNumber":"accountNumber"},"card":{"cardNumber":"cardNumber"}},
                digital_wallet = {"identifier":"identifier","provider":"PAYPAL_AU","name":"name","type":"EMAIL"},
                international = {"bankDetails":{"country":"country","routingNumber":"routingNumber","fedWireNumber":"fedWireNumber","chipNumber":"chipNumber","legalEntityIdentifier":"legalEntityIdentifier","accountNumber":"accountNumber","bankAddress":{"address":"address","name":"name"},"sortCode":"sortCode","beneficiaryBankBIC":"beneficiaryBankBIC"},"beneficiaryDetails":{"country":"country","name":"name","message":"message"}}
            )
        else:
            return BankingPayeeDetailV2AllOf(
                payee_u_type = 'biller',
        )
        """

    def testBankingPayeeDetailV2AllOf(self):
        """Test BankingPayeeDetailV2AllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()