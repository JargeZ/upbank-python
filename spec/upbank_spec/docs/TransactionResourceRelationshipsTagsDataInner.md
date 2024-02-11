# TransactionResourceRelationshipsTagsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;tags&#x60; | 
**id** | **str** | The label of the tag, which also acts as the tag’s unique identifier.  | 

## Example

```python
from upbank_spec.models.transaction_resource_relationships_tags_data_inner import TransactionResourceRelationshipsTagsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationshipsTagsDataInner from a JSON string
transaction_resource_relationships_tags_data_inner_instance = TransactionResourceRelationshipsTagsDataInner.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationshipsTagsDataInner.to_json()

# convert the object into a dict
transaction_resource_relationships_tags_data_inner_dict = transaction_resource_relationships_tags_data_inner_instance.to_dict()
# create an instance of TransactionResourceRelationshipsTagsDataInner from a dict
transaction_resource_relationships_tags_data_inner_form_dict = transaction_resource_relationships_tags_data_inner.from_dict(transaction_resource_relationships_tags_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


