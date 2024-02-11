# WebhookResourceRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**AccountResourceRelationshipsTransactions**](AccountResourceRelationshipsTransactions.md) |  | 

## Example

```python
from upbank_spec.models.webhook_resource_relationships import WebhookResourceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResourceRelationships from a JSON string
webhook_resource_relationships_instance = WebhookResourceRelationships.from_json(json)
# print the JSON string representation of the object
print WebhookResourceRelationships.to_json()

# convert the object into a dict
webhook_resource_relationships_dict = webhook_resource_relationships_instance.to_dict()
# create an instance of WebhookResourceRelationships from a dict
webhook_resource_relationships_form_dict = webhook_resource_relationships.from_dict(webhook_resource_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


