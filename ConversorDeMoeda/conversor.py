from PyQt5 import uic, QtWidgets
from cotacoes.AllCotacoes import *


def Converter():
    # exceção caso valor seja vazio 
    try:
        valor = tela.inputValor.text().replace(',','.')
        valor = float(valor)
    except:
        tela.inputValor.setText('1')
        valor = 1

    moeda_inicial = tela.cbMoedaInicial.currentText()
    moeda_cambio = tela.cbMoedaCambio.currentText()
    
    for cotacao_k, cotacao_v in dic_cotacoes.items():
        if cotacao_k == moeda_inicial:
            moeda_inicial = cotacao_v
            moeda_inicial.replace(',', '.')
            moeda_inicial = float(moeda_inicial)
        if cotacao_k == moeda_cambio:
            moeda_cambio = cotacao_v
            moeda_cambio.replace(',', '.')
            moeda_cambio = float(moeda_cambio)
                      
    resultado = converte_moedas(valor=valor, moeda_inicial=moeda_inicial, moeda_cambio=moeda_cambio)

    tela.lbResultado.setText(str(resultado))
    tela.lbData.setText(f'Data da Cotação: {str(data)}')


app = QtWidgets.QApplication([])
tela = uic.loadUi("interfaces/TelaPrincipal.ui")

tela.btnConverter.clicked.connect(Converter)

tela.show()
app.exec()
