# RoundUpObject

Provides information about how a Round Up was applied, such as whether or not a boost was included in the Round Up. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**MoneyObject**](MoneyObject.md) |  | 
**boost_portion** | [**RoundUpObjectBoostPortion**](RoundUpObjectBoostPortion.md) |  | 

## Example

```python
from upbank_spec.models.round_up_object import RoundUpObject

# TODO update the JSON string below
json = "{}"
# create an instance of RoundUpObject from a JSON string
round_up_object_instance = RoundUpObject.from_json(json)
# print the JSON string representation of the object
print RoundUpObject.to_json()

# convert the object into a dict
round_up_object_dict = round_up_object_instance.to_dict()
# create an instance of RoundUpObject from a dict
round_up_object_form_dict = round_up_object.from_dict(round_up_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


