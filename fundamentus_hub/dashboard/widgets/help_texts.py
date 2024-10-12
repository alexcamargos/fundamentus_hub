#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: help_texts.py
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

HELP_TEXTS = {
    'Cotação': 'Preço de fechamento da ação no último pregão.',
    'P/L': 'Preço da ação dividido pelo lucro por ação. O P/L é o número de anos que se levaria para reaver o capital aplicado na compra de uma ação, através do recebimento do lucro gerado pela empresa, considerando que esses lucros permaneçam constantes.',
    'P/VP': 'Preço da ação dividido pelo Valor Patrimonial por ação. Informa quanto o mercado está disposto a pagar sobre o Patrimônio Líquido da empresa.',
    'P/EBIT': 'Preço da ação dividido pelo EBIT por ação. EBIT é o Lucro antes dos Impostos e Despesas Financeiras. É uma boa aproximação do lucro operacional da empresa.',
    'PSR': 'Price Sales Ratio: Preço da ação dividido pela Receita Líquida por ação.',
    'Preço/Ativos': 'Preço da ação dividido pelos Ativos totais por ação.',
    'Preço/Ativ circ liq': 'Preço da ação dividido pelos Ativos Circulantes Líquidos por ação. Ativo Circ. Líq. é obtido subtraindo os ativos circulantes pelas dívidas de curto e longo prazo, ou seja, após o pagamento de todas as dívidas, quanto sobraria dos ativos mais líquidos da empresa (caixa, estoque, etc).',
    'Dividend Yield': 'Dividendo pago por ação dividido pelo preço da ação. É o rendimento gerado para o dono da ação pelo pagamento de dividendos.',
    'EV/EBITDA': 'Valor da Firma (Enterprise Value dividido pelo EBITDA).',
    'EV/EBIT': 'Valor da Firma (Enterprise Value dividido pelo EBIT).',
    'Preço/Capital de giro': 'Preço da ação dividido pelo capital de giro por ação. Capital de giro é o Ativo Circulante menos Passivo Circulante.',
    'ROE': 'Retorno sobre o Patrimônio Líquido: Lucro líquido dividido pelo Patrimônio Líquido.',
    'ROIC': 'Retorno sobre o Capital Investido: Calculado dividindo-se o EBIT por (Ativos - Fornecedores - Caixa). Informa o retorno que a empresa consegue sobre o capital total aplicado.',
    'EBIT/Ativo': 'EBIT dividido pelo Ativo total. Indica a capacidade de geração de lucro da empresa em relação ao total de ativos.',
    'Crescimento receita': 'Crescimento da Receita Líquida nos últimos cinco anos.',
    'Giro ativos': 'Receita Líquida dividida pelo Ativo total. Indica a eficiência da empresa em gerar receita a partir de seus ativos.',
    'Margem bruta': 'Lucro Bruto dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o custo dos produtos/serviços vendidos.',
    'Margem EBIT': 'EBIT dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o pagamento dos custos dos produtos/serviços vendidos, das despesas com vendas, gerais e administrativas.',
    'Margem líquida': 'Lucro Líquido dividido pela Receita Líquida: Indica a porcentagem de cada R$1,00 de venda que sobrou após o pagamento de todos os custos e despesas.',
    'Liquidez corrente': 'Ativo Circulante dividido pelo Passivo Circulante: Reflete a capacidade de pagamento da empresa no curto prazo.',
    'Dívida bruta/Patrim': 'Dívida Bruta (Dívida + Debêntures) dividida pelo Patrimônio Líquido: Indica quanto a empresa deve em relação ao seu patrimônio líquido.',
    'Dívida líquida/Patrim': 'Dívida Líquida (Dívida Bruta - Disponibilidades) dividida pelo Patrimônio Líquido: Indica quanto a empresa deve em relação ao seu patrimônio líquido.',
    'Dívida líquida/EBITDA': 'Dívida Líquida (Dívida Bruta - Disponibilidades) dividida pelo EBITDA: Indica quantos anos a empresa levaria para pagar sua dívida líquida com o EBITDA.',
    'PL/Ativos': 'Patrimônio Líquido dividido pelos Ativos Totais: Indica a proporção de recursos próprios em relação ao total de ativos da empresa.',
    'Ativo': 'Todos os bens, direitos e valores a receber de uma entidade.',
    'Ativo circulante': 'Bens ou direitos que podem ser convertido em dinheiro em curto prazo.',
    'Disponibilidades': 'Bens numerários (dinheiro) disponíveis em caixa ou em bancos.',
    'Dívida bruta': 'Dívida Bruta é obtida somando-se as dívidas de curto e longo prazo mais as debêntures de curto e longo prazo.',
    'Dívida líquida': 'Dívida Bruta menos Disponibilidades. Se este valor é negativo, significa que a empresa possui caixa líquido positivo.',
    'Patrimônio líquido': 'O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, a diferença entre o valor dos ativos e dos passivos e resultado de exercícios futuros representa o PL (Patrimônio Líquido), que é o valor contábil devido pela pessoa jurídica aos sócios ou acionistas.',
    'Receita líquida': 'Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.',
    'EBIT': 'Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - Despesas de vendas - Despesas administrativas',
    'Lucro líquido': 'Lucro Líquido é o resultado da empresa após o pagamento de todas as despesas, impostos e juros.',
}
