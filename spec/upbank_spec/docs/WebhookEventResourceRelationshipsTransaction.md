# WebhookEventResourceRelationshipsTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookEventResourceRelationshipsTransactionData**](WebhookEventResourceRelationshipsTransactionData.md) |  | 
**links** | [**AccountResourceRelationshipsTransactionsLinks**](AccountResourceRelationshipsTransactionsLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.webhook_event_resource_relationships_transaction import WebhookEventResourceRelationshipsTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventResourceRelationshipsTransaction from a JSON string
webhook_event_resource_relationships_transaction_instance = WebhookEventResourceRelationshipsTransaction.from_json(json)
# print the JSON string representation of the object
print WebhookEventResourceRelationshipsTransaction.to_json()

# convert the object into a dict
webhook_event_resource_relationships_transaction_dict = webhook_event_resource_relationships_transaction_instance.to_dict()
# create an instance of WebhookEventResourceRelationshipsTransaction from a dict
webhook_event_resource_relationships_transaction_form_dict = webhook_event_resource_relationships_transaction.from_dict(webhook_event_resource_relationships_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


