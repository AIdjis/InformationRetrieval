from booleanretrieval import BooleanSearch,ProximitySearch
from rankedretrieval import ScoreFuction
import json
from nltk.stem import PorterStemmer
import re
import pandas as pd


class Utils:
    id_documents=pd.read_csv('preprossing.csv')['id'].values

    with open('Inverted_Index.json', 'r') as openfile:
            inverted_index=json.load(openfile)

    def get_documents(self,term):
            try:
                return self.inverted_index[term]
            except KeyError:
                return []

    def document_list(query):
        
        documents=Utils.get_documents(Utils,query[0])
        i=1
        while i<len(query):
            documents=BooleanSearch.union(documents,Utils.get_documents(Utils,query[i]))
            i+=1
        return documents

    def query_method(self,query):
        if query in re.findall('#\d+\(\w+,\w+\)',query):
                proximity_query=re.findall('\w+', query)
                return ProximitySearch.proximity_list(Utils.query_prossing(proximity_query[1]),Utils.query_prossing(proximity_query[2]),proximity_query[0],self.inverted_index)
        elif query in re.findall('"\w+ \w+"',query):
                pahrse_query=re.findall('\w+', query)
                return ProximitySearch.proximity_list(Utils.query_prossing(pahrse_query[0]),Utils.query_prossing(pahrse_query[1]),0,self.inverted_index)
        return Utils.get_documents(self,Utils.query_prossing(query))

    def query_prossing(term):
        return PorterStemmer().stem(term)

    def get_stopwords():
        openfile = open('data/stopwords.txt','r')
        stopwords=[]
        for i in range(571):
            word=openfile.readline()
            stopwords.append(word[0:len(word)-1])
        openfile.close()
        return stopwords
        
    def match(self,query):
        if query in re.findall('["\w+ \w+"|#\d+\(\w+,\w+\)|\w]+ [AND|OR|NOT]+ ["\w+ \w+"|#\d+\(\w+,\w+\)+\w]+|"\w+ \w+"|#\d+\(\w+,\w+\)|\w+',query):
            query=re.findall('"\w+ \w+"|#\d+\(\w+,\w+\)|\S+',query)
            
            result=[]
            i=0
            while i<len(query):
                if query[i]=='NOT':
                    result=BooleanSearch.inverse(Utils.query_method(self,query[i+1]),self.id_documents)
                    i+=2
                elif query[i]=='AND' and query[i+1]=='NOT' :
                    result=BooleanSearch.intersection(result,BooleanSearch.inverse(Utils.query_method(self,query[i+2]),self.id_documents))
                    i+=3
                elif query[i]=='AND':
                    result=BooleanSearch.intersection(result,Utils.query_method(self,query[i+1]))
                    i+=2
                elif query[i]=='OR' and query[i+1]=='NOT' :
                    result=BooleanSearch.union(result,BooleanSearch.inverse(Utils.query_method(self,query[i+2]),self.id_documents))
                    i+=3
                elif query[i]=='OR':
                    result=BooleanSearch.union(result,Utils.query_method(self,query[i+1]))
                    i+=2
                else:
                    result=Utils.query_method(self,query[i])
                    
                    i+=1
           
            return result

        else:
            stopwords=Utils.get_stopwords()
            query=re.findall('\S+',query)
            query=[i for i in query if i.lower() not in stopwords]
            query=[PorterStemmer().stem(i) for i in query]
            documents_list=Utils.document_list(query)
            query_vectore=ScoreFuction.query_vectore(query,self.id_documents,self.inverted_index)
            result=ScoreFuction.cosine_Similarity(documents_list,query,query_vectore)
            if len(result)<150:
                return result
            else:
                return result[0:150]

       
        
             
        
        

            

        














    

    

        
        

    
