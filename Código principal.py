import warnings
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import openpyxl
warnings.filterwarnings('ignore')

cidades = """porto-de-moz
prainha
primavera
quatipuru
redencao
rio-maria
rondon-do-para
ruropolis
salinopolis
salvaterra
santa-barbara-do-para
santa-cruz-do-arari
santa-izabel-do-para
santa-luzia-do-para
santa-maria-das-barreiras
santa-maria-do-para
santana-do-araguaia
santarem
santarem-novo
santo-antonio-do-taua
sao-caetano-de-odivelas
sao-domingos-do-araguaia
sao-domingos-do-capim
sao-felix-do-xingu
sao-francisco-do-para
sao-geraldo-do-araguaia
sao-joao-da-ponta
sao-joao-de-pirabas
sao-joao-do-araguaia
sao-miguel-do-guama
sao-sebastiao-da-boa-vista
sapucaia
senador-jose-porfirio
soure
tailandia
terra-alta
terra-santa
tome-acu
tracuateua
trairao
tucuma
tucurui
ulianopolis
uruara
vigia
viseu
vitoria-do-xingu
xinguara"""
city = cidades.split("\n")
#Criar Tabela só com as colunas



for cid in city:
    horario = pd.DataFrame(columns=['info','Valor'])
    #Informações do navegador
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = f"https://cidades.ibge.gov.br/brasil/pa/{cid}/panorama" #Endereço da pagina
    headers={'User-Agent':user_agent} 
    request=urllib.request.Request(url,None,headers) 
    url = urllib.request.urlopen(request)

    #Pegar código HTML da pagina
    html = BeautifulSoup(url.read(),"html.parser")

    #Limpar os dados
    info = html.find_all("td",{"class":"lista__nome"})
    inf=[]
    for i in info:
        text = i.get_text().strip()
        text = text[:text.find("\n")]
        inf.append(text)

    valor = html.find_all("td",{"class":"lista__valor"})

    #Limpar os dados
    val=[]
    for i in valor:
        text = i.get_text().strip()
        text = text.split(" ")
        val.append(text[0])

    for t in range(len(val)):
        horario = horario.append({"info":inf[t],"Valor":val[t]},ignore_index=True)

    horario.to_excel(f"{cid}.xlsx")
    print(f"Cidade: {cid}, capturados!")
