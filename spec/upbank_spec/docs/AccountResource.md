# AccountResource

Provides information about an Up bank account. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;accounts&#x60; | 
**id** | **str** | The unique identifier for this account.  | 
**attributes** | [**AccountResourceAttributes**](AccountResourceAttributes.md) |  | 
**relationships** | [**AccountResourceRelationships**](AccountResourceRelationships.md) |  | 
**links** | [**AccountResourceLinks**](AccountResourceLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.account_resource import AccountResource

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResource from a JSON string
account_resource_instance = AccountResource.from_json(json)
# print the JSON string representation of the object
print AccountResource.to_json()

# convert the object into a dict
account_resource_dict = account_resource_instance.to_dict()
# create an instance of AccountResource from a dict
account_resource_form_dict = account_resource.from_dict(account_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


