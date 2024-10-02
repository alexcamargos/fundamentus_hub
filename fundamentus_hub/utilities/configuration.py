#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: configuration.py
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

from enum import Enum


class StreamlitConfiguration(Enum):
    """Configuration class"""

    # Streamlit configuration
    PAGE_CONFIG = {
        'layout': 'wide',
        'page_title': 'Fundamentus Hub',
        'page_icon': '📊',
    }

    TITLE = 'Fundamentus Hub'
    DESCRIPTION = 'Este projeto cria um dashboard utilizando a API pyfundamentus para exibir os principais indicadores financeiros das empresas listadas na B3, facilitando a análise fundamentalista através de visualizações claras e acessíveis para investidores e analistas.'


class SGSAPIConfiguration(Enum):
    """Configuration class"""

    # BCData API URL
    TAXA_SELIC = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json'
    IPCA = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json'
    IGPM = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados?formato=json'
    DOLAR = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json'
    EURO = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados?formato=json'
    PIB = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.7326/dados?formato=json'
