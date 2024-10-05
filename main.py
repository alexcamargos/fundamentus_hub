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

import argparse

import streamlit as st

from fundamentus_hub.dashboard.footer import dasboard_footer
from fundamentus_hub.dashboard.index import dasboard_index
from fundamentus_hub.downloader.handler import (DataPersister,
                                                DataProcessor,
                                                DownloadHandler,
                                                StockFetcher)
from fundamentus_hub.utilities.categories import FundamentusCategories as Categories
from fundamentus_hub.utilities.configuration import DownloadHandler as DownloadCfg
from fundamentus_hub.utilities.configuration import StreamlitConfiguration as StreamlitCfg


def get_arguments() -> argparse.Namespace:
    """Argument parser.

    :return: Argument parser.
    """

    __version__ = '0.0.1'

    # Create the parser.
    parser = argparse.ArgumentParser(
        prog=StreamlitCfg.TITLE.value,
        description=StreamlitCfg.DESCRIPTION.value,
        epilog='Created by Alexsander Lopes Camargos - https://github.com/alexcamargos')

    # Add the arguments.
    parser.add_argument('-d',
                        '--download',
                        action='store_true',
                        help='Download data from fundamentus API.')

    parser.add_argument('-b',
                        '--dashboard',
                        action='store_true',
                        help='Run the Streamlit dashboard.')

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version=f'%(prog)s {__version__}')

    return parser.parse_args()


def download_fundamentus_data(portfolio: list) -> None:
    """Download data from fundamentus API"""

    # Create a StockFetcher instance.
    fetcher = StockFetcher()
    # Create a DataProcessor instance.
    processor = DataProcessor(Categories.categories.value)
    # Create a DataPersister instance.
    persister = DataPersister()

    # Create a DownloadHandler instance.
    handler = DownloadHandler(fetcher, processor, persister)

    handler.run(portfolio,
                DownloadCfg.DATA_FILE.value,
                DownloadCfg.DATA_FORMAT.value)


def main_streamlit_app(portfolio: list) -> None:
    """Main function for Streamlit"""

    st.set_page_config(**StreamlitCfg.PAGE_CONFIG.value)

    st.title(StreamlitCfg.TITLE.value)

    st.write(StreamlitCfg.DESCRIPTION.value)

    dasboard_index()

    dasboard_footer()


if __name__ == '__main__':

    # Test portfolio of stocks.
    test_portfolio = ['WEGE3', 'ITSA4', 'ALOS3', 'EGIE3']

    # Get the arguments.
    args = get_arguments()

    if args.download:
        # Download data from fundamentus API.
        download_fundamentus_data([])
    else:
        # Run the Streamlit dashboard.
        main_streamlit_app(test_portfolio)
