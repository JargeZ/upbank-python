# GetCategoryResponse

Successful response to get a single category and its ancestry. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CategoryResource**](CategoryResource.md) |  | 

## Example

```python
from upbank_spec.models.get_category_response import GetCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoryResponse from a JSON string
get_category_response_instance = GetCategoryResponse.from_json(json)
# print the JSON string representation of the object
print GetCategoryResponse.to_json()

# convert the object into a dict
get_category_response_dict = get_category_response_instance.to_dict()
# create an instance of GetCategoryResponse from a dict
get_category_response_form_dict = get_category_response.from_dict(get_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


