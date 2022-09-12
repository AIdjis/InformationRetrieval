import json
import math as mt
import pandas as pd

class TfIdf:
    def term_fequency():
        with open('proximity_Index.json', 'r') as openfile:
            proximity_index=json.load(openfile)
        term_fequency={}
        for term in proximity_index:
            document={}
            for i in proximity_index[term]:
                document[i]=len(proximity_index[term][str(i)])
            term_fequency[term]=document
        return term_fequency
        
    def document_fequency():
        with open('Inverted_Index.json', 'r') as openfile:
            inverted_index=json.load(openfile)
        document_fequency={}
        for term in inverted_index:
            document_fequency[term]=len(inverted_index[term])
        return document_fequency
    
    def normalization(document):
        result=0
        for i in document:
            result+=mt.pow(document[i],2)
        return mt.sqrt(result)

    def weigth_tfidf(document_fequency,term_fequency):
        with open('Inverted_Index.json', 'r') as openfile:
            inverted_index=json.load(openfile)
        vectors={}
        id=pd.read_csv('preprossing.csv')['id'].values
        for document in id:
            wiegth={}
            for term in document_fequency:
                if document in inverted_index[term]:
                    tf_idf=(1+mt.log10(term_fequency[term][str(document)]))*(mt.log10(len(id)/document_fequency[term]))
                    wiegth[term]=tf_idf
            for term in wiegth:
                wiegth[term]=round(wiegth[term]/TfIdf.normalization(wiegth),4)

            vectors[str(document)]=wiegth
        return (vectors)

   

term_fequency=TfIdf.term_fequency()
document_fequency=TfIdf.document_fequency()
vectors=TfIdf.weigth_tfidf(document_fequency,term_fequency)


documents_tfidf= json.dumps(vectors)
with open("documents_tfidf.json", "w") as outfile:
    outfile.write(documents_tfidf)