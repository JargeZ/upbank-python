# WebhookDeliveryLogResourceAttributesResponse

Information about the response that was received from the webhook URL. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The HTTP status code received in the response.  | 
**body** | **str** | The payload that was received in the response body.  | 

## Example

```python
from upbank_spec.models.webhook_delivery_log_resource_attributes_response import WebhookDeliveryLogResourceAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogResourceAttributesResponse from a JSON string
webhook_delivery_log_resource_attributes_response_instance = WebhookDeliveryLogResourceAttributesResponse.from_json(json)
# print the JSON string representation of the object
print WebhookDeliveryLogResourceAttributesResponse.to_json()

# convert the object into a dict
webhook_delivery_log_resource_attributes_response_dict = webhook_delivery_log_resource_attributes_response_instance.to_dict()
# create an instance of WebhookDeliveryLogResourceAttributesResponse from a dict
webhook_delivery_log_resource_attributes_response_form_dict = webhook_delivery_log_resource_attributes_response.from_dict(webhook_delivery_log_resource_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


