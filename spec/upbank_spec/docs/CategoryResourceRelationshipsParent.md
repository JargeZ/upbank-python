# CategoryResourceRelationshipsParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CategoryResourceRelationshipsParentData**](CategoryResourceRelationshipsParentData.md) |  | 
**links** | [**AccountResourceRelationshipsTransactionsLinks**](AccountResourceRelationshipsTransactionsLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.category_resource_relationships_parent import CategoryResourceRelationshipsParent

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResourceRelationshipsParent from a JSON string
category_resource_relationships_parent_instance = CategoryResourceRelationshipsParent.from_json(json)
# print the JSON string representation of the object
print CategoryResourceRelationshipsParent.to_json()

# convert the object into a dict
category_resource_relationships_parent_dict = category_resource_relationships_parent_instance.to_dict()
# create an instance of CategoryResourceRelationshipsParent from a dict
category_resource_relationships_parent_form_dict = category_resource_relationships_parent.from_dict(category_resource_relationships_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


