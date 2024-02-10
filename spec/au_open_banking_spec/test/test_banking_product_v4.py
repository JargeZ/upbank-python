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

from au_open_banking_spec.models.banking_product_v4 import BankingProductV4

class TestBankingProductV4(unittest.TestCase):
    """BankingProductV4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankingProductV4:
        """Test BankingProductV4
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankingProductV4`
        """
        model = BankingProductV4()
        if include_optional:
            return BankingProductV4(
                product_id = '',
                effective_from = '',
                effective_to = '',
                last_updated = '',
                product_category = 'BUSINESS_LOANS',
                name = '',
                description = '',
                brand = '',
                brand_name = '',
                application_uri = '',
                is_tailored = True,
                additional_information = {"eligibilityUri":"eligibilityUri","additionalFeesAndPricingUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalTermsUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"bundleUri":"bundleUri","feesAndPricingUri":"feesAndPricingUri","additionalBundleUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalEligibilityUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalOverviewUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"termsUri":"termsUri","overviewUri":"overviewUri"},
                card_art = [
                    {"imageUri":"imageUri","title":"title"}
                    ]
            )
        else:
            return BankingProductV4(
                product_id = '',
                last_updated = '',
                product_category = 'BUSINESS_LOANS',
                name = '',
                description = '',
                brand = '',
                is_tailored = True,
        )
        """

    def testBankingProductV4(self):
        """Test BankingProductV4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
