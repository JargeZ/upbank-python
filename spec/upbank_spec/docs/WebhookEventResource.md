# WebhookEventResource

Provides the event data used in asynchronous webhook event callbacks to subscribed endpoints. Webhooks events have defined `eventType`s and may optionally relate to other resources within the Up API. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;webhook-events&#x60; | 
**id** | **str** | The unique identifier for this event. This will remain constant across delivery retries.  | 
**attributes** | [**WebhookEventResourceAttributes**](WebhookEventResourceAttributes.md) |  | 
**relationships** | [**WebhookEventResourceRelationships**](WebhookEventResourceRelationships.md) |  | 

## Example

```python
from upbank_spec.models.webhook_event_resource import WebhookEventResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventResource from a JSON string
webhook_event_resource_instance = WebhookEventResource.from_json(json)
# print the JSON string representation of the object
print WebhookEventResource.to_json()

# convert the object into a dict
webhook_event_resource_dict = webhook_event_resource_instance.to_dict()
# create an instance of WebhookEventResource from a dict
webhook_event_resource_form_dict = webhook_event_resource.from_dict(webhook_event_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


