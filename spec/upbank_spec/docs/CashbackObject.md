# CashbackObject

Provides information about an instant reimbursement in the form of cashback. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A brief description of why this cashback was paid.  | 
**amount** | [**MoneyObject**](MoneyObject.md) |  | 

## Example

```python
from upbank_spec.models.cashback_object import CashbackObject

# TODO update the JSON string below
json = "{}"
# create an instance of CashbackObject from a JSON string
cashback_object_instance = CashbackObject.from_json(json)
# print the JSON string representation of the object
print CashbackObject.to_json()

# convert the object into a dict
cashback_object_dict = cashback_object_instance.to_dict()
# create an instance of CashbackObject from a dict
cashback_object_form_dict = cashback_object.from_dict(cashback_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


