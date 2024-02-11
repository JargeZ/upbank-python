# CategoryResourceRelationshipsChildrenDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;categories&#x60; | 
**id** | **str** | The unique identifier of the resource within its type.  | 

## Example

```python
from upbank_spec.models.category_resource_relationships_children_data_inner import CategoryResourceRelationshipsChildrenDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResourceRelationshipsChildrenDataInner from a JSON string
category_resource_relationships_children_data_inner_instance = CategoryResourceRelationshipsChildrenDataInner.from_json(json)
# print the JSON string representation of the object
print CategoryResourceRelationshipsChildrenDataInner.to_json()

# convert the object into a dict
category_resource_relationships_children_data_inner_dict = category_resource_relationships_children_data_inner_instance.to_dict()
# create an instance of CategoryResourceRelationshipsChildrenDataInner from a dict
category_resource_relationships_children_data_inner_form_dict = category_resource_relationships_children_data_inner.from_dict(category_resource_relationships_children_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


