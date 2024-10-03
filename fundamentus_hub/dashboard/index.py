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

from fundamentus_hub.dashboard.indicator import create_indicator_metrics
from fundamentus_hub.downloader.requester import SGSRequester
from fundamentus_hub.utilities.configuration import \
    SGSAPIConfiguration as SGSCfg


def dasboard_index():
    """Dashboard index page."""

    create_indicator_metrics()
