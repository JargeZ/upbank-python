# AccountResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name associated with the account in the Up application.  | 
**account_type** | [**AccountTypeEnum**](AccountTypeEnum.md) |  | 
**ownership_type** | [**OwnershipTypeEnum**](OwnershipTypeEnum.md) |  | 
**balance** | [**MoneyObject**](MoneyObject.md) |  | 
**created_at** | **datetime** | The date-time at which this account was first opened.  | 

## Example

```python
from upbank_spec.models.account_resource_attributes import AccountResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResourceAttributes from a JSON string
account_resource_attributes_instance = AccountResourceAttributes.from_json(json)
# print the JSON string representation of the object
print AccountResourceAttributes.to_json()

# convert the object into a dict
account_resource_attributes_dict = account_resource_attributes_instance.to_dict()
# create an instance of AccountResourceAttributes from a dict
account_resource_attributes_form_dict = account_resource_attributes.from_dict(account_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


