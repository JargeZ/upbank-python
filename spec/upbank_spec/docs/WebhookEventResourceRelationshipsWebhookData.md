# WebhookEventResourceRelationshipsWebhookData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;webhooks&#x60; | 
**id** | **str** | The unique identifier of the resource within its type.  | 

## Example

```python
from upbank_spec.models.webhook_event_resource_relationships_webhook_data import WebhookEventResourceRelationshipsWebhookData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventResourceRelationshipsWebhookData from a JSON string
webhook_event_resource_relationships_webhook_data_instance = WebhookEventResourceRelationshipsWebhookData.from_json(json)
# print the JSON string representation of the object
print WebhookEventResourceRelationshipsWebhookData.to_json()

# convert the object into a dict
webhook_event_resource_relationships_webhook_data_dict = webhook_event_resource_relationships_webhook_data_instance.to_dict()
# create an instance of WebhookEventResourceRelationshipsWebhookData from a dict
webhook_event_resource_relationships_webhook_data_form_dict = webhook_event_resource_relationships_webhook_data.from_dict(webhook_event_resource_relationships_webhook_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


