import json
import math as mt

class ScoreFuction:

    
    def query_vectore(query,id_documents,inverted_index):
        query_vectore={}
        for term in query:
            try:
                query_vectore[term]=(1+mt.log10(query.count(term)))*(mt.log10(len(id_documents)/len(inverted_index[term])))
            except:
                continue
        return query_vectore

    
    def cosine_Similarity(documents_list,query,query_vectore):
        with open('documents_tfidf.json', 'r') as openfile:
            documents_weight=json.load(openfile)
        results={}
        for id in documents_list:
            score=0
            for term in query:
                try: 
                    score+=query_vectore[term]*documents_weight[str(id)][term]
                except KeyError:
                    continue

            results[id]=round(score,4)
        ranked_document = sorted(results.items(), key=lambda x: x[1], reverse=True)
        return ranked_document








