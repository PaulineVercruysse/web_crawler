# MAIN CODE

execfile('utils/get_page.py')
execfile('utils/add_page_to_index.py')
execfile('utils/get_all_links.py')
execfile('utils/union.py')

def crawl_web():
    seed = raw_input('Enter an url ') #in case: ask the user for the seed page to crawl
    #print 'crawl_web realised on this url: https://www.udacity.com/cs101x/index.html'
    #seed = 'https://www.udacity.com/cs101x/index.html' #in case: want to have a pre-determined start page
    tocrawl = [seed] #list of pages left to crawl
    crawled = [] #list of pages already crawled
    index = {} #dictionnary to have index urls and keyword
    graph = {}#graphic fro interlinks <url>:[list of pages it links to]
    while tocrawl: #if list empty: False; if list not empty: True 
        page = tocrawl.pop() #page added to the list of page to crawl
        if page not in crawled: #check if page already has been crawled
            content = get_page(page) #get the content of the page as string
            add_page_to_index(index, page, content) #building the index
            outlinks = get_all_links(content) #get all links that are found on the page
            graph[page] = outlinks #associate the page and the outgoing links from that page
            union(tocrawl, outlinks) #add the new outlinks in the pages to crawl
            crawled.append(page) #keep track of the pages that we have crawled: the url of the page that just has been crawled move from tocrawl to crawled
    return index, graph

#crawl_web() #need to add if we want crawl_web to fonction on its one
