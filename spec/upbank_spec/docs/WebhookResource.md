# WebhookResource

Provides information about a webhook. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this resource: &#x60;webhooks&#x60; | 
**id** | **str** | The unique identifier for this webhook.  | 
**attributes** | [**WebhookResourceAttributes**](WebhookResourceAttributes.md) |  | 
**relationships** | [**WebhookResourceRelationships**](WebhookResourceRelationships.md) |  | 
**links** | [**AccountResourceLinks**](AccountResourceLinks.md) |  | [optional] 

## Example

```python
from upbank_spec.models.webhook_resource import WebhookResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResource from a JSON string
webhook_resource_instance = WebhookResource.from_json(json)
# print the JSON string representation of the object
print WebhookResource.to_json()

# convert the object into a dict
webhook_resource_dict = webhook_resource_instance.to_dict()
# create an instance of WebhookResource from a dict
webhook_resource_form_dict = webhook_resource.from_dict(webhook_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


