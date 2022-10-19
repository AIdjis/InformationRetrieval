from utils import Utils
import time

if __name__=="__main__":
    query=''
    while query!='exit()':
        query=str(input('please enter your query:'))
        start_time=time.time()
        if query=='':
            continue
        if query=='exit()':
            continue
        search=Utils()
        results=search.match(query)
        if results ==[]:
            print(f'About'+' '+str(len(results))+' '+'results' +' ' +'('+str(round(time.time()-start_time,3))+' '+ 'seconds'+')' )
            print(f'your search "{query}" did not  match any documents')
        else:
            print(f'About'+' '+str(len(results))+' '+'results' +' ' +'('+str(round(time.time()-start_time,3))+' '+ 'seconds'+')' )
            print(search.match(query))














