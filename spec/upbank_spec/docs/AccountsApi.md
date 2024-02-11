# upbank_spec.AccountsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_get**](AccountsApi.md#accounts_get) | **GET** /accounts | List accounts
[**accounts_id_get**](AccountsApi.md#accounts_id_get) | **GET** /accounts/{id} | Retrieve account


# **accounts_get**
> ListAccountsResponse accounts_get(page_size=page_size, filter_account_type=filter_account_type, filter_ownership_type=filter_ownership_type)

List accounts

Retrieve a paginated list of all accounts for the currently authenticated user. The returned list is paginated and can be scrolled by following the `prev` and `next` links where present. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.account_type_enum import AccountTypeEnum
from upbank_spec.models.list_accounts_response import ListAccountsResponse
from upbank_spec.models.ownership_type_enum import OwnershipTypeEnum
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
    api_instance = upbank_spec.AccountsApi(api_client)
    page_size = 30 # int | The number of records to return in each page.  (optional)
    filter_account_type = upbank_spec.AccountTypeEnum() # AccountTypeEnum | The type of account for which to return records. This can be used to filter Savers from spending accounts.  (optional)
    filter_ownership_type = upbank_spec.OwnershipTypeEnum() # OwnershipTypeEnum | The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts.  (optional)

    try:
        # List accounts
        api_response = await api_instance.accounts_get(page_size=page_size, filter_account_type=filter_account_type, filter_ownership_type=filter_ownership_type)
        print("The response of AccountsApi->accounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 
 **filter_account_type** | [**AccountTypeEnum**](.md)| The type of account for which to return records. This can be used to filter Savers from spending accounts.  | [optional] 
 **filter_ownership_type** | [**OwnershipTypeEnum**](.md)| The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts.  | [optional] 

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

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

# **accounts_id_get**
> GetAccountResponse accounts_id_get(id)

Retrieve account

Retrieve a specific account by providing its unique identifier. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.get_account_response import GetAccountResponse
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
    api_instance = upbank_spec.AccountsApi(api_client)
    id = '92b41408-6b7b-4fca-982b-3fb1fdd77220' # str | The unique identifier for the account. 

    try:
        # Retrieve account
        api_response = await api_instance.accounts_id_get(id)
        print("The response of AccountsApi->accounts_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->accounts_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the account.  | 

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

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

