# UpdateTransactionTagsRequest

Request to add or remove tags associated with a transaction. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TagInputResourceIdentifier]**](TagInputResourceIdentifier.md) | The tags to add to or remove from the transaction.  | 

## Example

```python
from upbank_spec.models.update_transaction_tags_request import UpdateTransactionTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionTagsRequest from a JSON string
update_transaction_tags_request_instance = UpdateTransactionTagsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTransactionTagsRequest.to_json()

# convert the object into a dict
update_transaction_tags_request_dict = update_transaction_tags_request_instance.to_dict()
# create an instance of UpdateTransactionTagsRequest from a dict
update_transaction_tags_request_form_dict = update_transaction_tags_request.from_dict(update_transaction_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


