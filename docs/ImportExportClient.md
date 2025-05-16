# [Import-Export Client](../easyssp_import_export/client/import_export_client.py)

All URIs are relative to *https://www.easy-ssp.com*

| Method                                             | HTTP request                            | Description        |
|----------------------------------------------------|-----------------------------------------|--------------------|
| [**import_ssp**](ImportExportClient.md#import_ssp) | **POST** /integration/api/v1/ssp        | Imports a SSP-file |
| [**export**](ImportExportClient.md#export_ssp)     | **GET** /integration/api/v1/ssp/{sspId} | Exports a SSP-file |
| [**import_ssd**](ImportExportClient.md#import_ssd) | **POST** /integration/api/v1/ssd        | Imports a SSD-file |

# **import_ssp**

Imports an SSP-file

Loads a .ssp-file. When successful, the API returns the ID of the created SSP-model as well as a URL that can be used to
open the SSP-Model in the easySSP WebApp.

### Parameters

| Name         | Type          | Description                                                                            | Notes      |
|--------------|---------------|----------------------------------------------------------------------------------------|------------|
| **filename** | **str**       | The name of the SSP-file. Will use this as a file name when downloading the SSP-model. | [optional] |
| **body**     | **bytearray** |                                                                                        | [optional] |

### Return data type

[**UploadResponse**](UploadResponse.md)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: application/x-ssp-package
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Response headers |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The SSP-file has been successfully processed and stored. Returns an object containing the id of the created SSP-Model as well as the URL to open the SSP-Model in the easySSP WebApp.                                                                                                                                                                                                                                                                                                                                                            | -                |
| **400**     | - The file exceeds the allowed size (currently 500MB) - The SSP-file is unreadable (invalid zip-file)<br/> - The SSP-file is invalid (violating the SSP container structure rules)<br/> - A file inside the SSP-container is unreadable (e.g. an .ssd-file)<br/> - A file inside the SSP-container is invalid (e.g. a file is deviating from the SSP Standard XML schema definition)<br/> - A file inside the SSP-container exceeds the allowed size (currently 500MB)<br/> - The sum of resource files exceeds the allowed size (currently 1GB) | -                |
| **500**     | A different error occurred while reading or storing the SSP-file. This most often indicates a validation issue with the data base, which in turn might indicate an invalid SSP-file. Please contact us, if this issue persists after retry and the validity of the file is checked.                                                                                                                                                                                                                                                              | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | -                |
| **403**     | The user lacks the permissions to access the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | -                |

[[Back to README]](../README.md)

# **export_ssp**

Exports an SSP-file

Downloads the SSP-model corresponding to the SSP-model id as an .ssp-file.

### Parameters

| Name             | Type    | Description                     | Notes |
|------------------|---------|---------------------------------|-------|
| **ssp_model_id** | **str** | ID of the SSP-model to download |       |

### Return type

**bytearray**

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-ssp-package, application/json

### HTTP response details

| Status code | Description                                                                                                     | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The SSP-file has been successfully created and downloaded.                                                      | -                |
| **400**     | Unable to create the zip structure of the SSP-file. Unable to parse an SSP associated file to an XML-structure. | -                |
| **404**     | There is no SSP-model associated with the given id or the id is invalid.                                        | -                |
| **401**     | The request lacks a valid access token                                                                          | -                |
| **403**     | The user lacks the permissions to access the resource or the current user has no access to the model.           | -                |

[[Back to README]](../README.md)

# **import_ssd**

Imports an SSD file

Loads a .ssd-file and adds it to a new SSP-model. When successful, the API returns the ID of the created SSP-model as
well as a URL that can be used to open the SSP-Model in the easySSP WebApp.

### Parameters

| Name         | Type          | Description                                                                                               | Notes      |
|--------------|---------------|-----------------------------------------------------------------------------------------------------------|------------|
| **filename** | **str**       | The name of the SSD-file. Will use this as template for the SSP-file name when downloading the SSP-model. | [optional] |
| **body**     | **bytearray** |                                                                                                           | [optional] |

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: application/x-ssp-definition
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                                                                                                         | Response headers |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The SSD-file has been successfully processed and stored. Returns an object containing the id of the created SSP-Model as well as the URL to open the SSP-Model in the easySSP WebApp.                                                                                               | -                |
| **400**     | - The file exceeds the allowed size (currently 500MB)<br/> - The SSD-file is invalid                                                                                                                                                                                                | -                |
| **500**     | A different error occurred while reading or storing the SSD-file. This most often indicates a validation issue with the data base, which in turn might indicate an invalid SSD-file. Please contact us, if this issue persists after retry and the validity of the file is checked. | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                                                                                             | -                |
| **403**     | The user lacks the permissions to access the resource.                                                                                                                                                                                                                              | -                |

[[Back to README]](../README.md)

