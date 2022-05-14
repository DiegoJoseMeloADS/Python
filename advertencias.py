import requests
from googletrans import Translator

link = "https://api.adviceslip.com/advice"


requisicao = requests.get(link)

requisicao_dic = requisicao.json()

alerta = requisicao_dic['slip']['advice']

tradutor = Translator()

alerta_traduzido = tradutor.translate(alerta, dest = "pt").text

print(f'O conselho do dia é {alerta_traduzido}')
