# TransactionResourceRelationshipsAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionResourceRelationshipsAccountData**](TransactionResourceRelationshipsAccountData.md) |  | 
**links** | [**AccountResourceRelationshipsTransactionsLinks**](AccountResourceRelationshipsTransactionsLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.transaction_resource_relationships_account import TransactionResourceRelationshipsAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationshipsAccount from a JSON string
transaction_resource_relationships_account_instance = TransactionResourceRelationshipsAccount.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationshipsAccount.to_json()

# convert the object into a dict
transaction_resource_relationships_account_dict = transaction_resource_relationships_account_instance.to_dict()
# create an instance of TransactionResourceRelationshipsAccount from a dict
transaction_resource_relationships_account_form_dict = transaction_resource_relationships_account.from_dict(transaction_resource_relationships_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


