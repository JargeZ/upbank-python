# TransactionResourceRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**TransactionResourceRelationshipsAccount**](TransactionResourceRelationshipsAccount.md) |  | 
**transfer_account** | [**TransactionResourceRelationshipsTransferAccount**](TransactionResourceRelationshipsTransferAccount.md) |  | 
**category** | [**TransactionResourceRelationshipsCategory**](TransactionResourceRelationshipsCategory.md) |  | 
**parent_category** | [**CategoryResourceRelationshipsParent**](CategoryResourceRelationshipsParent.md) |  | 
**tags** | [**TransactionResourceRelationshipsTags**](TransactionResourceRelationshipsTags.md) |  | 

## Example

```python
from upbank_spec.models.transaction_resource_relationships import TransactionResourceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationships from a JSON string
transaction_resource_relationships_instance = TransactionResourceRelationships.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationships.to_json()

# convert the object into a dict
transaction_resource_relationships_dict = transaction_resource_relationships_instance.to_dict()
# create an instance of TransactionResourceRelationships from a dict
transaction_resource_relationships_form_dict = transaction_resource_relationships.from_dict(transaction_resource_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


