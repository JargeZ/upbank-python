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

from upbank_spec.models.list_webhook_delivery_logs_response import ListWebhookDeliveryLogsResponse

class TestListWebhookDeliveryLogsResponse(unittest.TestCase):
    """ListWebhookDeliveryLogsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListWebhookDeliveryLogsResponse:
        """Test ListWebhookDeliveryLogsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListWebhookDeliveryLogsResponse`
        """
        model = ListWebhookDeliveryLogsResponse()
        if include_optional:
            return ListWebhookDeliveryLogsResponse(
                data = [
                    upbank_spec.models.webhook_delivery_log_resource.WebhookDeliveryLogResource(
                        type = '', 
                        id = '', 
                        attributes = upbank_spec.models.webhook_delivery_log_resource_attributes.WebhookDeliveryLogResource_attributes(
                            request = upbank_spec.models.webhook_delivery_log_resource_attributes_request.WebhookDeliveryLogResource_attributes_request(
                                body = '', ), 
                            response = upbank_spec.models.webhook_delivery_log_resource_attributes_response.WebhookDeliveryLogResource_attributes_response(
                                status_code = 56, 
                                body = '', ), 
                            delivery_status = null, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        relationships = upbank_spec.models.webhook_delivery_log_resource_relationships.WebhookDeliveryLogResource_relationships(
                            webhook_event = upbank_spec.models.webhook_delivery_log_resource_relationships_webhook_event.WebhookDeliveryLogResource_relationships_webhookEvent(
                                data = upbank_spec.models.webhook_delivery_log_resource_relationships_webhook_event_data.WebhookDeliveryLogResource_relationships_webhookEvent_data(
                                    type = '', 
                                    id = '', ), ), ), )
                    ],
                links = upbank_spec.models.list_accounts_response_links.ListAccountsResponse_links(
                    prev = '', 
                    next = '', )
            )
        else:
            return ListWebhookDeliveryLogsResponse(
                data = [
                    upbank_spec.models.webhook_delivery_log_resource.WebhookDeliveryLogResource(
                        type = '', 
                        id = '', 
                        attributes = upbank_spec.models.webhook_delivery_log_resource_attributes.WebhookDeliveryLogResource_attributes(
                            request = upbank_spec.models.webhook_delivery_log_resource_attributes_request.WebhookDeliveryLogResource_attributes_request(
                                body = '', ), 
                            response = upbank_spec.models.webhook_delivery_log_resource_attributes_response.WebhookDeliveryLogResource_attributes_response(
                                status_code = 56, 
                                body = '', ), 
                            delivery_status = null, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        relationships = upbank_spec.models.webhook_delivery_log_resource_relationships.WebhookDeliveryLogResource_relationships(
                            webhook_event = upbank_spec.models.webhook_delivery_log_resource_relationships_webhook_event.WebhookDeliveryLogResource_relationships_webhookEvent(
                                data = upbank_spec.models.webhook_delivery_log_resource_relationships_webhook_event_data.WebhookDeliveryLogResource_relationships_webhookEvent_data(
                                    type = '', 
                                    id = '', ), ), ), )
                    ],
                links = upbank_spec.models.list_accounts_response_links.ListAccountsResponse_links(
                    prev = '', 
                    next = '', ),
        )
        """

    def testListWebhookDeliveryLogsResponse(self):
        """Test ListWebhookDeliveryLogsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
