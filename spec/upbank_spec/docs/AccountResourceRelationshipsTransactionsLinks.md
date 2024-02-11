# AccountResourceRelationshipsTransactionsLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related** | **str** | The link to retrieve the related resource(s) in this relationship.  | 

## Example

```python
from upbank_spec.models.account_resource_relationships_transactions_links import AccountResourceRelationshipsTransactionsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResourceRelationshipsTransactionsLinks from a JSON string
account_resource_relationships_transactions_links_instance = AccountResourceRelationshipsTransactionsLinks.from_json(json)
# print the JSON string representation of the object
print AccountResourceRelationshipsTransactionsLinks.to_json()

# convert the object into a dict
account_resource_relationships_transactions_links_dict = account_resource_relationships_transactions_links_instance.to_dict()
# create an instance of AccountResourceRelationshipsTransactionsLinks from a dict
account_resource_relationships_transactions_links_form_dict = account_resource_relationships_transactions_links.from_dict(account_resource_relationships_transactions_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


