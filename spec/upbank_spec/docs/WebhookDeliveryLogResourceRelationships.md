# WebhookDeliveryLogResourceRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_event** | [**WebhookDeliveryLogResourceRelationshipsWebhookEvent**](WebhookDeliveryLogResourceRelationshipsWebhookEvent.md) |  | 

## Example

```python
from upbank_spec.models.webhook_delivery_log_resource_relationships import WebhookDeliveryLogResourceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogResourceRelationships from a JSON string
webhook_delivery_log_resource_relationships_instance = WebhookDeliveryLogResourceRelationships.from_json(json)
# print the JSON string representation of the object
print WebhookDeliveryLogResourceRelationships.to_json()

# convert the object into a dict
webhook_delivery_log_resource_relationships_dict = webhook_delivery_log_resource_relationships_instance.to_dict()
# create an instance of WebhookDeliveryLogResourceRelationships from a dict
webhook_delivery_log_resource_relationships_form_dict = webhook_delivery_log_resource_relationships.from_dict(webhook_delivery_log_resource_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


