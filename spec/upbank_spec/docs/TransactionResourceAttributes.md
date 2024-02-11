# TransactionResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TransactionStatusEnum**](TransactionStatusEnum.md) |  | 
**raw_text** | **str** | The original, unprocessed text of the transaction. This is often not a perfect indicator of the actual merchant, but it is useful for reconciliation purposes in some cases.  | 
**description** | **str** | A short description for this transaction. Usually the merchant name for purchases.  | 
**message** | **str** | Attached message for this transaction, such as a payment message, or a transfer note.  | 
**is_categorizable** | **bool** | Boolean flag set to true on transactions that support the use of categories.  | 
**hold_info** | [**TransactionResourceAttributesHoldInfo**](TransactionResourceAttributesHoldInfo.md) |  | 
**round_up** | [**TransactionResourceAttributesRoundUp**](TransactionResourceAttributesRoundUp.md) |  | 
**cashback** | [**TransactionResourceAttributesCashback**](TransactionResourceAttributesCashback.md) |  | 
**amount** | [**MoneyObject**](MoneyObject.md) |  | 
**foreign_amount** | [**TransactionResourceAttributesForeignAmount**](TransactionResourceAttributesForeignAmount.md) |  | 
**settled_at** | **datetime** | The date-time at which this transaction settled. This field will be &#x60;null&#x60; for transactions that are currently in the &#x60;HELD&#x60; status.  | 
**created_at** | **datetime** | The date-time at which this transaction was first encountered.  | 

## Example

```python
from upbank_spec.models.transaction_resource_attributes import TransactionResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceAttributes from a JSON string
transaction_resource_attributes_instance = TransactionResourceAttributes.from_json(json)
# print the JSON string representation of the object
print TransactionResourceAttributes.to_json()

# convert the object into a dict
transaction_resource_attributes_dict = transaction_resource_attributes_instance.to_dict()
# create an instance of TransactionResourceAttributes from a dict
transaction_resource_attributes_form_dict = transaction_resource_attributes.from_dict(transaction_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


