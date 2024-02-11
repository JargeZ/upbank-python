# TransactionResourceRelationshipsTransferAccount

If this transaction is a transfer between accounts, this relationship will contain the account the transaction went to/came from. The `amount` field can be used to determine the direction of the transfer. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionResourceRelationshipsTransferAccountData**](TransactionResourceRelationshipsTransferAccountData.md) |  | 
**links** | [**AccountResourceRelationshipsTransactionsLinks**](AccountResourceRelationshipsTransactionsLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.transaction_resource_relationships_transfer_account import TransactionResourceRelationshipsTransferAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationshipsTransferAccount from a JSON string
transaction_resource_relationships_transfer_account_instance = TransactionResourceRelationshipsTransferAccount.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationshipsTransferAccount.to_json()

# convert the object into a dict
transaction_resource_relationships_transfer_account_dict = transaction_resource_relationships_transfer_account_instance.to_dict()
# create an instance of TransactionResourceRelationshipsTransferAccount from a dict
transaction_resource_relationships_transfer_account_form_dict = transaction_resource_relationships_transfer_account.from_dict(transaction_resource_relationships_transfer_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


