# UploadResponse


## Properties

| Name    | Type    | Description                                                                        | Notes      |
|---------|---------|------------------------------------------------------------------------------------|------------|
| **id**  | **str** | The id of the created SSP-Model. This id can be used for downloading the SSP-File. | [optional] |
| **url** | **str** | The URL to access the SSP-Model in the easySSP WebApp.                             | [optional] |

## Example

```python
from easyssp_import_export.models.upload_response import UploadResponse

upload_response = UploadResponse(id='c1146953-296f-4ef6-9eb6-5cdf26d4b416',
                                 url='https://easy-ssp.com/app/?extId=80KdCCw9Vci06ko9QPe6Wg%3D%3D%3A8DFeRNvN9sYmqJoq1qlHAVajsEPGjDh9rfHOlGEe8dO87O3wg30Cj%2BH6vhtze5H4')
# print the JSON string representation of the object
print(upload_response.to_json())

# convert the object into a dict
upload_response_dict = upload_response.to_dict()
# create an instance of UploadResponse from a dict
upload_response_from_dict = UploadResponse.from_dict(upload_response_dict)
```
[[Back to README]](../README.md)


