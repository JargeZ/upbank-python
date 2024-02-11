# RoundUpObjectBoostPortion

The portion of the Round Up `amount` owing to boosted Round Ups, represented as a negative value. If no boost was added to the Round Up this field will be `null`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The ISO 4217 currency code.  | 
**value** | **str** | The amount of money, formatted as a string in the relevant currency. For example, for an Australian dollar value of $10.56, this field will be &#x60;\&quot;10.56\&quot;&#x60;. The currency symbol is not included in the string.  | 
**value_in_base_units** | **int** | The amount of money in the smallest denomination for the currency, as a 64-bit integer.  For example, for an Australian dollar value of $10.56, this field will be &#x60;1056&#x60;.  | 

## Example

```python
from upbank_spec.models.round_up_object_boost_portion import RoundUpObjectBoostPortion

# TODO update the JSON string below
json = "{}"
# create an instance of RoundUpObjectBoostPortion from a JSON string
round_up_object_boost_portion_instance = RoundUpObjectBoostPortion.from_json(json)
# print the JSON string representation of the object
print RoundUpObjectBoostPortion.to_json()

# convert the object into a dict
round_up_object_boost_portion_dict = round_up_object_boost_portion_instance.to_dict()
# create an instance of RoundUpObjectBoostPortion from a dict
round_up_object_boost_portion_form_dict = round_up_object_boost_portion.from_dict(round_up_object_boost_portion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


