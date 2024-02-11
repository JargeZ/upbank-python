# TransactionResourceRelationshipsCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CategoryResourceRelationshipsParentData**](CategoryResourceRelationshipsParentData.md) |  | 
**links** | [**TransactionResourceRelationshipsCategoryLinks**](TransactionResourceRelationshipsCategoryLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.transaction_resource_relationships_category import TransactionResourceRelationshipsCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationshipsCategory from a JSON string
transaction_resource_relationships_category_instance = TransactionResourceRelationshipsCategory.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationshipsCategory.to_json()

# convert the object into a dict
transaction_resource_relationships_category_dict = transaction_resource_relationships_category_instance.to_dict()
# create an instance of TransactionResourceRelationshipsCategory from a dict
transaction_resource_relationships_category_form_dict = transaction_resource_relationships_category.from_dict(transaction_resource_relationships_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


