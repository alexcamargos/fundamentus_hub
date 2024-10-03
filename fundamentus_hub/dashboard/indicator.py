#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: indicator.py
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

import pandas as pd
import streamlit as st

from fundamentus_hub.downloader.requester import SGSRequester
from fundamentus_hub.utilities.configuration import \
    SGSAPIConfiguration as SGSCfg


@st.cache_data(ttl=3600, suppress_st_warning=True)
def extract_sgs_value(data) -> float:
    """Extract data from the SGS API and return the last value."""

    data_frame = pd.DataFrame(data)
    data_frame = data_frame.set_index('data')
    values = data_frame['valor']

    return float(values.iloc[-1])


def format_value(raw_value: float, output_format: str) -> str:
    """Format the value according to the output format.

    Arguments:
        raw_value (float) -- The raw value to be formatted.
        output_format (str) -- The output format.

    Returns:
        The formatted value.
    """

    if output_format == 'percent_aa':
        return f'{raw_value:.2f}% a.a.'

    if output_format == 'percent_am':
        return f'{raw_value:.2f}% a.m.'

    if output_format == 'currency':
        return f'R${raw_value:,.2f}'

    return f'{raw_value:.2f}'


def create_indicator_metrics():
    """Create the indicator metrics."""

    st.subheader('Indicadores Econômicos')

    with st.spinner('Acessando o Sistema Gerenciador de Séries Temporais do Banco Central...'):
        # Obter os itens do Enum que são dicionários
        indicators = [indicator for indicator in SGSCfg if isinstance(indicator.value,
                                                                      dict)]

        # Determinar o número de colunas por linha (divide por 2)
        num_indicators = len(indicators)
        num_columns = (num_indicators + 1) // 2  # Número de colunas por linha

        # Cria as colunas para as duas linhas
        columns = st.columns(num_columns) + st.columns(num_columns)

        # Distribui os indicadores entre as colunas
        for index, indicator in enumerate(indicators):
            raw_value = extract_sgs_value(SGSRequester(indicator.value['url']).make_request())
            formatted_value = format_value(raw_value, indicator.value.get('output_format',
                                                                          'default'))

            with columns[index]:
                st.metric(value=formatted_value,
                          label=indicator.value['label'],
                          help=indicator.value['help'])
