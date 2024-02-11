# TagInputResourceIdentifier

Uniquely identifies a single tag in the API. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;tags&#x60; | 
**id** | **str** | The label of the tag, which also acts as the tag’s unique identifier.  | 

## Example

```python
from upbank_spec.models.tag_input_resource_identifier import TagInputResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TagInputResourceIdentifier from a JSON string
tag_input_resource_identifier_instance = TagInputResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print TagInputResourceIdentifier.to_json()

# convert the object into a dict
tag_input_resource_identifier_dict = tag_input_resource_identifier_instance.to_dict()
# create an instance of TagInputResourceIdentifier from a dict
tag_input_resource_identifier_form_dict = tag_input_resource_identifier.from_dict(tag_input_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


