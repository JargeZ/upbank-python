# ErrorObjectSource

If applicable, location in the request that this error relates to. This may be a parameter in the query string, or a an attribute in the request body. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter** | **str** | If this error relates to a query parameter, the name of the parameter.  | [optional] 
**pointer** | **str** | If this error relates to an attribute in the request body, a rfc-6901 JSON pointer to the attribute.  | [optional] 

## Example

```python
from upbank_spec.models.error_object_source import ErrorObjectSource

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorObjectSource from a JSON string
error_object_source_instance = ErrorObjectSource.from_json(json)
# print the JSON string representation of the object
print ErrorObjectSource.to_json()

# convert the object into a dict
error_object_source_dict = error_object_source_instance.to_dict()
# create an instance of ErrorObjectSource from a dict
error_object_source_form_dict = error_object_source.from_dict(error_object_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


