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

"""Dashboard index page."""

from pathlib import Path

import pandas as pd
import streamlit as st

from fundamentus_hub.dashboard.widgets.indicator_metrics import create_indicator_metrics
from fundamentus_hub.dashboard.widgets.stock_indicators import (
    show_balance_sheet, show_income_statement, show_indebtedness_indicators,
    show_market_indicators, show_oscillations, show_profitability_indicators,
    show_valuation_indicators)
from fundamentus_hub.utilities.configuration import DownloadHandler as DownloadCfg


@st.cache_data
def load_and_filter_portfolio(_portfolio: list) -> pd.DataFrame:
    """Load and filter portfolio."""

    # Get the directory path.
    directory_path = Path.cwd() / DownloadCfg.DATA_PATH.value
    csv_files = list(directory_path.glob('*.csv'))

    # Get the oldest and youngest files.
    oldest_data = min(csv_files, key=lambda file: file.stat().st_mtime)
    youngest_data = max(csv_files, key=lambda file: file.stat().st_mtime)

    # Load dataframes.
    oldest_df = pd.read_csv(oldest_data, delimiter=';')
    youngest_df = pd.read_csv(youngest_data,  delimiter=';')

    # Filter dataframes with portfolio.
    oldest_filtered_df = oldest_df[oldest_df['Código'].isin(_portfolio)]
    youngest_filtered_df = youngest_df[youngest_df['Código'].isin(_portfolio)]

    return oldest_filtered_df, youngest_filtered_df


def dasboard_index(portfolio: list) -> None:
    """Dashboard index page."""

    with st.container():
        create_indicator_metrics()

    with st.spinner('Carregando dados...'):
        oldest_df, youngest_df = load_and_filter_portfolio(portfolio)

    data = youngest_df.iloc[0]

    with st.container():
        st.subheader(f'{data["Código"]} - {data["Empresa"]}')

        with st.expander('Indicadores de Mercado', expanded=True):
            show_market_indicators(data)

        with st.expander('Oscilações', expanded=True):
            show_oscillations(data)

        with st.expander('Indicadores de Valuation', expanded=True):
            show_valuation_indicators(data)

        with st.expander('Indicadores de Rentabilidade', expanded=True):
            show_profitability_indicators(data)

        with st.expander('Indicadores de Endividamento', expanded=True):
            show_indebtedness_indicators(data)

        with st.expander('Balanço Patrimonial', expanded=True):
            show_balance_sheet(data)

        with st.expander('Demonstrativo de Resultados', expanded=True):
            show_income_statement(data)
