# TransactionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;transactions&#x60; | 
**id** | **str** | The unique identifier for this transaction.  | 
**attributes** | [**TransactionResourceAttributes**](TransactionResourceAttributes.md) |  | 
**relationships** | [**TransactionResourceRelationships**](TransactionResourceRelationships.md) |  | 
**links** | [**AccountResourceLinks**](AccountResourceLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.transaction_resource import TransactionResource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResource from a JSON string
transaction_resource_instance = TransactionResource.from_json(json)
# print the JSON string representation of the object
print TransactionResource.to_json()

# convert the object into a dict
transaction_resource_dict = transaction_resource_instance.to_dict()
# create an instance of TransactionResource from a dict
transaction_resource_form_dict = transaction_resource.from_dict(transaction_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


