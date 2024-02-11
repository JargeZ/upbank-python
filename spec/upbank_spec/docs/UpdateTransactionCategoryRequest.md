# UpdateTransactionCategoryRequest

Request to update the category associated with a transaction. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateTransactionCategoryRequestData**](UpdateTransactionCategoryRequestData.md) |  | 

## Example

```python
from upbank_spec.models.update_transaction_category_request import UpdateTransactionCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionCategoryRequest from a JSON string
update_transaction_category_request_instance = UpdateTransactionCategoryRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTransactionCategoryRequest.to_json()

# convert the object into a dict
update_transaction_category_request_dict = update_transaction_category_request_instance.to_dict()
# create an instance of UpdateTransactionCategoryRequest from a dict
update_transaction_category_request_form_dict = update_transaction_category_request.from_dict(update_transaction_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


