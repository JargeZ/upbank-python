# CategoryResourceRelationshipsChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CategoryResourceRelationshipsChildrenDataInner]**](CategoryResourceRelationshipsChildrenDataInner.md) |  | 
**links** | [**AccountResourceRelationshipsTransactionsLinks**](AccountResourceRelationshipsTransactionsLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.category_resource_relationships_children import CategoryResourceRelationshipsChildren

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResourceRelationshipsChildren from a JSON string
category_resource_relationships_children_instance = CategoryResourceRelationshipsChildren.from_json(json)
# print the JSON string representation of the object
print CategoryResourceRelationshipsChildren.to_json()

# convert the object into a dict
category_resource_relationships_children_dict = category_resource_relationships_children_instance.to_dict()
# create an instance of CategoryResourceRelationshipsChildren from a dict
category_resource_relationships_children_form_dict = category_resource_relationships_children.from_dict(category_resource_relationships_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


