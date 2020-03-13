import nltk
import re
#nltk.download()

texto = 'Os melhores médicos do mundo: o Dr. Dieta, o Dr. Tranquilidade e o Dr. Alegria.' #Jonathan Swift

'''Pré-processamento
Utilizando o split'''
texto_separado = texto.split('.')
texto_separado

texto_separado = texto.split()
texto_separado


'''Utilizando a NLTK
Tokenização'''
palavras = nltk.word_tokenize(texto)
palavras

stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords


'''Removendo as stopwords'''
limpar_dados = [x for x in texto.split() if re.match(r'[^\W\d]*$', x)]
juntar_novamente = ' '.join(limpar_dados)
limpar_texto = [palavra for palavra in juntar_novamente.split() if palavra.lower() not in stopwords]
limpar_texto


'''Redução para raiz'''
raiz = []
stemmer = nltk.stem.RSLPStemmer()
for y in limpar_texto:
    raiz.append(stemmer.stem(y))
raiz

'''Rotulando'''
tokens = nltk.pos_tag(limpar_texto)
tokens
