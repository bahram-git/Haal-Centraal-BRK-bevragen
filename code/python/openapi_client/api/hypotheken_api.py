# coding: utf-8

"""
    Kadaster - BRK-Bevragen API

    D.m.v. deze toepassing worden meerdere, korte bevragingen op de Basis Registratie Kadaster beschikbaar gesteld. Deze toepassing betreft het verstrekken van Kadastrale Onroerende Zaak informatie.   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class HypothekenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_hypotheek(self, kadastraalonroerendezaakidentificatie, hypotheekidentificatie, **kwargs):  # noqa: E501
        """get_hypotheek  # noqa: E501

        Het raadplegen van een hypotheek die rust op een kadastraal onroerende zaak met bijbehorende hypotheekhouder(s). Een hypotheekhouder vestigt als geldverstrekker een recht van hypotheek als zekerheid voor de lening.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hypotheek(kadastraalonroerendezaakidentificatie, hypotheekidentificatie, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str kadastraalonroerendezaakidentificatie: De unieke identificatie van een kadastraal onroerende zaak.  (required)
        :param str hypotheekidentificatie: De unieke identificatie van de hypotheek.  (required)
        :param str fields: Hiermee kun je de inhoud van de resource naar behoefte aanpassen door een door komma's gescheiden lijst van property namen op te geven. Bij opgave van niet-bestaande properties wordt een 400 Bad Request teruggegeven. Wanneer de fields parameter niet is opgegeven, worden alle properties met een waarde teruggegeven. Zie [functionele specificaties](https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature)
        :param str accept_crs: Gewenste CRS van de coördinaten in de response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: HypotheekHal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_hypotheek_with_http_info(kadastraalonroerendezaakidentificatie, hypotheekidentificatie, **kwargs)  # noqa: E501

    def get_hypotheek_with_http_info(self, kadastraalonroerendezaakidentificatie, hypotheekidentificatie, **kwargs):  # noqa: E501
        """get_hypotheek  # noqa: E501

        Het raadplegen van een hypotheek die rust op een kadastraal onroerende zaak met bijbehorende hypotheekhouder(s). Een hypotheekhouder vestigt als geldverstrekker een recht van hypotheek als zekerheid voor de lening.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hypotheek_with_http_info(kadastraalonroerendezaakidentificatie, hypotheekidentificatie, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str kadastraalonroerendezaakidentificatie: De unieke identificatie van een kadastraal onroerende zaak.  (required)
        :param str hypotheekidentificatie: De unieke identificatie van de hypotheek.  (required)
        :param str fields: Hiermee kun je de inhoud van de resource naar behoefte aanpassen door een door komma's gescheiden lijst van property namen op te geven. Bij opgave van niet-bestaande properties wordt een 400 Bad Request teruggegeven. Wanneer de fields parameter niet is opgegeven, worden alle properties met een waarde teruggegeven. Zie [functionele specificaties](https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature)
        :param str accept_crs: Gewenste CRS van de coördinaten in de response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(HypotheekHal, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'kadastraalonroerendezaakidentificatie',
            'hypotheekidentificatie',
            'fields',
            'accept_crs'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hypotheek" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'kadastraalonroerendezaakidentificatie' is set
        if self.api_client.client_side_validation and ('kadastraalonroerendezaakidentificatie' not in local_var_params or  # noqa: E501
                                                        local_var_params['kadastraalonroerendezaakidentificatie'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `kadastraalonroerendezaakidentificatie` when calling `get_hypotheek`")  # noqa: E501
        # verify the required parameter 'hypotheekidentificatie' is set
        if self.api_client.client_side_validation and ('hypotheekidentificatie' not in local_var_params or  # noqa: E501
                                                        local_var_params['hypotheekidentificatie'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hypotheekidentificatie` when calling `get_hypotheek`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'kadastraalonroerendezaakidentificatie' in local_var_params:
            path_params['kadastraalonroerendezaakidentificatie'] = local_var_params['kadastraalonroerendezaakidentificatie']  # noqa: E501
        if 'hypotheekidentificatie' in local_var_params:
            path_params['hypotheekidentificatie'] = local_var_params['hypotheekidentificatie']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501

        header_params = {}
        if 'accept_crs' in local_var_params:
            header_params['Accept-Crs'] = local_var_params['accept_crs']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/hal+json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/kadastraalonroerendezaken/{kadastraalonroerendezaakidentificatie}/hypotheken/{hypotheekidentificatie}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HypotheekHal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hypotheken_kadastraal_onroerende_zaak(self, kadastraalonroerendezaakidentificatie, **kwargs):  # noqa: E501
        """get_hypotheken_kadastraal_onroerende_zaak  # noqa: E501

        Het raadplegen van hypotheken die rusten op een kadastraal onroerende zaak met bijbehorende hypotheekhouder(s). Een hypotheekhouder vestigt als geldverstrekker een recht van hypotheek als zekerheid voor de lening.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hypotheken_kadastraal_onroerende_zaak(kadastraalonroerendezaakidentificatie, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str kadastraalonroerendezaakidentificatie: De unieke identificatie van een kadastraal onroerende zaak.  (required)
        :param str fields: Hiermee kun je de inhoud van de resource naar behoefte aanpassen door een door komma's gescheiden lijst van property namen op te geven. Bij opgave van niet-bestaande properties wordt een 400 Bad Request teruggegeven. Wanneer de fields parameter niet is opgegeven, worden alle properties met een waarde teruggegeven. Zie [functionele specificaties](https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature)
        :param str accept_crs: Gewenste CRS van de coördinaten in de response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: HypotheekHalCollectie
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_hypotheken_kadastraal_onroerende_zaak_with_http_info(kadastraalonroerendezaakidentificatie, **kwargs)  # noqa: E501

    def get_hypotheken_kadastraal_onroerende_zaak_with_http_info(self, kadastraalonroerendezaakidentificatie, **kwargs):  # noqa: E501
        """get_hypotheken_kadastraal_onroerende_zaak  # noqa: E501

        Het raadplegen van hypotheken die rusten op een kadastraal onroerende zaak met bijbehorende hypotheekhouder(s). Een hypotheekhouder vestigt als geldverstrekker een recht van hypotheek als zekerheid voor de lening.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hypotheken_kadastraal_onroerende_zaak_with_http_info(kadastraalonroerendezaakidentificatie, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str kadastraalonroerendezaakidentificatie: De unieke identificatie van een kadastraal onroerende zaak.  (required)
        :param str fields: Hiermee kun je de inhoud van de resource naar behoefte aanpassen door een door komma's gescheiden lijst van property namen op te geven. Bij opgave van niet-bestaande properties wordt een 400 Bad Request teruggegeven. Wanneer de fields parameter niet is opgegeven, worden alle properties met een waarde teruggegeven. Zie [functionele specificaties](https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature)
        :param str accept_crs: Gewenste CRS van de coördinaten in de response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(HypotheekHalCollectie, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'kadastraalonroerendezaakidentificatie',
            'fields',
            'accept_crs'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hypotheken_kadastraal_onroerende_zaak" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'kadastraalonroerendezaakidentificatie' is set
        if self.api_client.client_side_validation and ('kadastraalonroerendezaakidentificatie' not in local_var_params or  # noqa: E501
                                                        local_var_params['kadastraalonroerendezaakidentificatie'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `kadastraalonroerendezaakidentificatie` when calling `get_hypotheken_kadastraal_onroerende_zaak`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'kadastraalonroerendezaakidentificatie' in local_var_params:
            path_params['kadastraalonroerendezaakidentificatie'] = local_var_params['kadastraalonroerendezaakidentificatie']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501

        header_params = {}
        if 'accept_crs' in local_var_params:
            header_params['Accept-Crs'] = local_var_params['accept_crs']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/hal+json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/kadastraalonroerendezaken/{kadastraalonroerendezaakidentificatie}/hypotheken', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HypotheekHalCollectie',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
