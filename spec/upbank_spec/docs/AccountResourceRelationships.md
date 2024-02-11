# AccountResourceRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**AccountResourceRelationshipsTransactions**](AccountResourceRelationshipsTransactions.md) |  | 

## Example

```python
from upbank_spec.models.account_resource_relationships import AccountResourceRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResourceRelationships from a JSON string
account_resource_relationships_instance = AccountResourceRelationships.from_json(json)
# print the JSON string representation of the object
print AccountResourceRelationships.to_json()

# convert the object into a dict
account_resource_relationships_dict = account_resource_relationships_instance.to_dict()
# create an instance of AccountResourceRelationships from a dict
account_resource_relationships_form_dict = account_resource_relationships.from_dict(account_resource_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


