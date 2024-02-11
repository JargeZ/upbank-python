# WebhookEventResourceRelationshipsWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookEventResourceRelationshipsWebhookData**](WebhookEventResourceRelationshipsWebhookData.md) |  | 
**links** | [**AccountResourceRelationshipsTransactionsLinks**](AccountResourceRelationshipsTransactionsLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.webhook_event_resource_relationships_webhook import WebhookEventResourceRelationshipsWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventResourceRelationshipsWebhook from a JSON string
webhook_event_resource_relationships_webhook_instance = WebhookEventResourceRelationshipsWebhook.from_json(json)
# print the JSON string representation of the object
print WebhookEventResourceRelationshipsWebhook.to_json()

# convert the object into a dict
webhook_event_resource_relationships_webhook_dict = webhook_event_resource_relationships_webhook_instance.to_dict()
# create an instance of WebhookEventResourceRelationshipsWebhook from a dict
webhook_event_resource_relationships_webhook_form_dict = webhook_event_resource_relationships_webhook.from_dict(webhook_event_resource_relationships_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


