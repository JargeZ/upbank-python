# CategoryResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this category as seen in the Up application.  | 

## Example

```python
from upbank_spec.models.category_resource_attributes import CategoryResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResourceAttributes from a JSON string
category_resource_attributes_instance = CategoryResourceAttributes.from_json(json)
# print the JSON string representation of the object
print CategoryResourceAttributes.to_json()

# convert the object into a dict
category_resource_attributes_dict = category_resource_attributes_instance.to_dict()
# create an instance of CategoryResourceAttributes from a dict
category_resource_attributes_form_dict = category_resource_attributes.from_dict(category_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


