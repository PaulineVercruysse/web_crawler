# MAIN CODE 

execfile('crawl_web.py')
def lookup():
    index, graph = crawl_web() 
    keyword = raw_input('Enter a keyword ')
    if keyword in index: #keyword present in the index
        print ("the urls associated with the keyword are: {}".format(index[keyword])) #look in the dictionaary the urls for the enter at this keyword
        return index[keyword]
    else: #keyword not present in the index
        print 'this keyword is not in the index'
        return None
lookup()