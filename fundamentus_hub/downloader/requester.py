#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester.py
#  Version: 0.0.5
#
#  Summary: Python Fundamentus
#           Python Fundamentus is a Python API that allows you to quickly
#           access the main fundamental indicators of the main stocks
#           in the Brazilian market.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ------------------------------------------------------------------------------
"""HTTP Requester - This module is responsible for making HTTP requests."""

from typing import Dict

import requests

from fundamentus_hub.downloader.interfaces.requester import RequesterInterface


# pylint: disable=too-few-public-methods
class SGSRequester(RequesterInterface):
    """Represents a complete HTTP request."""

    def __init__(self) -> None:
        """Initialize the class."""

        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

    @staticmethod
    def __send_http_request(prepared_request: requests.PreparedRequest) -> requests.Response:
        """Send the HTTP request.

        Arguments:
            prepared_request {requests.PreparedRequest} -- Prepared request.

        Returns:
            requests.Response -- Response of the request.

        Raises:
            HTTPError: If the request fails.
        """

        with requests.Session() as session:
            response = session.send(prepared_request)

            response.raise_for_status()

            return response

    def make_request(self, url: str) -> Dict:
        """Make request to the url and return the response.

        Returns:
            Dict -- Response of the request.

        Raises:
            RequestException: If the request fails.
        """

        try:
            request = requests.Request(method="GET",
                                       url=url,
                                       headers=self.__headers)

            prepared_request = request.prepare()
            response = self.__send_http_request(prepared_request)

            return response.json()

        except requests.exceptions.RequestException as error:
            raise error
