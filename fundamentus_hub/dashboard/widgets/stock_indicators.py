#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: stock_indicators.py
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

from typing import List

import pandas as pd
import streamlit as st

from fundamentus_hub.utilities.humanizer import format_value


def create_metric_columns(indicators: list, columns_per_row: int = 6) -> None:
    """
    Creates metric columns for the dashboard using st.metric.

    Parameters:
        indicators (list): A list of dictionaries containing 'label',
                           'value', and optional 'help' for each metric.
        columns_per_row (int): The number of columns to display per row.
                               Default is 6.
    """

    for start_index in range(0, len(indicators), columns_per_row):
        columns = st.columns(min(columns_per_row,
                                 len(indicators) - start_index))

        for column_index, column in enumerate(columns):
            if start_index + column_index < len(indicators):
                indicator = indicators[start_index + column_index]

                with column:
                    st.metric(label=indicator["label"],
                              value=indicator["value"],
                              help=indicator.get("help", ""))


def show_market_indicators(data: pd.Series) -> None:
    """Displays market indicators."""

    columns = st.columns(2)

    with columns[0]:
        st.write(f'**Tipo**: {data["Tipo"]}')
        st.write(f'**Setor**: {data["Setor"]}')
        st.write(f'**Subsetor**: {data["Subsetor"]}')
        st.write(f'**Último balanço**: {data["Último balanço"]}')

    with columns[1]:
        st.write(f'**Nº de ações**: {data["Nº de ações"]}')
        st.write(f'**Valor de mercado**: {format_value(data["Valor de mercado"], is_monetary=True)}')
        st.write(f'**Valor da firma**: {format_value(data["Valor da firma"], is_monetary=True)}')
        st.write(f'**Volume negociado por dia**: {format_value(data["Volume negociado por dia"], is_monetary=True)}')


def display_oscillation_row(columns: List[st.delta_generator.DeltaGenerator],
                            periods: list,
                            data: pd.DataFrame) -> None:
    """Helper function to display a row of oscillation indicators."""

    for column_index, period in enumerate(periods):
        with columns[column_index]:
            st.write(f'**{period.capitalize()}:** {format_value(data[period], is_percentage=True)}')


def show_oscillations(data: pd.Series) -> None:
    """Displays oscillations indicators in two rows of four columns each."""

    # Define the keys and labels for each set of data
    time_periods_row1 = ["dia", "mês", "30 dias", "12 meses"]
    time_periods_row2 = ["2024", "2023", "2022", "2021"]

    # Create first row of oscillation indicators
    with st.container():
        columns = st.columns(4)
        display_oscillation_row(columns, time_periods_row1, data)

    # Create second row of oscillation indicators
    with st.container():
        columns = st.columns(4)
        display_oscillation_row(columns, time_periods_row2, data)


def show_valuation_indicators(data: pd.Series) -> None:
    """Displays valuation indicators."""

    valuation_indicators = [
        {'label': 'P/L',
         'value': format_value(data["P/L"]),
         'help': 'Help text in future'},
        {'label': 'P/VP',
         'value': format_value(data["P/VP"]),
         'help': 'Help text in future'},
        {'label': 'P/EBIT',
         'value': format_value(data["P/EBIT"]),
         'help': 'Help text in future'},
        {'label': 'PSR',
         'value': format_value(data["PSR"]),
         'help': 'Help text in future'},
        {'label': 'Preço/Ativos',
         'value': format_value(data["Preço/Ativos"]),
         'help': 'Help text in future'},
        {'label': 'Preço/Ativ circ liq',
         'value': format_value(data["Preço/Ativ circ liq"]),
         'help': 'Help text in future'},
        {'label': 'Dividend Yield',
         'value': format_value(data["Dividend Yield"], is_percentage=True),
         'help': 'Help text in future'},
        {'label': 'EV/EBITDA',
         'value': format_value(data["EV/EBITDA"]),
         'help': 'Help text in future'},
        {'label': 'EV/EBIT',
         'value': format_value(data["EV/EBIT"]),
         'help': 'Help text in future'},
        {'label': 'Preço/Capital de giro',
         'value': format_value(data["Preço/Capital de giro"]),
         'help': 'Help text in future'},
    ]

    create_metric_columns(valuation_indicators, columns_per_row=5)


