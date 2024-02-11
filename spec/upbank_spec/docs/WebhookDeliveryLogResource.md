# WebhookDeliveryLogResource

Provides historical webhook event delivery information for analysis and debugging purposes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;webhook-delivery-logs&#x60; | 
**id** | **str** | The unique identifier for this log entry.  | 
**attributes** | [**WebhookDeliveryLogResourceAttributes**](WebhookDeliveryLogResourceAttributes.md) |  | 
**relationships** | [**WebhookDeliveryLogResourceRelationships**](WebhookDeliveryLogResourceRelationships.md) |  | 

## Example

```python
from upbank_spec.models.webhook_delivery_log_resource import WebhookDeliveryLogResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogResource from a JSON string
webhook_delivery_log_resource_instance = WebhookDeliveryLogResource.from_json(json)
# print the JSON string representation of the object
print WebhookDeliveryLogResource.to_json()

# convert the object into a dict
webhook_delivery_log_resource_dict = webhook_delivery_log_resource_instance.to_dict()
# create an instance of WebhookDeliveryLogResource from a dict
webhook_delivery_log_resource_form_dict = webhook_delivery_log_resource.from_dict(webhook_delivery_log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


