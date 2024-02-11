# TransactionResourceRelationshipsTransferAccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;accounts&#x60; | 
**id** | **str** | The unique identifier of the resource within its type.  | 

## Example

```python
from upbank_spec.models.transaction_resource_relationships_transfer_account_data import TransactionResourceRelationshipsTransferAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationshipsTransferAccountData from a JSON string
transaction_resource_relationships_transfer_account_data_instance = TransactionResourceRelationshipsTransferAccountData.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationshipsTransferAccountData.to_json()

# convert the object into a dict
transaction_resource_relationships_transfer_account_data_dict = transaction_resource_relationships_transfer_account_data_instance.to_dict()
# create an instance of TransactionResourceRelationshipsTransferAccountData from a dict
transaction_resource_relationships_transfer_account_data_form_dict = transaction_resource_relationships_transfer_account_data.from_dict(transaction_resource_relationships_transfer_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


