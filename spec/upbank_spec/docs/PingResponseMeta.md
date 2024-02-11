# PingResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the authenticated customer.  | 
**status_emoji** | **str** | A cute emoji that represents the response status.  | 

## Example

```python
from upbank_spec.models.ping_response_meta import PingResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PingResponseMeta from a JSON string
ping_response_meta_instance = PingResponseMeta.from_json(json)
# print the JSON string representation of the object
print PingResponseMeta.to_json()

# convert the object into a dict
ping_response_meta_dict = ping_response_meta_instance.to_dict()
# create an instance of PingResponseMeta from a dict
ping_response_meta_form_dict = ping_response_meta.from_dict(ping_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


