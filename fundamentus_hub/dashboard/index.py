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

from fundamentus_hub.utilities.configuration import SGSAPIConfiguration as SGSCfg
from fundamentus_hub.downloader.requester import SGSRequester


@st.cache_data(ttl=3600)
def extract_sgs_data(data) -> float:
    """Extract data from the SGS API and return the last value."""

    data_frame = pd.DataFrame(data)
    data_frame = data_frame.set_index('data')
    values = data_frame['valor']

    return float(values.iloc[-1])


def dasboard_index():
    """Dashboard index page."""

    st.subheader('Indicadores Econômicos')

    with st.spinner('Acessando o Sistema Gerenciador de Séries Temporais do Banco Central...'):
        selic_api = SGSRequester(SGSCfg.TAXA_SELIC.value)
        selic_value = extract_sgs_data(selic_api.make_request())

        dolar_api = SGSRequester(SGSCfg.DOLAR.value)
        dolar_value = extract_sgs_data(dolar_api.make_request())

        euro_api = SGSRequester(SGSCfg.EURO.value)
        euro_value = extract_sgs_data(euro_api.make_request())

        ipca_api = SGSRequester(SGSCfg.IPCA.value)
        ipca_value = extract_sgs_data(ipca_api.make_request())

        igpm_api = SGSRequester(SGSCfg.IGPM.value)
        igpm_value = extract_sgs_data(igpm_api.make_request())

        pib_api = SGSRequester(SGSCfg.PIB.value)
        pib_value = extract_sgs_data(pib_api.make_request())

        indicators = {
            'Taxa Selic': {
                'label': ':green[Taxa Selic]',
                'value': f'{selic_value:.2f}%'},
            'Dólar': {
                'label': ':green[Dólar]',
                'value': f'R${dolar_value:.2f}'},
            'Euro': {
                'label': ':green[Euro]',
                'value': f'R${euro_value:.2f}'},
            'IPCA': {
                'label': ':green[IPCA]',
                'value': f'{ipca_value:.2f}%'},
            'IGPM': {
                'label': ':green[IGPM]',
                'value': f'{igpm_value:.2f}%'},
            'PIB': {
                'label': ':green[PIB]',
                'value': f'{pib_value:.2f}%'}
        }

        # Criando colunas dinamicamente de acordo com o número de indicadores
        columns = st.columns(len(indicators))
        # Preenchendo cada coluna com o rótulo e valor configuráveis
        for column, (_, data) in zip(columns, indicators.items()):
            column.metric(label=data['label'], value=data['value'])
