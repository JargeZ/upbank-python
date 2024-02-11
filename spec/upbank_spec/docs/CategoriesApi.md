# upbank_spec.CategoriesApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_get**](CategoriesApi.md#categories_get) | **GET** /categories | List categories
[**categories_id_get**](CategoriesApi.md#categories_id_get) | **GET** /categories/{id} | Retrieve category
[**transactions_transaction_id_relationships_category_patch**](CategoriesApi.md#transactions_transaction_id_relationships_category_patch) | **PATCH** /transactions/{transactionId}/relationships/category | Categorize transaction


# **categories_get**
> ListCategoriesResponse categories_get(filter_parent=filter_parent)

List categories

Retrieve a list of all categories and their ancestry. The returned list is not paginated. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.list_categories_response import ListCategoriesResponse
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
    api_instance = upbank_spec.CategoriesApi(api_client)
    filter_parent = 'good-life' # str | The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a `404` response.  (optional)

    try:
        # List categories
        api_response = await api_instance.categories_get(filter_parent=filter_parent)
        print("The response of CategoriesApi->categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_parent** | **str**| The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

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

# **categories_id_get**
> GetCategoryResponse categories_id_get(id)

Retrieve category

Retrieve a specific category by providing its unique identifier. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.get_category_response import GetCategoryResponse
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
    api_instance = upbank_spec.CategoriesApi(api_client)
    id = 'restaurants-and-cafes' # str | The unique identifier for the category. 

    try:
        # Retrieve category
        api_response = await api_instance.categories_id_get(id)
        print("The response of CategoriesApi->categories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the category.  | 

### Return type

[**GetCategoryResponse**](GetCategoryResponse.md)

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

# **transactions_transaction_id_relationships_category_patch**
> transactions_transaction_id_relationships_category_patch(transaction_id, update_transaction_category_request=update_transaction_category_request)

Categorize transaction

Updates the category associated with a transaction. Only transactions for which `isCategorizable` is set to true support this operation. The `id` is taken from the list exposed on `/categories` and cannot be one of the top-level (parent) categories. To de-categorize a transaction, set the entire `data` key to `null`. An HTTP `204` is returned on success. The associated category, along with its request URL is also exposed via the `category` relationship on the transaction resource returned from `/transactions/{id}`. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.update_transaction_category_request import UpdateTransactionCategoryRequest
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
    api_instance = upbank_spec.CategoriesApi(api_client)
    transaction_id = 'a572c7c3-b637-433c-a4ce-c0be5dcb0a5a' # str | The unique identifier for the transaction. 
    update_transaction_category_request = upbank_spec.UpdateTransactionCategoryRequest() # UpdateTransactionCategoryRequest |  (optional)

    try:
        # Categorize transaction
        await api_instance.transactions_transaction_id_relationships_category_patch(transaction_id, update_transaction_category_request=update_transaction_category_request)
    except Exception as e:
        print("Exception when calling CategoriesApi->transactions_transaction_id_relationships_category_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier for the transaction.  | 
 **update_transaction_category_request** | [**UpdateTransactionCategoryRequest**](UpdateTransactionCategoryRequest.md)|  | [optional] 

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

