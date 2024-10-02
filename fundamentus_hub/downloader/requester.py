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

import requests
import streamlit as st

from fundamentus_hub.downloader.interfaces.requester import RequesterInterface


# pylint: disable=too-few-public-methods
class SGSRequester(RequesterInterface):
    """Represents a complete HTTP request."""

    def __init__(self, url: str) -> None:
        """Initialize the class.

        :param url: str: URL to make the request.
        :param params: dict: Parameters to make the request.
        """

        self.__url = url
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

    @staticmethod
    def __send_http_request(prepared_request: requests.PreparedRequest) -> requests.Response:
        """Send the HTTP request.

        :param prepared_request: requests.PreparedRequest: Prepared request.
        :return: requests.Response: Response of the request.
        :raises HTTPError: If the request fails.
        """

        with requests.Session() as session:
            response = session.send(prepared_request)

            response.raise_for_status()

            return response

    def make_request(self):
        """Make request to the url and return the response.

        :return: dict: Response of the request.
        :raises RequestException: If the request fails.
        """

        try:
            request = requests.Request(method="GET",
                                       url=self.__url,
                                       headers=self.__headers)

            prepared_request = request.prepare()
            response = self.__send_http_request(prepared_request)

            return response.json()

        except requests.exceptions.RequestException as error:
            raise error
