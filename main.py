#talvez tenha que setar essa variável para
# set PYTHONIOENCODING=utf-8
# para poder a saída do arquivo funcionar


from html2txt import converters  # bilioteca que faz a conversão de HTML para texto puro
from collections import Counter # biblioteca que nos possibilita contar a ocorrência de palavras mais facilmente
import re #importa modulo que usa Regular Expressions RegEx


#abre o arquivo contendo a ata de audiência
arquivo = open("ata_sentenca.txt", "r", encoding='UTF-8')
conteudo_arquivo = arquivo.read()

#converte o arquivo de HTML para txt puro
markdown = converters.Html2Markdown().convert(conteudo_arquivo)
print(markdown)

#conta a ocorrência de cada palabra
aparicoes = Counter(markdown.split())

#lista com possíveis palavras para cada situação
adiar = ['redesigno', 'adia-se', 'adiar']
sentenca = ['ENCERRADA', 'INSTRUÇÃO', 'PROCESSUAL', 'RECUSADA', 'SEGUNDA', 'PROPOSTA', 'CONCILIATÓRIA']
pericia = ['PERÍCIA', 'doença', 'ocupacional', 'insalubridade', 'insalubre', 'periculosidade', 'periculoso', 'quesitos', 'laudo']


#verifica se o processo foi encerrado para sentença
# busca na ata o padrão de encerramento mais comum
# DESIGNANDO O **DIA 16/12/2022, **PARA PUBLICAÇÃO DA SENTENÇA
# essa expressão regular localiza o padrão DIA DD/MM/YYYY ENTRE AS PALAVRAS 'DESIGNANDO O' E 'PARA PUBLICAÇÃO DA SENTENÇA'

padrao_encerrada_para_sentenca = re.compile('DESIGNANDO O.*DIA [0-9]{2}/[0-9]{2}/[0-9]{4}.*PARA PUBLICAÇÃO DA SENTENÇA')
busca = padrao_encerrada_para_sentenca.search(markdown)
if busca:
    print(f"Processo encerrado para sentenção a ser prolatada no dia {busca.group()}")
    for palavra in aparicoes.keys():
        if palavra in sentenca:
            print(f"{palavra} - {aparicoes[palavra]}")


#varre cada palavra em busca de algum contexto
for palavra in aparicoes.keys():
    if palavra in adiar:
        print(f"{palavra} - {aparicoes[palavra]}")
    if palavra in pericia:
        print(f"{palavra} - {aparicoes[palavra]}")


