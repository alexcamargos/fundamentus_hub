#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: handler.py
#  Version: 0.0.1
#  Summary: Fundamentus Hub
#           Este projeto cria um dashboard utilizando a API pyfundamentus para
#           exibir os principais indicadores financeiros das empresas listadas
#           na B3, facilitando a análise fundamentalista através de visualizações
#           claras e acessíveis para investidores e analistas.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

import concurrent.futures
import datetime
import pickle

import pandas as pd
from fundamentus import Pipeline
from fundamentus.exceptions.extract_exception import ExtractException
from fundamentus.exceptions.http_request_error import HttpRequestError
from loguru import logger

from fundamentus_hub.downloader.interfaces.handler import (DataPersisterInterface,
                                                           DataProcessorInterface,
                                                           StockFetcherInterface)
from fundamentus_hub.utilities.configuration import DownloadHandler as DownloadCfg


class StockFetcher(StockFetcherInterface):
    """Stock Fetcher class"""

    def get_all_tickets(self) -> list:
        """Get all tickets from pyfundamentus API"""

        # Get all companies from pyfundamentus API.
        response = Pipeline().list_all_companies()

        return [ticket['code'] for ticket in response.transformed_information]

    def get_data(self, ticket: str) -> list:
        """Get data from pyfundamentus API"""

        # Get data from pyfundamentus API.
        try:
            logger.info(f'Getting data from {ticket}')
            fundamentus_response = Pipeline(ticket).get_all_information()

            return fundamentus_response
        except HttpRequestError as error:
            logger.error(f'Error getting data from {ticket}')
            logger.error(f'Error: {error}')

            return None


# pylint: disable=too-few-public-methods
class DataProcessor(DataProcessorInterface):
    """Data Processor class"""

    def __init__(self, categories: list) -> None:
        self.__categories = categories

    def process_information(self, ticket_data) -> dict:
        """Process the information extracted from pyfundamentus API"""

        temporal_data = {}

        # Extract information from each category.
        for category in self.__categories:
            data_section = ticket_data.transformed_information.get(category, {})
            temporal_data.update(self.extract_information(data_section))

        return temporal_data

    def extract_information(self, data_section: dict) -> dict:
        """Extract information from data_section and store it in temporal_data"""

        data = {}

        # Access the fields of data_section.
        for item in data_section.values():
            if isinstance(item, dict):
                for sub_item in item.values():
                    data[sub_item.title] = sub_item.value
            else:
                data[item.title] = item.value

        return data


# pylint: disable=too-few-public-methods
class DataPersister(DataPersisterInterface):
    """Data Persister class"""

    @staticmethod
    def persist_fundamentus_data(data_frame: pd.DataFrame,
                                 file_name: str,
                                 file_format: str = 'csv') -> None:
        """Persist data to a file"""

        today = datetime.date.today().strftime("%d-%m-%Y")

        logger.info(f'Persisting data to {file_name}_{today}.{file_format}')

        if file_format == 'pkl':
            with open(f'{DownloadCfg.DATA_PATH.value}{file_name}_{today}.pkl', 'wb') as file:
                pickle.dump(data_frame, file)
        elif file_format == 'csv':
            data_frame.to_csv(f'{DownloadCfg.DATA_PATH.value}{file_name}_{today}.csv',
                              index=False,
                              sep=';',
                              encoding='utf-8')


# pylint: disable=too-few-public-methods
class DownloadHandler:
    """Download Handler class"""

    def __init__(self,
                 fetcher: StockFetcher,
                 processor: DataProcessor,
                 persister: DataPersister) -> None:
        self.__fetcher = fetcher
        self.__processor = processor
        self.__persister = persister

    def __log_error(self, tickets_error: list) -> None:
        """Log tickets with errors."""

        for ticket in tickets_error:
            logger.error(f'Error getting data from {ticket}')

    def __fetch_data_concurrently(self,
                                  portfolio: list) -> tuple:
        """Create a ThreadPoolExecutor to get data from pyfundamentus API"""

        if not portfolio:
            portfolio = self.__fetcher.get_all_tickets()

        tickets_data = []
        tickets_error = []

        # Create a ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit the tasks to the executor
            futures = [executor.submit(self.__fetcher.get_data, ticket) for ticket in portfolio]

            # Retrieve the results as they become available
            for future in concurrent.futures.as_completed(futures):
                try:
                    # Raises exception if an error occurred.
                    response = future.result()
                    if response is not None:
                        tickets_data.append(response)
                    else:
                        tickets_error.append(response)
                except ExtractException:
                    continue

        return tickets_data, tickets_error

    def run(self,
            portfolio: list,
            output_file: str,
            file_format: str = 'csv',
            show_tickets_error: bool = 'True') -> None:
        """Run the download handler"""

        # Step 1: Fetch data from pyfundamentus API.
        fundamentus_data, tickets_error = self.__fetch_data_concurrently(portfolio)

        if show_tickets_error:
            self.__log_error(tickets_error)

        # Step 2: Process the data.
        processed_data = [self.__processor.process_information(data) for data in fundamentus_data]

        # Step 3: Persist the data.
        data_frame = pd.DataFrame(processed_data)
        self.__persister.persist_fundamentus_data(data_frame,
                                                  output_file,
                                                  file_format)
