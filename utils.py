from booleanretrieval import BooleanSearch,ProximitySearch
from rankedretrieval import ScoreFuction
import json
from nltk.stem import PorterStemmer
import re
from preprossing import Preprossing



class Utils:
    def get_documents(term):

        with open('Inverted_Index.json', 'r') as openfile:
            inverted_index=json.load(openfile)
            try:
                return inverted_index[term]
            except KeyError:
                return []

    def document_list(query):
        documents=Utils.get_documents(query[0])
        i=1
        while i<len(query):
            documents=BooleanSearch.union(documents,Utils.get_documents(query[i]))
            i+=1
        return documents

    def query_method(query):
        if query in re.findall('#\d+\(\w+,\w+\)',query):
                proximity_query=re.findall('\w+', query)
                return ProximitySearch.proximity_list(Utils.query_prossing(proximity_query[1]),Utils.query_prossing(proximity_query[2]),proximity_query[0])
        elif query in re.findall('"\w+ \w+"',query):
                pahrse_query=re.findall('\w+', query)
                return ProximitySearch.proximity_list(Utils.query_prossing(pahrse_query[0]),Utils.query_prossing(pahrse_query[1]),0)
        return Utils.get_documents(Utils.query_prossing(query))

    def query_prossing(term):
        return PorterStemmer().stem(term)
        
    def match(query):
        if query in re.findall('["\w+ \w+"|#\d+\(\w+,\w+\)|\w]+ [AND|OR|NOT]+ ["\w+ \w+"|#\d+\(\w+,\w+\)+\w]+|"\w+ \w+"|#\d+\(\w+,\w+\)|\w+',query):
            query=re.findall('"\w+ \w+"|#\d+\(\w+,\w+\)|\S+',query)
            
            result=[]
            i=0
            while i<len(query):
                if query[i]=='NOT':
                    result=BooleanSearch.inverse(Utils.query_method(query[i+1]),)
                    i+=2
                elif query[i]=='AND' and query[i+1]=='NOT' :
                    result=BooleanSearch.intersection(result,BooleanSearch.inverse(Utils.query_method(query[i+2])))
                    i+=3
                elif query[i]=='AND':
                    result=BooleanSearch.intersection(result,Utils.query_method(query[i+1]))
                    i+=2
                elif query[i]=='OR' and query[i+1]=='NOT' :
                    result=BooleanSearch.union(result,BooleanSearch.inverse(Utils.query_method(query[i+2])))
                    i+=3
                elif query[i]=='OR':
                    result=BooleanSearch.union(result,Utils.query_method(query[i+1]))
                    i+=2
                else:
                    result=Utils.query_method(query[i])
                    
                    i+=1
           
            return result

        else:
            stopwords=Preprossing.get_stopwords()
            query=re.findall('\S+',query)
            query=[i for i in query if i.lower() not in stopwords]
            query=[PorterStemmer().stem(i) for i in query]
            documents_list=Utils.document_list(query)
            query_vectore=ScoreFuction.query_vectore(query)
            result=ScoreFuction.cosine_Similarity(documents_list,query,query_vectore)
            if len(result)<150:
                return result
            else:
                return result[0:150]

       
        
             
        
        

            

        














    

    

        
        

    
