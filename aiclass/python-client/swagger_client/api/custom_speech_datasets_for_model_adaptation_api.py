# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CustomSpeechDatasetsForModelAdaptationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_dataset(self, id, **kwargs):  # noqa: E501
        """Deletes the specified dataset.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dataset(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the dataset. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_dataset_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dataset_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_dataset_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes the specified dataset.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dataset_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the dataset. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/datasets/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset(self, id, **kwargs):  # noqa: E501
        """Gets the dataset identified by the given ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the dataset. (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_dataset_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets the dataset identified by the given ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the dataset. (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/datasets/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dataset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets(self, **kwargs):  # noqa: E501
        """Gets a list of datasets for the authenticated subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Dataset]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of datasets for the authenticated subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Dataset]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Dataset]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_supported_locales_for_datasets(self, **kwargs):  # noqa: E501
        """Gets a list of supported locales for data imports.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_locales_for_datasets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IReadOnlyDictionary2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_supported_locales_for_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_supported_locales_for_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_supported_locales_for_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of supported locales for data imports.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_locales_for_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IReadOnlyDictionary2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_supported_locales_for_datasets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/datasets/locales', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IReadOnlyDictionary2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dataset(self, id, dataset_update, **kwargs):  # noqa: E501
        """Updates the mutable details of the dataset identified by its ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dataset(id, dataset_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the dataset. (required)
        :param DatasetUpdate dataset_update: The updated values for the dataset. (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dataset_with_http_info(id, dataset_update, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dataset_with_http_info(id, dataset_update, **kwargs)  # noqa: E501
            return data

    def update_dataset_with_http_info(self, id, dataset_update, **kwargs):  # noqa: E501
        """Updates the mutable details of the dataset identified by its ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dataset_with_http_info(id, dataset_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the dataset. (required)
        :param DatasetUpdate dataset_update: The updated values for the dataset. (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'dataset_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_dataset`")  # noqa: E501
        # verify the required parameter 'dataset_update' is set
        if ('dataset_update' not in params or
                params['dataset_update'] is None):
            raise ValueError("Missing the required parameter `dataset_update` when calling `update_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dataset_update' in params:
            body_params = params['dataset_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/datasets/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dataset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_dataset(self, **kwargs):  # noqa: E501
        """Uploads data and creates a new dataset.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_dataset(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The name of this data import (always add this string for any import).
        :param str description: Optional description of this data import.
        :param str locale: The locale of this data import (always add this string for any import).
        :param str data_import_kind: The kind of the data import (always add this string for any import).
        :param str properties: Optional properties of this data import (json serialized object with key/values, where all values must be strings)
        :param file audiodata: A zip file containing the audio data (this and the audio archive file for acoustic data imports).
        :param file transcriptions: A text file containing the transcriptions for the audio data (this and the transcriptions file for acoustic data imports).
        :param file languagedata: A text file containing the language or pronunciation data (only this file for language data imports).
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_dataset_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.upload_dataset_with_http_info(**kwargs)  # noqa: E501
            return data

    def upload_dataset_with_http_info(self, **kwargs):  # noqa: E501
        """Uploads data and creates a new dataset.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_dataset_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The name of this data import (always add this string for any import).
        :param str description: Optional description of this data import.
        :param str locale: The locale of this data import (always add this string for any import).
        :param str data_import_kind: The kind of the data import (always add this string for any import).
        :param str properties: Optional properties of this data import (json serialized object with key/values, where all values must be strings)
        :param file audiodata: A zip file containing the audio data (this and the audio archive file for acoustic data imports).
        :param file transcriptions: A text file containing the transcriptions for the audio data (this and the transcriptions file for acoustic data imports).
        :param file languagedata: A text file containing the language or pronunciation data (only this file for language data imports).
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'description', 'locale', 'data_import_kind', 'properties', 'audiodata', 'transcriptions', 'languagedata']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_dataset" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'locale' in params:
            form_params.append(('locale', params['locale']))  # noqa: E501
        if 'data_import_kind' in params:
            form_params.append(('dataImportKind', params['data_import_kind']))  # noqa: E501
        if 'properties' in params:
            form_params.append(('properties', params['properties']))  # noqa: E501
        if 'audiodata' in params:
            local_var_files['audiodata'] = params['audiodata']  # noqa: E501
        if 'transcriptions' in params:
            local_var_files['transcriptions'] = params['transcriptions']  # noqa: E501
        if 'languagedata' in params:
            local_var_files['languagedata'] = params['languagedata']  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key', 'token']  # noqa: E501

        return self.api_client.call_api(
            '/api/speechtotext/v2.0/datasets/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
