# ListAccountsResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | **str** | The link to the previous page in the results. If this value is &#x60;null&#x60; there is no previous page.  | 
**next** | **str** | The link to the next page in the results. If this value is &#x60;null&#x60; there is no next page.  | 

## Example

```python
from upbank_spec.models.list_accounts_response_links import ListAccountsResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccountsResponseLinks from a JSON string
list_accounts_response_links_instance = ListAccountsResponseLinks.from_json(json)
# print the JSON string representation of the object
print ListAccountsResponseLinks.to_json()

# convert the object into a dict
list_accounts_response_links_dict = list_accounts_response_links_instance.to_dict()
# create an instance of ListAccountsResponseLinks from a dict
list_accounts_response_links_form_dict = list_accounts_response_links.from_dict(list_accounts_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


