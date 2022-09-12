# import libraries 
import nltk
from nltk.stem import PorterStemmer
import re
import csv

class Preprossing:

    def get_stopwords():
        openfile = open('data/stopwords.txt','r')
        stopwords=[]
        for i in range(571):
            word=openfile.readline()
            stopwords.append(word[0:len(word)-1])
        openfile.close()
        return stopwords

    def get_documents():
        openfile=open('data/trec.sample.txt','r')
        data=openfile.read()
        text=re.findall(r': .+',data)
        i=0
        documents={}
        while i<len(text):
            id=re.search(r'\d+',text[i])
            documents[int(id.group(0))]=text[i+1]+text[i+2]
            i+=3
        openfile.close()
        return documents

    def remove_Punctuation(documents):
        for id in documents:
            documents[id]=re.sub(r'\W'," ",documents[id].lower())
        return documents

    def remove_stopwords(documents):
        for i in documents:
            document=''
            words=nltk.word_tokenize(documents[i])
            for j in words:
                if j not in stopwords:
                    document+=' '+j
            documents[i]=document
        return documents
        
    def stemming(documents):
        for i in documents:
            document=''
            words=nltk.word_tokenize(documents[i])
            for j in words:
                document+=' '+PorterStemmer().stem(j)
            documents[i]=document
        return documents


stopwords=Preprossing.get_stopwords()
documents=Preprossing.get_documents()
documents=Preprossing.remove_Punctuation(documents)
documents=Preprossing.remove_stopwords(documents)
documents=Preprossing.stemming(documents)

with open('preprossing.csv','w') as csvfile:
    write=csv.writer(csvfile)
    write.writerow(('id','document'))
    for id in documents:
       write.writerow((id,documents[id]))
    csvfile.close()





