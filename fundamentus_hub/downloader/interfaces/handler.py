#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: requester.py
#  Version: 0.0.1
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

"""Interfaces for the handler module."""

from abc import ABC, abstractmethod
from typing import Dict

from pandas import DataFrame


class StockFecherInterface(ABC):
    """Represents a stock fetcher."""

    @abstractmethod
    def get_all_tickets(self) -> list:
        """Get all tickets from pyfundamentus API."""

        raise NotImplementedError("You should implement this method.")

    @abstractmethod
    def get_data(self, ticket: str) -> list:
        """Get data from pyfundamentus API."""

        raise NotImplementedError("You should implement this method.")


class DataProcessorInterface(ABC):
    """Represents a data processor."""

    @abstractmethod
    def process_information(self, ticket_data) -> Dict:
        """Process the information extracted from pyfundamentus API"""

        raise NotImplementedError("You should implement this method.")

    @abstractmethod
    def extract_information(self, data_section: Dict) -> Dict:
        """Extract the information from the data section"""

        raise NotImplementedError("You should implement this method.")


class DataPersisterInterface(ABC):
    """Data Persister class"""

    @staticmethod
    def persist_fundamentus_data(data_frame: DataFrame,
                                 file_name: str,
                                 file_format: str) -> None:
        """Represents a data persister."""

        raise NotImplementedError("You should implement this method.")
