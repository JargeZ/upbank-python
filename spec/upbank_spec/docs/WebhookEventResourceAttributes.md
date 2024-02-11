# WebhookEventResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**WebhookEventTypeEnum**](WebhookEventTypeEnum.md) |  | 
**created_at** | **datetime** | The date-time at which this event was generated.  | 

## Example

```python
from upbank_spec.models.webhook_event_resource_attributes import WebhookEventResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventResourceAttributes from a JSON string
webhook_event_resource_attributes_instance = WebhookEventResourceAttributes.from_json(json)
# print the JSON string representation of the object
print WebhookEventResourceAttributes.to_json()

# convert the object into a dict
webhook_event_resource_attributes_dict = webhook_event_resource_attributes_instance.to_dict()
# create an instance of WebhookEventResourceAttributes from a dict
webhook_event_resource_attributes_form_dict = webhook_event_resource_attributes.from_dict(webhook_event_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


