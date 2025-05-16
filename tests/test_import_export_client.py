from unittest.mock import Mock

from easyssp_utils.client import ApiClient, ApiResponse
import pytest

from easyssp_import_export.client.import_export_client import ImportExportClient
from easyssp_import_export.models.upload_response import UploadResponse


@pytest.fixture
def mock_api_client():
    return Mock(spec=ApiClient)


@pytest.fixture
def import_export_client(mock_api_client):
    return ImportExportClient(api_client=mock_api_client, username="test_user", password="test-pass", user_agent="easyssp-import-export-client-tests")


def test_export_success(import_export_client, mock_api_client):
    mock_response = b"binary-content-for-ssp-file"
    mock_api_client.call_api.return_value.read.return_value = mock_response
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    _request_timeout = (5.0, 10.0)
    result = import_export_client.export_ssp(ssp_id="valid_id", _request_timeout=_request_timeout).data

    assert isinstance(result, bytes)
    assert result == b"binary-content-for-ssp-file"
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    mock_api_client.call_api.assert_called_once()


def test_export_with_invalid_id(import_export_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("Invalid SSP model ID")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception, match="Invalid SSP model ID"):
        import_export_client.export_ssp(ssp_id="invalid_id")


def test_import_ssd_success(import_export_client, mock_api_client):
    mock_rest_response = UploadResponse(id="test_ssd_id", url="http://example.com/ssd")
    mock_api_client.call_api.return_value.read.return_value = b'{"id": "test_ssd_id", "url": "http://example.com/ssd"}'
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    _request_timeout = (5.0, 10.0)
    result = import_export_client.import_ssd(filename="test_file.ssd", body=b"ssd data", _request_timeout=_request_timeout).data

    assert result.id == "test_ssd_id"
    assert result.url == "http://example.com/ssd"
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    mock_api_client.call_api.assert_called_once()


def test_import_ssd_with_missing_file(import_export_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("File not provided")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception, match="File not provided"):
        import_export_client.import_ssd(filename=None, body=None)


def test_import_ssp_success(import_export_client, mock_api_client):
    mock_rest_response = UploadResponse(id="test_id", url="http://example.com")
    mock_api_client.call_api.return_value.read.return_value = b'{"id": "test_id", "url": "http://example.com"}'
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    _request_timeout = (5.0, 10.0)
    result = import_export_client.import_ssp(filename="test_file.ssp", body=b"test data",
                                             _request_timeout=_request_timeout).data

    assert result.id == "test_id"
    assert result.url == "http://example.com"
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    mock_api_client.call_api.assert_called_once()


def test_import_ssp_with_missing_file(import_export_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("File not provided")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception, match="File not provided"):
        import_export_client.import_ssp(filename=None, body=None)
