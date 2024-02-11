# upbank_spec.TransactionsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_transactions_get**](TransactionsApi.md#accounts_account_id_transactions_get) | **GET** /accounts/{accountId}/transactions | List transactions by account
[**transactions_get**](TransactionsApi.md#transactions_get) | **GET** /transactions | List transactions
[**transactions_id_get**](TransactionsApi.md#transactions_id_get) | **GET** /transactions/{id} | Retrieve transaction


# **accounts_account_id_transactions_get**
> ListTransactionsResponse accounts_account_id_transactions_get(account_id, page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)

List transactions by account

Retrieve a list of all transactions for a specific account. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. To narrow the results to a specific date range pass one or both of `filter[since]` and `filter[until]` in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.list_transactions_response import ListTransactionsResponse
from upbank_spec.models.transaction_status_enum import TransactionStatusEnum
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
    api_instance = upbank_spec.TransactionsApi(api_client)
    account_id = 'b5544658-4bbd-4eb1-8f63-a9909e0f564b' # str | The unique identifier for the account. 
    page_size = 30 # int | The number of records to return in each page.  (optional)
    filter_status = upbank_spec.TransactionStatusEnum() # TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`.  (optional)
    filter_since = '2020-01-01T01:02:03+10:00' # datetime | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
    filter_until = '2020-02-01T01:02:03+10:00' # datetime | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
    filter_category = 'good-life' # str | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response.  (optional)
    filter_tag = 'Holiday' # str | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  (optional)

    try:
        # List transactions by account
        api_response = await api_instance.accounts_account_id_transactions_get(account_id, page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)
        print("The response of TransactionsApi->accounts_account_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->accounts_account_id_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The unique identifier for the account.  | 
 **page_size** | **int**| The number of records to return in each page.  | [optional] 
 **filter_status** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] 
 **filter_since** | **datetime**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_until** | **datetime**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_category** | **str**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 
 **filter_tag** | **str**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

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

# **transactions_get**
> ListTransactionsResponse transactions_get(page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)

List transactions

Retrieve a list of all transactions across all accounts for the currently authenticated user. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. To narrow the results to a specific date range pass one or both of `filter[since]` and `filter[until]` in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.list_transactions_response import ListTransactionsResponse
from upbank_spec.models.transaction_status_enum import TransactionStatusEnum
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
    api_instance = upbank_spec.TransactionsApi(api_client)
    page_size = 30 # int | The number of records to return in each page.  (optional)
    filter_status = upbank_spec.TransactionStatusEnum() # TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`.  (optional)
    filter_since = '2020-01-01T01:02:03+10:00' # datetime | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
    filter_until = '2020-02-01T01:02:03+10:00' # datetime | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
    filter_category = 'good-life' # str | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response.  (optional)
    filter_tag = 'Holiday' # str | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  (optional)

    try:
        # List transactions
        api_response = await api_instance.transactions_get(page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)
        print("The response of TransactionsApi->transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 
 **filter_status** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] 
 **filter_since** | **datetime**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_until** | **datetime**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_category** | **str**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 
 **filter_tag** | **str**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

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

# **transactions_id_get**
> GetTransactionResponse transactions_id_get(id)

Retrieve transaction

Retrieve a specific transaction by providing its unique identifier. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.get_transaction_response import GetTransactionResponse
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
    api_instance = upbank_spec.TransactionsApi(api_client)
    id = '7a9d19f9-106c-4e29-8591-52fc5d8f09c5' # str | The unique identifier for the transaction. 

    try:
        # Retrieve transaction
        api_response = await api_instance.transactions_id_get(id)
        print("The response of TransactionsApi->transactions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the transaction.  | 

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

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