def show_profitability_indicators(data: pd.Series) -> None:
    """Displays profitability indicators."""

    profitability_indicators = [
        {'label': 'ROE',
         'value': f'{format_value(data["ROE"], is_percentage=True)}',
         'help': 'Help text in future'},
        {'label': 'ROIC',
         'value': f'{format_value(data["ROIC"], is_percentage=True)}',
         'help': 'Help text in future'},
        {'label': 'EBIT/Ativo',
         'value': f'{format_value(data["EBIT/Ativo"])}',
         'help': 'Help text in future'},
        {'label': 'Crescimento receita',
         'value': f'{format_value(data["Crescimento receita"], is_percentage=True)}',
         'help': 'Help text in future'},
        {'label': 'Giro ativos',
         'value': f'{format_value(data["Giro ativos"])}',
         'help': 'Help text in future'},
        {'label': 'Margem bruta',
         'value': f'{format_value(data["Margem bruta"], is_percentage=True)}',
         'help': 'Help text in future'},
        {'label': 'Margem EBIT',
         'value': f'{format_value(data["Margem EBIT"], is_percentage=True)}',
         'help': 'Help text in future'},
        {'label': 'Margem líquida',
         'value': f'{format_value(data["Margem líquida"], is_percentage=True)}',
         'help': 'Help text in future'},
    ]

    create_metric_columns(profitability_indicators, columns_per_row=4)


def show_indebtedness_indicators(data: pd.Series) -> None:
    """Displays indebtedness indicators."""

    indebtedness_indicators = [
        {'label': 'Liquidez corrente',
         'value': f'R$ {data["Liquidez corrente"]:,.2f}',
         'help': 'Help text in future'},
        {'label': 'Dívida bruta/Patrim',
         'value': f'R$ {data["Dívida bruta/Patrim"]:,.2f}',
         'help': 'Help text in future'},
        {'label': 'Dívida líquida/Patrim',
         'value': f'R$ {data["Dívida líquida/Patrim"]:,.2f}',
         'help': 'Help text in future'},
        {'label': 'Dívida líquida/EBITDA',
         'value': f'R$ {data["Dívida líquida/EBITDA"]:,.2f}',
         'help': 'Help text in future'},
        {'label': 'PL/Ativos',
         'value': f'R$ {data["PL/Ativos"]:,.2f}',
         'help': 'Help text in future'},
    ]

    create_metric_columns(indebtedness_indicators)


def show_balance_sheet(data: pd.Series) -> None:
    """Displays balance sheet indicators."""

    balance_sheet = [
        {'label': 'Ativo',
         'value': f'{format_value(data["Ativo"], is_monetary=True)}',
         'help': 'Help text in future'},
        {'label': 'Ativo circulante',
         'value': f'{format_value(data["Ativo circulante"], is_monetary=True)}',
         'help': 'Help text in future'},
        {'label': 'Disponibilidades',
         'value': f'{format_value(data["Disponibilidades"], is_monetary=True)}',
         'help': 'Help text in future'},
        {'label': 'Dívida bruta',
         'value': f'{format_value(data["Dívida bruta"], is_monetary=True)}',
         'help': 'Help text in future'},
        {'label': 'Dívida líquida',
         'value': f'{format_value(data["Dívida líquida"], is_monetary=True)}',
         'help': 'Help text in future'},
        {'label': 'Patrimônio líquido',
         'value': f'{format_value(data["Patrimônio líquido"], is_monetary=True)}',
         'help': 'Help text in future'},
    ]

    create_metric_columns(balance_sheet, columns_per_row=3)


def show_income_statement(data: pd.Series) -> None:
    """Displays income statement indicators."""

    income_statement = [
        {'label': 'Receita líquida',
         'value': f'{format_value(data["Receita líquida"], is_monetary=True)}',
         'help': 'Help text in future'},
        {'label': 'EBIT',
         'value': f'{format_value(data["EBIT"], is_monetary=True)}',
         'help': 'Help text in future'},
        {'label': 'Lucro líquido',
         'value': f'{format_value(data["Lucro líquido"], is_monetary=True)}',
         'help': 'Help text in future'},
    ]

    create_metric_columns(income_statement)
