# WebhookDeliveryLogResourceAttributesRequest

Information about the request that was sent to the webhook URL. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The payload that was sent in the request body.  | 

## Example

```python
from upbank_spec.models.webhook_delivery_log_resource_attributes_request import WebhookDeliveryLogResourceAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogResourceAttributesRequest from a JSON string
webhook_delivery_log_resource_attributes_request_instance = WebhookDeliveryLogResourceAttributesRequest.from_json(json)
# print the JSON string representation of the object
print WebhookDeliveryLogResourceAttributesRequest.to_json()

# convert the object into a dict
webhook_delivery_log_resource_attributes_request_dict = webhook_delivery_log_resource_attributes_request_instance.to_dict()
# create an instance of WebhookDeliveryLogResourceAttributesRequest from a dict
webhook_delivery_log_resource_attributes_request_form_dict = webhook_delivery_log_resource_attributes_request.from_dict(webhook_delivery_log_resource_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


