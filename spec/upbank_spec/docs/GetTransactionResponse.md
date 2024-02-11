# GetTransactionResponse

Successful response to get a single transaction. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionResource**](TransactionResource.md) |  | 

## Example

```python
from upbank_spec.models.get_transaction_response import GetTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionResponse from a JSON string
get_transaction_response_instance = GetTransactionResponse.from_json(json)
# print the JSON string representation of the object
print GetTransactionResponse.to_json()

# convert the object into a dict
get_transaction_response_dict = get_transaction_response_instance.to_dict()
# create an instance of GetTransactionResponse from a dict
get_transaction_response_form_dict = get_transaction_response.from_dict(get_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


