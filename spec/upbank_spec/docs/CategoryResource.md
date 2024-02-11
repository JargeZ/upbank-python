# CategoryResource

Provides information about a category and its ancestry. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;categories&#x60; | 
**id** | **str** | The unique identifier for this category. This is a human-readable but URL-safe value.  | 
**attributes** | [**CategoryResourceAttributes**](CategoryResourceAttributes.md) |  | 
**relationships** | [**CategoryResourceRelationships**](CategoryResourceRelationships.md) |  | 
**links** | [**AccountResourceLinks**](AccountResourceLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.category_resource import CategoryResource

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResource from a JSON string
category_resource_instance = CategoryResource.from_json(json)
# print the JSON string representation of the object
print CategoryResource.to_json()

# convert the object into a dict
category_resource_dict = category_resource_instance.to_dict()
# create an instance of CategoryResource from a dict
category_resource_form_dict = category_resource.from_dict(category_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


