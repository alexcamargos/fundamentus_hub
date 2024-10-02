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
    """Configuration for 'Sistema Gerenciador de Séries Temporais do Banco Central'."""

    # SGS API URL.
    API = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato={}'
    # API response format.
    RESPONSE_FORMAT = 'json'
    # 432 - Taxa de juros - Meta Selic definida pelo Copom.
    TAXA_SELIC = API.format(432, RESPONSE_FORMAT)
    # 4389 - Taxa de juros - CDI anualizada base 252.
    CDI = API.format(4389, RESPONSE_FORMAT)
    # 13521 - Meta para a inflação.
    META_INFLACAO = API.format(13521, RESPONSE_FORMAT)
    # 433 - Índice nacional de preços ao consumidor-amplo (IPCA).
    IPCA = API.format(433, RESPONSE_FORMAT)
    # 189 - Índice geral de preços do mercado (IGP-M)
    IGPM = API.format(189, RESPONSE_FORMAT)
    # 1 - Taxa de câmbio - Livre - Dólar americano (venda) - diário.
    DOLAR = API.format(1, RESPONSE_FORMAT)
    # 21619	Taxa de câmbio - Livre - Euro (venda).
    EURO = API.format(21619, RESPONSE_FORMAT)
    # 7326 - Produto Interno Bruto - Taxa de variação real no ano
    PIB = API.format(7326, RESPONSE_FORMAT)
