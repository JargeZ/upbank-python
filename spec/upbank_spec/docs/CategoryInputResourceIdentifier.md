# CategoryInputResourceIdentifier

Uniquely identifies a category in the API. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;categories&#x60; | 
**id** | **str** | The unique identifier of the category, as returned by the &#x60;/categories&#x60; endpoint.  | 

## Example

```python
from upbank_spec.models.category_input_resource_identifier import CategoryInputResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryInputResourceIdentifier from a JSON string
category_input_resource_identifier_instance = CategoryInputResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print CategoryInputResourceIdentifier.to_json()

# convert the object into a dict
category_input_resource_identifier_dict = category_input_resource_identifier_instance.to_dict()
# create an instance of CategoryInputResourceIdentifier from a dict
category_input_resource_identifier_form_dict = category_input_resource_identifier.from_dict(category_input_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


