# upbank_spec.TagsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags | List tags
[**transactions_transaction_id_relationships_tags_delete**](TagsApi.md#transactions_transaction_id_relationships_tags_delete) | **DELETE** /transactions/{transactionId}/relationships/tags | Remove tags from transaction
[**transactions_transaction_id_relationships_tags_post**](TagsApi.md#transactions_transaction_id_relationships_tags_post) | **POST** /transactions/{transactionId}/relationships/tags | Add tags to transaction


# **tags_get**
> ListTagsResponse tags_get(page_size=page_size, page_after=page_after)

List tags

Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. Results are ordered lexicographically. The `transactions` relationship for each tag exposes a link to get the transactions with the given tag. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.list_tags_response import ListTagsResponse
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
    api_instance = upbank_spec.TagsApi(api_client)
    page_size = 50 # int | The number of records to return in each page.  (optional)
    page_after = 'WyIyMDI0LTAyLTA5VDAxOjA3OjU5LjYwMzk0OTAwMFoiLCJiNDBlMWYzMS00ZGFjLTQ0MzItYjIwMy04MjFjNmRhZTA1M2MiXQ==' # str | The token to retrieve the next page in the results.  (optional)

    try:
        # List tags
        api_response = await api_instance.tags_get(page_size=page_size, page_after=page_after)
        print("The response of TagsApi->tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 
 **page_after** | **str**| The token to retrieve the next page in the results.  | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

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

# **transactions_transaction_id_relationships_tags_delete**
> transactions_transaction_id_relationships_tags_delete(transaction_id, update_transaction_tags_request=update_transaction_tags_request)

Remove tags from transaction

Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP `204` is returned on success. The associated tags, along with this request URL, are also exposed via the `tags` relationship on the transaction resource returned from `/transactions/{id}`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.update_transaction_tags_request import UpdateTransactionTagsRequest
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
    api_instance = upbank_spec.TagsApi(api_client)
    transaction_id = 'c3feb4ba-829c-4482-b882-1b9bd23da82d' # str | The unique identifier for the transaction. 
    update_transaction_tags_request = upbank_spec.UpdateTransactionTagsRequest() # UpdateTransactionTagsRequest |  (optional)

    try:
        # Remove tags from transaction
        await api_instance.transactions_transaction_id_relationships_tags_delete(transaction_id, update_transaction_tags_request=update_transaction_tags_request)
    except Exception as e:
        print("Exception when calling TagsApi->transactions_transaction_id_relationships_tags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier for the transaction.  | 
 **update_transaction_tags_request** | [**UpdateTransactionTagsRequest**](UpdateTransactionTagsRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_id_relationships_tags_post**
> transactions_transaction_id_relationships_tags_post(transaction_id, update_transaction_tags_request=update_transaction_tags_request)

Add tags to transaction

Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP `204` is returned on success. The associated tags, along with this request URL, are also exposed via the `tags` relationship on the transaction resource returned from `/transactions/{id}`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.update_transaction_tags_request import UpdateTransactionTagsRequest
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
    api_instance = upbank_spec.TagsApi(api_client)
    transaction_id = 'acde4631-db56-49a6-aea3-4e2311ef1d6a' # str | The unique identifier for the transaction. 
    update_transaction_tags_request = upbank_spec.UpdateTransactionTagsRequest() # UpdateTransactionTagsRequest |  (optional)

    try:
        # Add tags to transaction
        await api_instance.transactions_transaction_id_relationships_tags_post(transaction_id, update_transaction_tags_request=update_transaction_tags_request)
    except Exception as e:
        print("Exception when calling TagsApi->transactions_transaction_id_relationships_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier for the transaction.  | 
 **update_transaction_tags_request** | [**UpdateTransactionTagsRequest**](UpdateTransactionTagsRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

