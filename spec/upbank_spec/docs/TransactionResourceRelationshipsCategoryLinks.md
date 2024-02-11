# TransactionResourceRelationshipsCategoryLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | The link to retrieve or modify linkage between this resources and the related resource(s) in this relationship.  | 
**related** | **str** | The link to retrieve the related resource(s) in this relationship.  | [optional] 

## Example

```python
from upbank_spec.models.transaction_resource_relationships_category_links import TransactionResourceRelationshipsCategoryLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResourceRelationshipsCategoryLinks from a JSON string
transaction_resource_relationships_category_links_instance = TransactionResourceRelationshipsCategoryLinks.from_json(json)
# print the JSON string representation of the object
print TransactionResourceRelationshipsCategoryLinks.to_json()

# convert the object into a dict
transaction_resource_relationships_category_links_dict = transaction_resource_relationships_category_links_instance.to_dict()
# create an instance of TransactionResourceRelationshipsCategoryLinks from a dict
transaction_resource_relationships_category_links_form_dict = transaction_resource_relationships_category_links.from_dict(transaction_resource_relationships_category_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


