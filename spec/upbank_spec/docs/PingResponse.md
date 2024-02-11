# PingResponse

Basic ping response to verify authentication. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PingResponseMeta**](PingResponseMeta.md) |  | 

## Example

```python
from upbank_spec.models.ping_response import PingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PingResponse from a JSON string
ping_response_instance = PingResponse.from_json(json)
# print the JSON string representation of the object
print PingResponse.to_json()

# convert the object into a dict
ping_response_dict = ping_response_instance.to_dict()
# create an instance of PingResponse from a dict
ping_response_form_dict = ping_response.from_dict(ping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


