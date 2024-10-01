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

import pandas as pd
import streamlit as st

from fundamentus_hub.utilities.configuration import BCDataAPIConfiguration as BCDataAPICfg


@st.cache_data
def get_sgs_data(url: str) -> float:
    '''Get data from API'''

    data_frame = pd.read_json(url)
    index = data_frame.set_index('data')
    value = index['valor']

    return value[-1]


def dasboard_index():
    with st.spinner('Baixando Informações...'):
        # Obtém a taxa Selic a partir da URL e processa os dados
        indicators = {
            'Taxa Selic': {
                'label': ':green[Taxa Selic]',
                'value': f'{get_sgs_data(BCDataAPICfg.TAXA_SELIC.value)}%'},
            'Dólar': {
                'label': ':green[Dólar]',
                'value': f'R${get_sgs_data(BCDataAPICfg.DOLAR.value):.2f}'},
            'Euro': {
                'label': ':green[Euro]',
                'value': f'R${get_sgs_data(BCDataAPICfg.EURO.value):.2f}'},
            'IPCA': {
                'label': ':green[IPCA]',
                'value': f'{get_sgs_data(BCDataAPICfg.IPCA.value)}%'},
            'IGPM': {
                'label': ':green[IGPM]',
                'value': f'{get_sgs_data(BCDataAPICfg.IGPM.value)}%'},
            'PIB': {
                'label': ':green[PIB]',
                'value': f'{get_sgs_data(BCDataAPICfg.PIP.value)}%'}
        }

        # Criando colunas dinamicamente de acordo com o número de indicadores
        columns = st.columns(len(indicators))

        # Preenchendo cada coluna com o rótulo e valor configuráveis
        for column, (key, data) in zip(columns, indicators.items()):
            column.metric(label=data['label'], value=data['value'])
