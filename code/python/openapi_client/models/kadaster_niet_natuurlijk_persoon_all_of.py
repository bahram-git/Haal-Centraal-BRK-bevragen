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


class KadasterNietNatuurlijkPersoonAllOf(object):
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
        'statutaire_naam': 'str',
        'statutaire_zetel': 'str',
        'rechtsvorm': 'Waardelijst',
        'kvk_nummer': 'str',
        'rsin': 'str'
    }

    attribute_map = {
        'statutaire_naam': 'statutaireNaam',
        'statutaire_zetel': 'statutaireZetel',
        'rechtsvorm': 'rechtsvorm',
        'kvk_nummer': 'kvkNummer',
        'rsin': 'rsin'
    }

    def __init__(self, statutaire_naam=None, statutaire_zetel=None, rechtsvorm=None, kvk_nummer=None, rsin=None, local_vars_configuration=None):  # noqa: E501
        """KadasterNietNatuurlijkPersoonAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._statutaire_naam = None
        self._statutaire_zetel = None
        self._rechtsvorm = None
        self._kvk_nummer = None
        self._rsin = None
        self.discriminator = None

        if statutaire_naam is not None:
            self.statutaire_naam = statutaire_naam
        if statutaire_zetel is not None:
            self.statutaire_zetel = statutaire_zetel
        if rechtsvorm is not None:
            self.rechtsvorm = rechtsvorm
        if kvk_nummer is not None:
            self.kvk_nummer = kvk_nummer
        if rsin is not None:
            self.rsin = rsin

    @property
    def statutaire_naam(self):
        """Gets the statutaire_naam of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501


        :return: The statutaire_naam of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :rtype: str
        """
        return self._statutaire_naam

    @statutaire_naam.setter
    def statutaire_naam(self, statutaire_naam):
        """Sets the statutaire_naam of this KadasterNietNatuurlijkPersoonAllOf.


        :param statutaire_naam: The statutaire_naam of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :type: str
        """

        self._statutaire_naam = statutaire_naam

    @property
    def statutaire_zetel(self):
        """Gets the statutaire_zetel of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501


        :return: The statutaire_zetel of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :rtype: str
        """
        return self._statutaire_zetel

    @statutaire_zetel.setter
    def statutaire_zetel(self, statutaire_zetel):
        """Sets the statutaire_zetel of this KadasterNietNatuurlijkPersoonAllOf.


        :param statutaire_zetel: The statutaire_zetel of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :type: str
        """

        self._statutaire_zetel = statutaire_zetel

    @property
    def rechtsvorm(self):
        """Gets the rechtsvorm of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501


        :return: The rechtsvorm of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :rtype: Waardelijst
        """
        return self._rechtsvorm

    @rechtsvorm.setter
    def rechtsvorm(self, rechtsvorm):
        """Sets the rechtsvorm of this KadasterNietNatuurlijkPersoonAllOf.


        :param rechtsvorm: The rechtsvorm of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :type: Waardelijst
        """

        self._rechtsvorm = rechtsvorm

    @property
    def kvk_nummer(self):
        """Gets the kvk_nummer of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501


        :return: The kvk_nummer of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :rtype: str
        """
        return self._kvk_nummer

    @kvk_nummer.setter
    def kvk_nummer(self, kvk_nummer):
        """Sets the kvk_nummer of this KadasterNietNatuurlijkPersoonAllOf.


        :param kvk_nummer: The kvk_nummer of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :type: str
        """

        self._kvk_nummer = kvk_nummer

    @property
    def rsin(self):
        """Gets the rsin of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501


        :return: The rsin of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rsin

    @rsin.setter
    def rsin(self, rsin):
        """Sets the rsin of this KadasterNietNatuurlijkPersoonAllOf.


        :param rsin: The rsin of this KadasterNietNatuurlijkPersoonAllOf.  # noqa: E501
        :type: str
        """

        self._rsin = rsin

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
        if not isinstance(other, KadasterNietNatuurlijkPersoonAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KadasterNietNatuurlijkPersoonAllOf):
            return True

        return self.to_dict() != other.to_dict()
