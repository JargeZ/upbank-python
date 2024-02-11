# ListWebhookDeliveryLogsResponse

Successful response to get all delivery logs for a webhook. This returns a paginated list of delivery logs, which can be scrolled by following the `next` and `prev` links if present. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookDeliveryLogResource]**](WebhookDeliveryLogResource.md) | The list of delivery logs returned in this response.  | 
**links** | [**ListAccountsResponseLinks**](ListAccountsResponseLinks.md) |  | 

## Example

```python
from upbank_spec.models.list_webhook_delivery_logs_response import ListWebhookDeliveryLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookDeliveryLogsResponse from a JSON string
list_webhook_delivery_logs_response_instance = ListWebhookDeliveryLogsResponse.from_json(json)
# print the JSON string representation of the object
print ListWebhookDeliveryLogsResponse.to_json()

# convert the object into a dict
list_webhook_delivery_logs_response_dict = list_webhook_delivery_logs_response_instance.to_dict()
# create an instance of ListWebhookDeliveryLogsResponse from a dict
list_webhook_delivery_logs_response_form_dict = list_webhook_delivery_logs_response.from_dict(list_webhook_delivery_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


