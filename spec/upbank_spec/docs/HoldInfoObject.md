# HoldInfoObject

Provides information about the amount at which a transaction was in the `HELD` status. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**MoneyObject**](MoneyObject.md) |  | 
**foreign_amount** | [**HoldInfoObjectForeignAmount**](HoldInfoObjectForeignAmount.md) |  | 

## Example

```python
from upbank_spec.models.hold_info_object import HoldInfoObject

# TODO update the JSON string below
json = "{}"
# create an instance of HoldInfoObject from a JSON string
hold_info_object_instance = HoldInfoObject.from_json(json)
# print the JSON string representation of the object
print HoldInfoObject.to_json()

# convert the object into a dict
hold_info_object_dict = hold_info_object_instance.to_dict()
# create an instance of HoldInfoObject from a dict
hold_info_object_form_dict = hold_info_object.from_dict(hold_info_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


