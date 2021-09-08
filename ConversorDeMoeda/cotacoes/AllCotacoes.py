import requests
import pandas as pd
from datetime import datetime


def converte_moedas(valor, moeda_inicial, moeda_cambio):
        valor = float(valor)
        moeda_inicial = float(moeda_inicial)
        moeda_cambio = float(moeda_cambio)
        conversao = (valor*moeda_inicial) / moeda_cambio
        return round(conversao, 5)

# Data Atual
data = datetime.now().date()

# Requisição de Cotações
requisicao =  requests.get("https://economia.awesomeapi.com.br/json/all")
requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USD"]["bid"]
cotacao_euro = requisicao_dic["EUR"]["bid"]
cotacao_btc = requisicao_dic["BTC"]["bid"]
cotacao_cad = requisicao_dic["CAD"]["bid"]
cotacao_gbp = requisicao_dic["GBP"]["bid"]
cotacao_ars = requisicao_dic["ARS"]["bid"]
cotacao_ltc = requisicao_dic["LTC"]["bid"]
cotacao_jpy = requisicao_dic["JPY"]["bid"]
cotacao_chf = requisicao_dic["CHF"]["bid"]
cotacao_aud = requisicao_dic["AUD"]["bid"]
cotacao_cny = requisicao_dic["CNY"]["bid"]
cotacao_ils = requisicao_dic["ILS"]["bid"]
cotacao_eth = requisicao_dic["ETH"]["bid"]
cotacao_xrp = requisicao_dic["XRP"]["bid"]
cotacao_doge = requisicao_dic["DOGE"]["bid"]
cotacao_brl = "1.0"

# Tabela excel com cotações
tabela = pd.read_excel("cotacoes/AllCotações.xlsx")
tabela.loc[0, "Cotação"] = float(cotacao_dolar)
tabela.loc[1, "Cotação"] = float(cotacao_euro)
tabela.loc[2, "Cotação"] = float(cotacao_btc) * 1000
tabela.loc[3, "Cotação"] = float(cotacao_cad)
tabela.loc[4, "Cotação"] = float(cotacao_gbp)
tabela.loc[5, "Cotação"] = float(cotacao_ars)
tabela.loc[6, "Cotação"] = float(cotacao_ltc)
tabela.loc[7, "Cotação"] = float(cotacao_jpy)
tabela.loc[8, "Cotação"] = float(cotacao_chf)
tabela.loc[9, "Cotação"] = float(cotacao_aud)
tabela.loc[10, "Cotação"] = float(cotacao_cny)
tabela.loc[11, "Cotação"] = float(cotacao_ils)
tabela.loc[12, "Cotação"] = float(cotacao_eth)
tabela.loc[13, "Cotação"] = float(cotacao_xrp)
tabela.loc[14, "Cotação"] = float(cotacao_doge)
tabela.loc[15, "Cotação"] = float(cotacao_brl)
tabela.loc[0, "Data Última Atualização"] = datetime.now()
tabela.to_excel("cotacoes/AllCotações.xlsx", index=False)


# Dicionario com cotaçôes
dic_cotacoes = {'Dólar-USD':cotacao_dolar,'Euro-EUR':cotacao_euro,'Bitcoin-BTC':cotacao_btc ,'Dólar Canadense-CAD': cotacao_cad,'Libra Esterlina-GBP':cotacao_gbp,'Peso Argentino-ARS':cotacao_ars,'Litecoin-LTC':cotacao_ltc,'Iene Japonês-JPY':cotacao_jpy,'Franco Suíço-CHF':cotacao_chf,'Dólar Australiano-AUD':cotacao_aud,'Yuan Chinês-CNY':cotacao_cny,'Novo Shekel Israelense-ILS':cotacao_ils,'Ethereum-ETH':cotacao_eth,'Ripple-XRP':cotacao_xrp,'Dogecoin-DOGE':cotacao_doge,'Real-BRL':cotacao_brl}
