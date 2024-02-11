# HoldInfoObjectForeignAmount

The foreign currency amount of this transaction while in the `HELD` status. This field will be `null` for domestic transactions. The amount was converted to the AUD amount reflected in the `amount` field. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The ISO 4217 currency code.  | 
**value** | **str** | The amount of money, formatted as a string in the relevant currency. For example, for an Australian dollar value of $10.56, this field will be &#x60;\&quot;10.56\&quot;&#x60;. The currency symbol is not included in the string.  | 
**value_in_base_units** | **int** | The amount of money in the smallest denomination for the currency, as a 64-bit integer.  For example, for an Australian dollar value of $10.56, this field will be &#x60;1056&#x60;.  | 

## Example

```python
from upbank_spec.models.hold_info_object_foreign_amount import HoldInfoObjectForeignAmount

# TODO update the JSON string below
json = "{}"
# create an instance of HoldInfoObjectForeignAmount from a JSON string
hold_info_object_foreign_amount_instance = HoldInfoObjectForeignAmount.from_json(json)
# print the JSON string representation of the object
print HoldInfoObjectForeignAmount.to_json()

# convert the object into a dict
hold_info_object_foreign_amount_dict = hold_info_object_foreign_amount_instance.to_dict()
# create an instance of HoldInfoObjectForeignAmount from a dict
hold_info_object_foreign_amount_form_dict = hold_info_object_foreign_amount.from_dict(hold_info_object_foreign_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


