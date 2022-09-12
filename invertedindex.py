import pandas as pd
import numpy as np
import json



class InvertedIndex:
   
    def word_list(list):
        corpus=''
        for i in list:
            corpus+=i
        return set(corpus.split())

    def document_list(id,document):
        id =[int(i) for i in id]
        document=[i.split() for i in document]
        return dict(zip(id,document))
    
    def indexing(words,documents):
        index={}
        for term in words:
            document=[]
            for id in documents:
                if list(documents[id]).count(term)>0:
                    document.append(id)
            index[term]=document
        return index

    def position(index,documents):
        position_list={}
        for term in index:
            position={}
            for id in index[term]:
                document_word=np.array(documents[id])
                positions=np.where(document_word==term)
                positions =[int(i) for i in positions[0]]
                position[id]=list(positions)
                position_list[term]=position
        return position_list


data=pd.read_csv('preprossing.csv')

documents=data['document'].values
id=data['id'].values

words=InvertedIndex.word_list(set(documents))
documents=InvertedIndex.document_list(id,list(documents))
index=InvertedIndex.indexing(words,documents)
positional_index=InvertedIndex.position(index,documents)


inverted_index = json.dumps(index)
with open("Inverted_Index.json", "w") as outfile:
    outfile.write(inverted_index)

proximity_index = json.dumps(positional_index)
with open("Proximity_Index.json", "w") as outfile:
    outfile.write(proximity_index)
    