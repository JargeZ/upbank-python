# WebhookInputResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL that this webhook should post events to. This must be a valid HTTP or HTTPS URL that does not exceed 300 characters in length.  | 
**description** | **str** | An optional description for this webhook, up to 64 characters in length.  | [optional] 

## Example

```python
from upbank_spec.models.webhook_input_resource_attributes import WebhookInputResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInputResourceAttributes from a JSON string
webhook_input_resource_attributes_instance = WebhookInputResourceAttributes.from_json(json)
# print the JSON string representation of the object
print WebhookInputResourceAttributes.to_json()

# convert the object into a dict
webhook_input_resource_attributes_dict = webhook_input_resource_attributes_instance.to_dict()
# create an instance of WebhookInputResourceAttributes from a dict
webhook_input_resource_attributes_form_dict = webhook_input_resource_attributes.from_dict(webhook_input_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


