#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: footer.py
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


def dasboard_footer():
    footer = '''
        <style>
            .footer {
                left: 0;
                bottom: 0;
                width: 100%;
                text-align: center;
                padding: 10px 0;
                font-size: 14px;
                border-top: 1px solid #eaeaea;
            }
        </style>

        <div class="footer">
            Criado com ❤️ usando Streamlit. © 2024 -
            <a href="https://github.com/alexcamargos" target="_blank">
                Alexsander Lopes Camargos
            </a>
        </div>
    '''

    # Adicionando o rodapé ao app
    st.markdown(footer, unsafe_allow_html=True)
