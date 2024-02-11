# UpdateTransactionCategoryRequestData

The category to set on the transaction. Set this entire key to `null` de-categorize a transaction. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;categories&#x60; | 
**id** | **str** | The unique identifier of the category, as returned by the &#x60;/categories&#x60; endpoint.  | 

## Example

```python
from upbank_spec.models.update_transaction_category_request_data import UpdateTransactionCategoryRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionCategoryRequestData from a JSON string
update_transaction_category_request_data_instance = UpdateTransactionCategoryRequestData.from_json(json)
# print the JSON string representation of the object
print UpdateTransactionCategoryRequestData.to_json()

# convert the object into a dict
update_transaction_category_request_data_dict = update_transaction_category_request_data_instance.to_dict()
# create an instance of UpdateTransactionCategoryRequestData from a dict
update_transaction_category_request_data_form_dict = update_transaction_category_request_data.from_dict(update_transaction_category_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


