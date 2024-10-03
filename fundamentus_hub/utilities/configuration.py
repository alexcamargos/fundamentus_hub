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
    __API = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato={}'
    # API response format.
    __RESPONSE_FORMAT = 'json'

    # 432 - Taxa de juros - Meta Selic definida pelo Copom.
    TAXA_SELIC = {'url': __API.format(432, __RESPONSE_FORMAT),
                  'label': ':green[Taxa Selic]',
                  'help': 'Taxa de juros - Meta Selic definida pelo Copom.',
                  'output_format': 'percent_aa'}
    # 4389 - Taxa de juros - CDI anualizada base 252.
    CDI = {'url': __API.format(4389, __RESPONSE_FORMAT),
           'label': ':green[CDI]',
           'help': 'Taxa de juros - CDI anualizada base 252.',
           'output_format': 'percent_aa'}
    # 226 - Taxa referencial (TR).
    TR = {'url': __API.format(226, __RESPONSE_FORMAT),
          'label': ':green[TR]',
          'help': 'Taxa referencial (TR).',
          'output_format': 'percent_am'}
    # 256 - Taxa de juros de longo prazo - TJLP.
    TJLP = {'url': __API.format(256, __RESPONSE_FORMAT),
            'label': ':green[TJLP]',
            'help': 'Taxa de juros de longo prazo - TJLP.',
            'output_format': 'percent_aa'}
    # 253 - Taxa básica financeira (TBF).
    TBF = {'url': __API.format(253, __RESPONSE_FORMAT),
           'label': ':green[TBF]',
           'help': 'Taxa básica financeira (TBF).',
           'output_format': 'percent_am'}
    # 195 - Depósitos de poupança a partir de 04.05.2012 - Rentabilidade no período.
    POUPANCA = {'url': __API.format(195, __RESPONSE_FORMAT),
                'label': ':green[Poupança]',
                'help': 'Depósitos de poupança a partir de 04.05.2012 - Rentabilidade no período.',
                'output_format': 'percent_am'}
    # 433 - Índice nacional de preços ao consumidor-amplo (IPCA).
    ICPA = {'url': __API.format(433, __RESPONSE_FORMAT),
            'label': ':green[IPCA]',
            'help': 'Índice nacional de preços ao consumidor-amplo (IPCA).',
            'output_format': 'percent_aa'}
    # 189 - Índice geral de preços do mercado (IGP-M).
    IGPM = {'url': __API.format(189, __RESPONSE_FORMAT),
            'label': ':green[IGP-M]',
            'help': 'Índice geral de preços do mercado (IGP-M).',
            'output_format': 'percent_am'}
    # 1 - Taxa de câmbio - Livre - Dólar americano (venda) - diário.
    DOLAR = {'url': __API.format(1, __RESPONSE_FORMAT),
             'label': ':green[Dólar]',
             'help': 'Taxa de câmbio - Livre - Dólar americano (venda) - diário.',
             'output_format': 'currency'}
    # 21619	Taxa de câmbio - Livre - Euro (venda).
    EURO = {'url': __API.format(21619, __RESPONSE_FORMAT),
            'label': ':green[Euro]',
            'help': 'Taxa de câmbio - Livre - Euro (venda).',
            'output_format': 'currency'}
    # 7326 - Produto Interno Bruto - Taxa de variação real no ano.
    PIB = {'url': __API.format(7326, __RESPONSE_FORMAT),
           'label': ':green[PIB]',
           'help': 'Produto Interno Bruto - Taxa de variação real no ano.',
           'output_format': 'percent_aa'}
    # 13521 - Meta para a inflação.
    META_INFLACAO = {'url': __API.format(13521, __RESPONSE_FORMAT),
                     'label': ':green[Meta Inflação]',
                     'help': 'Meta para a inflação.',
                     'output_format': 'percent_aa'}
