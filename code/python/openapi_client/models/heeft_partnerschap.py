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


class HeeftPartnerschap(object):
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
        'datum_ontbinding': 'DatumOnvolledig',
        'datum_sluiting': 'DatumOnvolledig',
        'naam': 'Naam'
    }

    attribute_map = {
        'datum_ontbinding': 'datumOntbinding',
        'datum_sluiting': 'datumSluiting',
        'naam': 'naam'
    }

    def __init__(self, datum_ontbinding=None, datum_sluiting=None, naam=None, local_vars_configuration=None):  # noqa: E501
        """HeeftPartnerschap - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._datum_ontbinding = None
        self._datum_sluiting = None
        self._naam = None
        self.discriminator = None

        if datum_ontbinding is not None:
            self.datum_ontbinding = datum_ontbinding
        if datum_sluiting is not None:
            self.datum_sluiting = datum_sluiting
        if naam is not None:
            self.naam = naam

    @property
    def datum_ontbinding(self):
        """Gets the datum_ontbinding of this HeeftPartnerschap.  # noqa: E501


        :return: The datum_ontbinding of this HeeftPartnerschap.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_ontbinding

    @datum_ontbinding.setter
    def datum_ontbinding(self, datum_ontbinding):
        """Sets the datum_ontbinding of this HeeftPartnerschap.


        :param datum_ontbinding: The datum_ontbinding of this HeeftPartnerschap.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_ontbinding = datum_ontbinding

    @property
    def datum_sluiting(self):
        """Gets the datum_sluiting of this HeeftPartnerschap.  # noqa: E501


        :return: The datum_sluiting of this HeeftPartnerschap.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_sluiting

    @datum_sluiting.setter
    def datum_sluiting(self, datum_sluiting):
        """Sets the datum_sluiting of this HeeftPartnerschap.


        :param datum_sluiting: The datum_sluiting of this HeeftPartnerschap.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_sluiting = datum_sluiting

    @property
    def naam(self):
        """Gets the naam of this HeeftPartnerschap.  # noqa: E501


        :return: The naam of this HeeftPartnerschap.  # noqa: E501
        :rtype: Naam
        """
        return self._naam

    @naam.setter
    def naam(self, naam):
        """Sets the naam of this HeeftPartnerschap.


        :param naam: The naam of this HeeftPartnerschap.  # noqa: E501
        :type: Naam
        """

        self._naam = naam

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
        if not isinstance(other, HeeftPartnerschap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HeeftPartnerschap):
            return True

        return self.to_dict() != other.to_dict()
