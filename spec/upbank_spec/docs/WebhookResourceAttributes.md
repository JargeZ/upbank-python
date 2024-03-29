# WebhookResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL that this webhook is configured to &#x60;POST&#x60; events to.  | 
**description** | **str** | An optional description that was provided at the time the webhook was created.  | 
**secret_key** | **str** | A shared secret key used to sign all webhook events sent to the configured webhook URL. This field is returned only once, upon the initial creation of the webhook. If lost, create a new webhook and delete this webhook.  The webhook URL receives a request with a &#x60;X-Up-Authenticity-Signature&#x60; header, which is the SHA-256 HMAC of the entire raw request body signed using this &#x60;secretKey&#x60;. It is advised to compute and check this signature to verify the authenticity of requests sent to the webhook URL. See [Handling webhook events](#callback_post_webhookURL) for full details.  | [optional] 
**created_at** | **datetime** | The date-time at which this webhook was created.  | 

## Example

```python
from upbank_spec.models.webhook_resource_attributes import WebhookResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResourceAttributes from a JSON string
webhook_resource_attributes_instance = WebhookResourceAttributes.from_json(json)
# print the JSON string representation of the object
print WebhookResourceAttributes.to_json()

# convert the object into a dict
webhook_resource_attributes_dict = webhook_resource_attributes_instance.to_dict()
# create an instance of WebhookResourceAttributes from a dict
webhook_resource_attributes_form_dict = webhook_resource_attributes.from_dict(webhook_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


