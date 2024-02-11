# ListTransactionsResponse

Successful response to get all transactions. This returns a paginated list of transactions, which can be scrolled by following the `prev` and `next` links if present. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransactionResource]**](TransactionResource.md) | The list of transactions returned in this response.  | 
**links** | [**ListAccountsResponseLinks**](ListAccountsResponseLinks.md) |  | 

## Example

```python
from upbank_spec.models.list_transactions_response import ListTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsResponse from a JSON string
list_transactions_response_instance = ListTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print ListTransactionsResponse.to_json()

# convert the object into a dict
list_transactions_response_dict = list_transactions_response_instance.to_dict()
# create an instance of ListTransactionsResponse from a dict
list_transactions_response_form_dict = list_transactions_response.from_dict(list_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


