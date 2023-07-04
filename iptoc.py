#!/usr/bin/env python
"""Returns the geolocation of an IP address.

Usage: python iptoc.py <ip address> <result type>.
Valid result types are: city, latlon, country, asn, all

Examples:
    $ python iptoc.py 72.234.1.1 city
    $ ('Hilo', 'Hawaii', '96720')

    $ python iptoc.py 72.234.1.1 latlon
    $ (19.706, -155.0928)

    $ python iptoc.py 72.234.1.1 country
    $ United States

    $ python iptoc.py 72.234.1.1 asn
    $ (36149, 'HAWAIIAN-TELCOM')

    $ python iptoc.py 72.234.1.1 all
    $ ((36149, 'HAWAIIAN-TELCOM'), ('Hilo', 'Hawaii', '96720'), 'United States', (19.706, -155.0928))

Args:
    ip address (str): The IP address to check.
    result type (str): The type of result to return. Valid types are: city, latlon, country, asn, all

"""
import ipaddress
import sys
import geoip2.database  # pip install geoip2
import iptoc_config as cfg

__author__ = "Michael Miranda"
__copyright__ = "Copyright 2023, iptoc"
__credits__ = ["Michael Miranda", "byteBOOST", "MaxMind"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Michael Miranda"
__email__ = "mm.git@byteboost.media"
__status__ = "Prototype"


def get_city(ip_to_check):
    """Returns a tuple of city, state, and zip code."""
    with geoip2.database.Reader(cfg.db_city_path) as reader:
        response = reader.city(ip_to_check)
        return response.city.name, response.subdivisions.most_specific.name, response.postal.code


def get_latlon(ip_to_check):
    """Returns a tuple of latitude and longitude."""
    with geoip2.database.Reader(cfg.db_city_path) as reader:
        response = reader.city(ip_to_check)
        return response.location.latitude, response.location.longitude


def get_country(ip_to_check):
    """Returns the country name."""
    with geoip2.database.Reader(cfg.db_country_path) as reader:
        response = reader.country(ip_to_check)
        return response.country.name


def get_asn(ip_to_check):
    """Returns a tuple of ASN and ASN organization."""
    with geoip2.database.Reader(cfg.db_asn_path) as reader:
        response = reader.asn(ip_to_check)
        return response.autonomous_system_number, response.autonomous_system_organization


def get_all(ip_to_check):
    """Returns a tuple of ASN, ASN organization, city, state, zip code, country, latitude, and longitude."""
    asn_response = get_asn(ip_to_check)
    city_response = get_city(ip_to_check)
    country_response = get_country(ip_to_check)
    latlon_response = get_latlon(ip_to_check)
    return asn_response, city_response, country_response, latlon_response


def __main__(ip_input, result_type):
    """
    Usage: python iptoc.py <ip address> <result type>.
    Valid result types are: city, latlon, country, asn, all
    """
    # how to validate ip_input is an ip address
    # https://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
    try:
        ipaddress.ip_address(ip_input)
    except ValueError:
        print('Invalid IP address')
        return
    if result_type == 'city':
        print(get_city(ip_input))
    elif result_type == 'latlon':
        print(get_latlon(ip_input))
    elif result_type == 'country':
        print(get_country(ip_input))
    elif result_type == 'asn':
        print(get_asn(ip_input))
    elif result_type == 'all':
        print(get_all(ip_input))
    else:
        print('Invalid result type: ' + result_type + '.\n' + __main__.__doc__)
        return


if __name__ == '__main__':
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        result_type = sys.argv[2]
        __main__(ip, result_type)
    else:
        print(__doc__)