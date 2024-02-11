# ListWebhooksResponse

Successful response to get all webhooks. This returns a paginated list of webhooks, which can be scrolled by following the `prev` and `next` links if present. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookResource]**](WebhookResource.md) | The list of webhooks returned in this response.  | 
**links** | [**ListAccountsResponseLinks**](ListAccountsResponseLinks.md) |  | 

## Example

```python
from upbank_spec.models.list_webhooks_response import ListWebhooksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhooksResponse from a JSON string
list_webhooks_response_instance = ListWebhooksResponse.from_json(json)
# print the JSON string representation of the object
print ListWebhooksResponse.to_json()

# convert the object into a dict
list_webhooks_response_dict = list_webhooks_response_instance.to_dict()
# create an instance of ListWebhooksResponse from a dict
list_webhooks_response_form_dict = list_webhooks_response.from_dict(list_webhooks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


