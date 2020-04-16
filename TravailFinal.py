# coding utf-8

import csv

from collections import Counter 



import nltk

import string 

#from nltk.tokenize import word_tokenize 

from nltk.stem import SnowballStemmer 

from nltk.stem import PorterStemmer

from nltk.corpus import stopwords 

path = "Horacio.txt"
file = open(path)
line = csv.reader(file)
next(file)
for line in file: 
 print(line)

 #*TENTATIVE POUR ESSAYER D'IMPRIMER UNE LIGNE SPÉCIFIQUE*

for line in file:
     print(line[2938]) #ERREUR STRING INDEX OUT OF RANGE

     
#for line in file:

	#total += 1

	#print("On a {} produits".format(total)) #READLINE HAS NO ATTRIBUTE DISPLAY

#fr = SnowballStemmer('french')
#racines = [fr.stem(mot) for mot in word_tokenize]
#print(racines)


#*MÉTHODE POUR FAIRE FONCTIONNER SNOWBALL STEMMER TEL QUE VU SUR : https://www.youtube.com/watch?v=p1ccbR2P_xA

#from nltk.tokenize import sent_tokenize, word_tokenize
#def stemSentence(sentence):
     #token_words-word_tokenize(sentence)
     #token_words
     #stem_sentence-[]
     #for word in token_words:
          #stem_sentence.append(porter.stem(word))
          #stem_sentence.append(" ")
     #return "".join(stem_sentence)

     #x=stemSentence(sentence)
     #print(x)


#*CETTE MÉTHODE TEL QUE MONDTRÉ DANS LE COURS NE M'AFFICHAIT QUE LA PREMIÈRE LIGNE DE TEXTE DU DOCUMENT CSV, ALORS J'AI REGARDÉ CECI POUR FAIRE CE QUI SE TROUVE PLUS HAUT : https://www.youtube.com/watch?v=Xi52tx6phRU
#conf = "Horacio.txt"
#f = open(conf)
#interventions = csv.reader(f)
#next(interventions)

 
#*CECI EST UNE TENTATIVE DE TOKENIZATION
#for inter in interventions:
     #tokens = word_tokenize(inter[0-10])
     #print(tokens)
