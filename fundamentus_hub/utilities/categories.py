#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: categories.py
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


class FundamentusCategories(Enum):
    """Categories for Fundamentus API"""

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
