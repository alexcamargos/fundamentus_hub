#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: indicator_metrics.py
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
from fundamentus_hub.utilities.configuration import SGSAPIConfiguration as SGSCfg
from fundamentus_hub.utilities.humanizer import format_metrics_value


@st.cache_data(ttl=3600, show_spinner=False)
def extract_sgs_value(data) -> pd.DataFrame:
    """Extract data from the SGS API and return the last value."""

    return pd.DataFrame(data).set_index('data')


def create_indicator_metrics():
    """Create the indicator metrics."""

    # Initialize the requester interface.
    requester = SGSRequester()

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
            response = extract_sgs_value(requester.make_request(indicator.value['url']))
            raw_value = float(response['valor'].iloc[-1])  # pylint: disable=unsubscriptable-object
            formatted_value = format_metrics_value(raw_value,
                                                   indicator.value.get('output_format',
                                                                       'default'))

            with columns[index]:
                st.metric(value=formatted_value,
                          label=indicator.value['label'],
                          help=indicator.value['help'])
