# MoneyObject

Provides information about a value of money. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The ISO 4217 currency code.  | 
**value** | **str** | The amount of money, formatted as a string in the relevant currency. For example, for an Australian dollar value of $10.56, this field will be &#x60;\&quot;10.56\&quot;&#x60;. The currency symbol is not included in the string.  | 
**value_in_base_units** | **int** | The amount of money in the smallest denomination for the currency, as a 64-bit integer.  For example, for an Australian dollar value of $10.56, this field will be &#x60;1056&#x60;.  | 

## Example

```python
from upbank_spec.models.money_object import MoneyObject

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyObject from a JSON string
money_object_instance = MoneyObject.from_json(json)
# print the JSON string representation of the object
print MoneyObject.to_json()

# convert the object into a dict
money_object_dict = money_object_instance.to_dict()
# create an instance of MoneyObject from a dict
money_object_form_dict = money_object.from_dict(money_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


