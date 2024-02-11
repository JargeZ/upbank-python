# upbank_spec.WebhooksApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_get**](WebhooksApi.md#webhooks_get) | **GET** /webhooks | List webhooks
[**webhooks_id_delete**](WebhooksApi.md#webhooks_id_delete) | **DELETE** /webhooks/{id} | Delete webhook
[**webhooks_id_get**](WebhooksApi.md#webhooks_id_get) | **GET** /webhooks/{id} | Retrieve webhook
[**webhooks_post**](WebhooksApi.md#webhooks_post) | **POST** /webhooks | Create webhook
[**webhooks_webhook_id_logs_get**](WebhooksApi.md#webhooks_webhook_id_logs_get) | **GET** /webhooks/{webhookId}/logs | List webhook logs
[**webhooks_webhook_id_ping_post**](WebhooksApi.md#webhooks_webhook_id_ping_post) | **POST** /webhooks/{webhookId}/ping | Ping webhook


# **webhooks_get**
> ListWebhooksResponse webhooks_get(page_size=page_size)

List webhooks

Retrieve a list of configured webhooks. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. Results are ordered oldest first to newest last. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.list_webhooks_response import ListWebhooksResponse
from upbank_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.up.com.au/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = upbank_spec.Configuration(
    host = "https://api.up.com.au/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = upbank_spec.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with upbank_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upbank_spec.WebhooksApi(api_client)
    page_size = 30 # int | The number of records to return in each page.  (optional)

    try:
        # List webhooks
        api_response = await api_instance.webhooks_get(page_size=page_size)
        print("The response of WebhooksApi->webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_delete**
> webhooks_id_delete(id)

Delete webhook

Delete a specific webhook by providing its unique identifier. Once deleted, webhook events will no longer be sent to the configured URL. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.up.com.au/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = upbank_spec.Configuration(
    host = "https://api.up.com.au/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = upbank_spec.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with upbank_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upbank_spec.WebhooksApi(api_client)
    id = 'a940825b-80b6-4798-b378-c6284259b4c5' # str | The unique identifier for the webhook. 

    try:
        # Delete webhook
        await api_instance.webhooks_id_delete(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the webhook.  | 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_get**
> GetWebhookResponse webhooks_id_get(id)

Retrieve webhook

Retrieve a specific webhook by providing its unique identifier. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.get_webhook_response import GetWebhookResponse
from upbank_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.up.com.au/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = upbank_spec.Configuration(
    host = "https://api.up.com.au/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = upbank_spec.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with upbank_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upbank_spec.WebhooksApi(api_client)
    id = 'c8283a72-24b0-4fd8-9b13-fccccab371e5' # str | The unique identifier for the webhook. 

    try:
        # Retrieve webhook
        api_response = await api_instance.webhooks_id_get(id)
        print("The response of WebhooksApi->webhooks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the webhook.  | 

### Return type

[**GetWebhookResponse**](GetWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_post**
> CreateWebhookResponse webhooks_post(create_webhook_request=create_webhook_request)

Create webhook

Create a new webhook with a given URL. The URL will receive webhook events as JSON-encoded `POST` requests. The URL must respond with a HTTP `200` status on success.  There is currently a limit of 10 webhooks at any given time. Once this limit is reached, existing webhooks will need to be deleted before new webhooks can be created.  Event delivery is retried with exponential backoff if the URL is unreachable or it does not respond with a `200` status. The response includes a `secretKey` attribute, which is used to sign requests sent to the webhook URL. It will not be returned from any other endpoints within the Up API. If the `secretKey` is lost, simply create a new webhook with the same URL, capture its `secretKey` and then delete the original webhook. See [Handling webhook events](#callback_post_webhookURL) for details on how to process webhook events.  It is probably a good idea to test the webhook by [sending it a `PING` event](#post_webhooks_webhookId_ping) after creating it. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.create_webhook_request import CreateWebhookRequest
from upbank_spec.models.create_webhook_response import CreateWebhookResponse
from upbank_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.up.com.au/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = upbank_spec.Configuration(
    host = "https://api.up.com.au/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = upbank_spec.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with upbank_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upbank_spec.WebhooksApi(api_client)
    create_webhook_request = upbank_spec.CreateWebhookRequest() # CreateWebhookRequest |  (optional)

    try:
        # Create webhook
        api_response = await api_instance.webhooks_post(create_webhook_request=create_webhook_request)
        print("The response of WebhooksApi->webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | [optional] 

### Return type

[**CreateWebhookResponse**](CreateWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_webhook_id_logs_get**
> ListWebhookDeliveryLogsResponse webhooks_webhook_id_logs_get(webhook_id, page_size=page_size)

List webhook logs

Retrieve a list of delivery logs for a webhook by providing its unique identifier. This is useful for analysis and debugging purposes. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. Results are ordered newest first to oldest last. Logs may be automatically purged after a period of time. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.list_webhook_delivery_logs_response import ListWebhookDeliveryLogsResponse
from upbank_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.up.com.au/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = upbank_spec.Configuration(
    host = "https://api.up.com.au/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = upbank_spec.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with upbank_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upbank_spec.WebhooksApi(api_client)
    webhook_id = '7104f5df-4993-495f-9d29-2b4d062c03a9' # str | The unique identifier for the webhook. 
    page_size = 30 # int | The number of records to return in each page.  (optional)

    try:
        # List webhook logs
        api_response = await api_instance.webhooks_webhook_id_logs_get(webhook_id, page_size=page_size)
        print("The response of WebhooksApi->webhooks_webhook_id_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_webhook_id_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique identifier for the webhook.  | 
 **page_size** | **int**| The number of records to return in each page.  | [optional] 

### Return type

[**ListWebhookDeliveryLogsResponse**](ListWebhookDeliveryLogsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_webhook_id_ping_post**
> WebhookEventCallback webhooks_webhook_id_ping_post(webhook_id)

Ping webhook

Send a `PING` event to a webhook by providing its unique identifier. This is useful for testing and debugging purposes. The event is delivered asynchronously and its data is returned in the response to this request. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.webhook_event_callback import WebhookEventCallback
from upbank_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.up.com.au/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = upbank_spec.Configuration(
    host = "https://api.up.com.au/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer_auth
configuration = upbank_spec.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with upbank_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upbank_spec.WebhooksApi(api_client)
    webhook_id = '830e127d-fb89-4400-92bb-f3f48289dcba' # str | The unique identifier for the webhook. 

    try:
        # Ping webhook
        api_response = await api_instance.webhooks_webhook_id_ping_post(webhook_id)
        print("The response of WebhooksApi->webhooks_webhook_id_ping_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_webhook_id_ping_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique identifier for the webhook.  | 

### Return type

[**WebhookEventCallback**](WebhookEventCallback.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

