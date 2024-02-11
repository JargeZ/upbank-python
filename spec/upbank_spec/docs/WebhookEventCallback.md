# WebhookEventCallback

Asynchronous callback request used for webhook event delivery. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookEventResource**](WebhookEventResource.md) |  | 

## Example

```python
from upbank_spec.models.webhook_event_callback import WebhookEventCallback

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventCallback from a JSON string
webhook_event_callback_instance = WebhookEventCallback.from_json(json)
# print the JSON string representation of the object
print WebhookEventCallback.to_json()

# convert the object into a dict
webhook_event_callback_dict = webhook_event_callback_instance.to_dict()
# create an instance of WebhookEventCallback from a dict
webhook_event_callback_form_dict = webhook_event_callback.from_dict(webhook_event_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


