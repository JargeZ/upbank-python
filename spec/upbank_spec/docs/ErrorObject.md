# ErrorObject

Provides information about an error processing a request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The HTTP status code associated with this error. This can also be obtained from the response headers. The status indicates the broad type of error according to HTTP semantics.  | 
**title** | **str** | A short description of this error. This should be stable across multiple occurrences of this type of error and typically expands on the reason for the status code.  | 
**detail** | **str** | A detailed description of this error. This should be considered unique to individual occurrences of an error and subject to change. It is useful for debugging purposes.  | 
**source** | [**ErrorObjectSource**](ErrorObjectSource.md) |  | [optional] 

## Example

```python
from upbank_spec.models.error_object import ErrorObject

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorObject from a JSON string
error_object_instance = ErrorObject.from_json(json)
# print the JSON string representation of the object
print ErrorObject.to_json()

# convert the object into a dict
error_object_dict = error_object_instance.to_dict()
# create an instance of ErrorObject from a dict
error_object_form_dict = error_object.from_dict(error_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


