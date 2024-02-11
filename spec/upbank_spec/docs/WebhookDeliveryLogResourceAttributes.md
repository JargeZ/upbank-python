# WebhookDeliveryLogResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**WebhookDeliveryLogResourceAttributesRequest**](WebhookDeliveryLogResourceAttributesRequest.md) |  | 
**response** | [**WebhookDeliveryLogResourceAttributesResponse**](WebhookDeliveryLogResourceAttributesResponse.md) |  | 
**delivery_status** | [**WebhookDeliveryStatusEnum**](WebhookDeliveryStatusEnum.md) |  | 
**created_at** | **datetime** | The date-time at which this log entry was created.  | 

## Example

```python
from upbank_spec.models.webhook_delivery_log_resource_attributes import WebhookDeliveryLogResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogResourceAttributes from a JSON string
webhook_delivery_log_resource_attributes_instance = WebhookDeliveryLogResourceAttributes.from_json(json)
# print the JSON string representation of the object
print WebhookDeliveryLogResourceAttributes.to_json()

# convert the object into a dict
webhook_delivery_log_resource_attributes_dict = webhook_delivery_log_resource_attributes_instance.to_dict()
# create an instance of WebhookDeliveryLogResourceAttributes from a dict
webhook_delivery_log_resource_attributes_form_dict = webhook_delivery_log_resource_attributes.from_dict(webhook_delivery_log_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


