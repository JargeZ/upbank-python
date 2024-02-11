# WebhookInputResource

Represents a webhook specified as request input. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**WebhookInputResourceAttributes**](WebhookInputResourceAttributes.md) |  | 

## Example

```python
from upbank_spec.models.webhook_input_resource import WebhookInputResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInputResource from a JSON string
webhook_input_resource_instance = WebhookInputResource.from_json(json)
# print the JSON string representation of the object
print WebhookInputResource.to_json()

# convert the object into a dict
webhook_input_resource_dict = webhook_input_resource_instance.to_dict()
# create an instance of WebhookInputResource from a dict
webhook_input_resource_form_dict = webhook_input_resource.from_dict(webhook_input_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


