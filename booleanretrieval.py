import json


class BooleanSearch:

    def intersection(list1,list2):
        if len(list1)<len(list2):
            return [ i for i in list1 if i  in list2 ]
        else:
            return [ i for i in list2 if i  in list1 ]

    def inverse(list1,id_documents):
        return [ i for i in id_documents if i not in list1 ]
        
    def union(list1,list2):
        if len(list1)<len(list2):
            result=[ i for i in list1 if i not in list2 ]
            result=result+list2
            result.sort()
            return result
        else:
            result=[ i for i in list2 if i not in list1 ]
            result=result+list1
            result.sort()
            return result


class ProximitySearch:

    def position(list1,list2,document_list,size):
        results=[]
        for i in document_list:
            pos=0
            while pos<len(list1[str(i)]):
                j=0
                while j<len(list2[str(i)]):
                    if list2[str(i)][j]-list1[str(i)][pos]-1>=0 and list2[str(i)][j]-list1[str(i)][pos]-1<=int(size):
                        results.append(int(i))
                        j=len(list2[str(i)])
                        pos=len(list1[str(i)])
                    j+=1
                pos+=1
        return results

    def proximity_list(word1,word2,size,inverted_index):
        
 
        document_list=BooleanSearch.intersection(inverted_index[word1],inverted_index[word2])
        
        with open('proximity_index.json', 'r') as openfile:
            proximity_index=json.load(openfile)
        return ProximitySearch.position(proximity_index[word1],proximity_index[word2],document_list,size)