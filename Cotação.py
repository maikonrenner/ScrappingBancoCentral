import requests
import time, sys

#Autenticando no proxy com auth NTLM
from requests_ntlm2 import HttpNtlmAuth
auth=HttpNtlmAuth('DOMINIO\\USER','PW')

frase = "Olá sou o CWBLab, "
frase2 = "Estou acessando o Banco Central, para coletar dados do DOLAR!"
frase3 = "Estou enviando os dados para o INDICADOR DE COTAÇÃO,"
frase4 = " Prontinho! ;)"

for i in list(frase):
    print(i, end='')
    #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
    sys.stdout.flush()
    time.sleep(0.05)


for i in list(frase2):
    print(i, end='')
    #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
    sys.stdout.flush()
    time.sleep(0.05)

#Chamada da url para o scrapping
r = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2018'&@dataFinalCotacao='12-31-2022'&$top=10000&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao", auth=auth)
dolar = r.json()
print(dolar)

#Extraçao e tratamento dos dados capturados no requests
import pandas as pd 
from datetime import datetime #Chamada para a captura da data e hora
data_hora = datetime.today() #Data:Hora

table = list()
item = {
    
    "Periodo": data_hora,
    "Compra": dolar['cotacaoCompra'],
    "Venda": dolar['cotacaoVenda'],

}

table.append(item)
df = pd.DataFrame(table)
print(df)