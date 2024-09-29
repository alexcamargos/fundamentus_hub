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

import fundamentus
import fundamentus.exceptions
import fundamentus.exceptions.http_request_error
import pandas as pd


def get_all_tickets(response: dict) -> list:
    """Get all tickets from pyfundamentus API"""

    return [ticket['code'] for ticket in response]


def get_data(ticket: str) -> list:
    """Get data from pyfundamentus API"""

    try:
        print(f'Getting data from {ticket}')
        fundamentus_response = fundamentus.Pipeline(ticket).get_all_information()

        return fundamentus_response
    except fundamentus.exceptions.http_request_error.HttpRequestError as error:
        print(f'Error getting data from {ticket}')
        print(f'Error: {error}')

        return None


def thread_pool_executor(portfolio: list) -> tuple:
    """Create a ThreadPoolExecutor to get data from pyfundamentus API"""

    data = []
    tickets_error = []

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the tasks to the executor
        futures = [executor.submit(get_data, ticket) for ticket in portfolio]

        # Retrieve the results as they become available
        for future in concurrent.futures.as_completed(futures):
            response = future.result()
            if response is not None:
                data.append(response)
            else:
                tickets_error.append(response)

    return data, tickets_error


def extract_information(data_section):
    """Extract information from data_section and store it in temporal_data"""

    data = {}

    for item in data_section.values():
        if isinstance(item, dict):
            for sub_item in item.values():
                # Acessa os campos de sub_item
                data[sub_item.title] = sub_item.value
        else:
            # Acessa os campos de item (namedtuple)
            data[item.title] = item.value

    return data


def process_information(ticket_data) -> dict:
    """Process the information extracted from pyfundamentus API"""

    temporal_data = {}

    # Categorias a serem processadas
    categories = [
        'stock_identification',
        'financial_summary',
        'price_information',
        'detailed_information',
        'oscillations',
        'valuation_indicators',
        'profitability_indicators',
        'indebtedness_indicators',
        'balance_sheet',
        'income_statement'
    ]

    # Itera pelas categorias e extrai as informações.
    for category in categories:
        data_section = ticket_data.transformed_information.get(category, {})
        temporal_data.update(extract_information(data_section))

    return temporal_data


def persist_fundamentus_data(data_frame: pd.DataFrame,
                             file_name: str,
                             file_format: str = 'pkl') -> None:
    """Persist data to a file"""

    today = datetime.date.today().strftime("%d-%m-%Y")

    if file_format == 'pkl':
        # Save data to a pickle file.
        with open(f'{file_name}_{today}.pkl', 'wb') as file:
            pickle.dump(data_frame, file)
    elif file_format == 'csv':
        # Save data to a csv file.
        data_frame.to_csv(f'{file_name}_{today}.csv',
                          index=False,
                          sep=';',
                          encoding='utf-8')


if __name__ == '__main__':

    PORTFOLIO = ['WEGE3', 'MGLU3', 'VALE3']

    # Get data from fundamentus.
    all_companies_response = fundamentus.Pipeline().list_all_companies()
    all_tickets = get_all_tickets(all_companies_response[0])

    tickets_data, tickets_error = thread_pool_executor(PORTFOLIO)
    fundamentus_data = [process_information(ticket_data) for ticket_data in tickets_data]

    df = pd.DataFrame(fundamentus_data)

    persist_fundamentus_data(df, 'fundamentus_data', file_format='csv')
