# coding: utf-8

"""
    Kadaster - BRK-Bevragen API

    D.m.v. deze toepassing worden meerdere, korte bevragingen op de Basis Registratie Kadaster beschikbaar gesteld. Deze toepassing betreft het verstrekken van Kadastrale Onroerende Zaak informatie.   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class BeslagLinks(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        '_self': 'HalLink',
        'beslagleggers': 'list[HalLink]'
    }

    attribute_map = {
        '_self': 'self',
        'beslagleggers': 'beslagleggers'
    }

    def __init__(self, _self=None, beslagleggers=None, local_vars_configuration=None):  # noqa: E501
        """BeslagLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__self = None
        self._beslagleggers = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if beslagleggers is not None:
            self.beslagleggers = beslagleggers

    @property
    def _self(self):
        """Gets the _self of this BeslagLinks.  # noqa: E501


        :return: The _self of this BeslagLinks.  # noqa: E501
        :rtype: HalLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this BeslagLinks.


        :param _self: The _self of this BeslagLinks.  # noqa: E501
        :type: HalLink
        """

        self.__self = _self

    @property
    def beslagleggers(self):
        """Gets the beslagleggers of this BeslagLinks.  # noqa: E501


        :return: The beslagleggers of this BeslagLinks.  # noqa: E501
        :rtype: list[HalLink]
        """
        return self._beslagleggers

    @beslagleggers.setter
    def beslagleggers(self, beslagleggers):
        """Sets the beslagleggers of this BeslagLinks.


        :param beslagleggers: The beslagleggers of this BeslagLinks.  # noqa: E501
        :type: list[HalLink]
        """

        self._beslagleggers = beslagleggers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BeslagLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BeslagLinks):
            return True

        return self.to_dict() != other.to_dict()
