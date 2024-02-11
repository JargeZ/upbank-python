# TransactionResourceAttributesHoldInfo

If this transaction is currently in the `HELD` status, or was ever in the `HELD` status, the `amount` and `foreignAmount` of the transaction while `HELD`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**MoneyObject**](MoneyObject.md) |  | 
**foreign_amount** | [**HoldInfoObjectForeignAmount**](HoldInfoObjectForeignAmount.md) |  | 

## Example

```python
from upbank_spec.models.transaction_resource_attributes_hold_info import TransactionResourceAttributesHoldInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceAttributesHoldInfo from a JSON string
transaction_resource_attributes_hold_info_instance = TransactionResourceAttributesHoldInfo.from_json(json)
# print the JSON string representation of the object
print TransactionResourceAttributesHoldInfo.to_json()

# convert the object into a dict
transaction_resource_attributes_hold_info_dict = transaction_resource_attributes_hold_info_instance.to_dict()
# create an instance of TransactionResourceAttributesHoldInfo from a dict
transaction_resource_attributes_hold_info_form_dict = transaction_resource_attributes_hold_info.from_dict(transaction_resource_attributes_hold_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


