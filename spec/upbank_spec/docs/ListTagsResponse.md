# ListTagsResponse

Successful response to get all tags. This returns a paginated list of tags, which can be scrolled by following the `prev` and `next` links if present. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TagResource]**](TagResource.md) | The list of tags returned in this response.  | 
**links** | [**ListAccountsResponseLinks**](ListAccountsResponseLinks.md) |  | 

## Example

```python
from upbank_spec.models.list_tags_response import ListTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTagsResponse from a JSON string
list_tags_response_instance = ListTagsResponse.from_json(json)
# print the JSON string representation of the object
print ListTagsResponse.to_json()

# convert the object into a dict
list_tags_response_dict = list_tags_response_instance.to_dict()
# create an instance of ListTagsResponse from a dict
list_tags_response_form_dict = list_tags_response.from_dict(list_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


