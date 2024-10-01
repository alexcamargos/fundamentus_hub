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

import streamlit as st

from fundamentus_hub.dashboard.index import dasboard_index
from fundamentus_hub.dashboard.footer import dasboard_footer
from fundamentus_hub.utilities.configuration import StreamlitConfiguration as StreamlitCfg


if __name__ == '__main__':

    st.set_page_config(**StreamlitCfg.PAGE_CONFIG.value)

    st.title(StreamlitCfg.TITLE.value)

    st.write(StreamlitCfg.DESCRIPTION.value)

    dasboard_index()

    dasboard_footer()
