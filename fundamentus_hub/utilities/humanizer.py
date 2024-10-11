#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: humanizer.py
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

def format_metrics_value(raw_value: float, output_format: str) -> str:
    """Format the value according to the output format.

    Arguments:
        raw_value (float): The raw value to be formatted.
        output_format (str): The output format.

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


def format_value(value: float,
                 is_monetary: bool = False,
                 is_percentage: bool = False) -> str:
    """
    Format the value based on whether it is monetary or percentage.

    Parameters:
        value (float): The numeric value to be formatted.
        is_monetary (bool): Whether the value is a monetary value.
        is_percentage (bool): Whether the value is a percentage value.

    Returns:
        str: The formatted value.
    """
    if is_monetary:
        return humanize_number(value)

    if is_percentage:
        return to_percentage(value)

    return f'{value:.2f}'


def to_percentage(value: float) -> str:
    """
    Converts a float value into a percentage string.

    Parameters:
        value (float): The value to be converted into a percentage.

    Returns:
        str: The percentage representation of the value.
    """
    return f'{value * 100:.2f}%'


def humanize_number(value) -> str:
    """
    Converts a large number into a human-readable format
    with suffixes (e.g., mil, M, B), ensuring that the input
    is numeric and divisions are performed only on valid values.

    Parameters:
        value: The value to be humanized, expected to be a
               numeric type (int or float).

    Returns:
        str: A human-readable version of the number with
             appropriate suffix or an error message.
    """

    if value == 0:
        return f'R$ {value:.0f}'

    if abs(value) >= 1_000_000_000:
        humanized_value = f'R$ {value / 1_000_000_000:.3f} B'
    elif abs(value) >= 1_000_000:
        humanized_value = f'R$ {value / 1_000_000:.3f} M'
    elif abs(value) >= 1_000:
        humanized_value = f'R$ {value / 1_000:.3f} mil'
    else:
        humanized_value = f'R$ {value:.3f}'

    return humanized_value
