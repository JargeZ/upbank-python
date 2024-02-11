# upbank_spec.UtilityEndpointsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**util_ping_get**](UtilityEndpointsApi.md#util_ping_get) | **GET** /util/ping | Ping


# **util_ping_get**
> PingResponse util_ping_get()

Ping

Make a basic ping request to the API. This is useful to verify that authentication is functioning correctly. On authentication success an HTTP `200` status is returned. On failure an HTTP `401` error response is returned. 

### Example

* Bearer Authentication (bearer_auth):

```python
import time
import os
import upbank_spec
from upbank_spec.models.ping_response import PingResponse
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
    api_instance = upbank_spec.UtilityEndpointsApi(api_client)

    try:
        # Ping
        api_response = await api_instance.util_ping_get()
        print("The response of UtilityEndpointsApi->util_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilityEndpointsApi->util_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

