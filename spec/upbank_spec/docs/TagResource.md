# TagResource

Provides information about a tag. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;tags&#x60; | 
**id** | **str** | The label of the tag, which also acts as the tag’s unique identifier.  | 
**relationships** | [**AccountResourceRelationships**](AccountResourceRelationships.md) |  | 

## Example

```python
from upbank_spec.models.tag_resource import TagResource

# TODO update the JSON string below
json = "{}"
# create an instance of TagResource from a JSON string
tag_resource_instance = TagResource.from_json(json)
# print the JSON string representation of the object
print TagResource.to_json()

# convert the object into a dict
tag_resource_dict = tag_resource_instance.to_dict()
# create an instance of TagResource from a dict
tag_resource_form_dict = tag_resource.from_dict(tag_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


