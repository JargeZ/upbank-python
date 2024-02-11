# TransactionResourceAttributesRoundUp

Details of how this transaction was rounded-up. If no Round Up was applied this field will be `null`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**MoneyObject**](MoneyObject.md) |  | 
**boost_portion** | [**RoundUpObjectBoostPortion**](RoundUpObjectBoostPortion.md) |  | 

## Example

```python
from upbank_spec.models.transaction_resource_attributes_round_up import TransactionResourceAttributesRoundUp

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceAttributesRoundUp from a JSON string
transaction_resource_attributes_round_up_instance = TransactionResourceAttributesRoundUp.from_json(json)
# print the JSON string representation of the object
print TransactionResourceAttributesRoundUp.to_json()

# convert the object into a dict
transaction_resource_attributes_round_up_dict = transaction_resource_attributes_round_up_instance.to_dict()
# create an instance of TransactionResourceAttributesRoundUp from a dict
transaction_resource_attributes_round_up_form_dict = transaction_resource_attributes_round_up.from_dict(transaction_resource_attributes_round_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


