# CategoryResourceRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**CategoryResourceRelationshipsParent**](CategoryResourceRelationshipsParent.md) |  | 
**children** | [**CategoryResourceRelationshipsChildren**](CategoryResourceRelationshipsChildren.md) |  | 

## Example

```python
from upbank_spec.models.category_resource_relationships import CategoryResourceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResourceRelationships from a JSON string
category_resource_relationships_instance = CategoryResourceRelationships.from_json(json)
# print the JSON string representation of the object
print CategoryResourceRelationships.to_json()

# convert the object into a dict
category_resource_relationships_dict = category_resource_relationships_instance.to_dict()
# create an instance of CategoryResourceRelationships from a dict
category_resource_relationships_form_dict = category_resource_relationships.from_dict(category_resource_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


