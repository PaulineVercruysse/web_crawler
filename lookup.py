#SEVENTH
#procedure to respond to query with inputs: an index (see up), a keyword that is search; output: a list of all the urls associated with the keyword. If the keyword is not in the index, the output should be None

execfile('crawl_web.py')
def lookup():
    index, graph = crawl_web() #crawl web is for a precise url
    keyword = raw_input('Enter a keyword ')
    if keyword in index:
        print ("the urls associated with the keyword are: {}".format(index[keyword]))
        return index[keyword]
    else:
        print 'this keyword is not in the index'
        return None
lookup()