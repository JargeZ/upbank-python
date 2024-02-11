# WebhookEventResourceRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | [**WebhookEventResourceRelationshipsWebhook**](WebhookEventResourceRelationshipsWebhook.md) |  | 
**transaction** | [**WebhookEventResourceRelationshipsTransaction**](WebhookEventResourceRelationshipsTransaction.md) |  | [optional] 

## Example

```python
from upbank_spec.models.webhook_event_resource_relationships import WebhookEventResourceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventResourceRelationships from a JSON string
webhook_event_resource_relationships_instance = WebhookEventResourceRelationships.from_json(json)
# print the JSON string representation of the object
print WebhookEventResourceRelationships.to_json()

# convert the object into a dict
webhook_event_resource_relationships_dict = webhook_event_resource_relationships_instance.to_dict()
# create an instance of WebhookEventResourceRelationships from a dict
webhook_event_resource_relationships_form_dict = webhook_event_resource_relationships.from_dict(webhook_event_resource_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


