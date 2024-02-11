# TransactionResourceAttributesCashback

If all or part of this transaction was instantly reimbursed in the form of cashback, details of the reimbursement. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A brief description of why this cashback was paid.  | 
**amount** | [**MoneyObject**](MoneyObject.md) |  | 

## Example

```python
from upbank_spec.models.transaction_resource_attributes_cashback import TransactionResourceAttributesCashback

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceAttributesCashback from a JSON string
transaction_resource_attributes_cashback_instance = TransactionResourceAttributesCashback.from_json(json)
# print the JSON string representation of the object
print TransactionResourceAttributesCashback.to_json()

# convert the object into a dict
transaction_resource_attributes_cashback_dict = transaction_resource_attributes_cashback_instance.to_dict()
# create an instance of TransactionResourceAttributesCashback from a dict
transaction_resource_attributes_cashback_form_dict = transaction_resource_attributes_cashback.from_dict(transaction_resource_attributes_cashback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


