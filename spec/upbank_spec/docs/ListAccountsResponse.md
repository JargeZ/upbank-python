# ListAccountsResponse

Successful response to get all accounts. This returns a paginated list of accounts, which can be scrolled by following the `prev` and `next` links if present. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccountResource]**](AccountResource.md) | The list of accounts returned in this response.  | 
**links** | [**ListAccountsResponseLinks**](ListAccountsResponseLinks.md) |  | 

## Example

```python
from upbank_spec.models.list_accounts_response import ListAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccountsResponse from a JSON string
list_accounts_response_instance = ListAccountsResponse.from_json(json)
# print the JSON string representation of the object
print ListAccountsResponse.to_json()

# convert the object into a dict
list_accounts_response_dict = list_accounts_response_instance.to_dict()
# create an instance of ListAccountsResponse from a dict
list_accounts_response_form_dict = list_accounts_response.from_dict(list_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


