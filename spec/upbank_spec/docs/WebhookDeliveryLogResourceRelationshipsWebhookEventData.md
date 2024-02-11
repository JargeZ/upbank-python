# WebhookDeliveryLogResourceRelationshipsWebhookEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;webhook-events&#x60; | 
**id** | **str** | The unique identifier of the resource within its type.  | 

## Example

```python
from upbank_spec.models.webhook_delivery_log_resource_relationships_webhook_event_data import WebhookDeliveryLogResourceRelationshipsWebhookEventData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogResourceRelationshipsWebhookEventData from a JSON string
webhook_delivery_log_resource_relationships_webhook_event_data_instance = WebhookDeliveryLogResourceRelationshipsWebhookEventData.from_json(json)
# print the JSON string representation of the object
print WebhookDeliveryLogResourceRelationshipsWebhookEventData.to_json()

# convert the object into a dict
webhook_delivery_log_resource_relationships_webhook_event_data_dict = webhook_delivery_log_resource_relationships_webhook_event_data_instance.to_dict()
# create an instance of WebhookDeliveryLogResourceRelationshipsWebhookEventData from a dict
webhook_delivery_log_resource_relationships_webhook_event_data_form_dict = webhook_delivery_log_resource_relationships_webhook_event_data.from_dict(webhook_delivery_log_resource_relationships_webhook_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


