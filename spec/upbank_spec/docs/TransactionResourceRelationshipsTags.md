# TransactionResourceRelationshipsTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransactionResourceRelationshipsTagsDataInner]**](TransactionResourceRelationshipsTagsDataInner.md) |  | 
**links** | [**TransactionResourceRelationshipsTagsLinks**](TransactionResourceRelationshipsTagsLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.transaction_resource_relationships_tags import TransactionResourceRelationshipsTags

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationshipsTags from a JSON string
transaction_resource_relationships_tags_instance = TransactionResourceRelationshipsTags.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationshipsTags.to_json()

# convert the object into a dict
transaction_resource_relationships_tags_dict = transaction_resource_relationships_tags_instance.to_dict()
# create an instance of TransactionResourceRelationshipsTags from a dict
transaction_resource_relationships_tags_form_dict = transaction_resource_relationships_tags.from_dict(transaction_resource_relationships_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


