from utils import Utils



query=''
while query!='exit()':
    query=str(input('please enter your query:'))
    if query=='':
        continue
    if query=='exit()':
        continue
    if Utils.match(query) ==[]:
        print('no document match this query')
    else:
        print(Utils.match(query))














