#FOURTH: MAIN CODE
#crawl_web : input: a seed page; output: an index with a list of all the urls that can be reached by following links starting from the seed page and processing ( keep going as long as there are more pages tocrawl)
#tocrawl is a list of pages left to crawl; start at the beginning with the seed page
#crawled is a list to keep track of all pages that we have crawled
#pages will me moved from tocrawl to crawled after being through procedure get_all_links
# returns index, graph of outlinks
execfile('utils/get_page.py')
execfile('utils/add_page_to_index.py')
execfile('utils/get_all_links.py')
execfile('utils/union.py')

def crawl_web():
    #seed = raw_input('Enter an url ') #if we want for the all web
    print 'crawl_web realised on this url: https://www.udacity.com/cs101x/index.html'
    seed = 'https://www.udacity.com/cs101x/index.html' #url for test
    tocrawl = [seed]
    crawled = []
    index = {} #see what is the index down, start with index empty (empty dictionary)
    graph = {}#produce graph, to see the connection between pages, <url>:[list of pages it links to]
    while tocrawl: #if list empty: interpreted as False; if list not empty: interpreted as True 
        page = tocrawl.pop() #page=variable added to the list of page to crawl
        if page not in crawled: #we do not want to crawl pages that we already crawled
            content = get_page(page) #see upper explanations, get_page(page) as variable to not need web request every time
            add_page_to_index(index, page, content) #building the index (see down)
            outlinks = get_all_links(content) #all links that we find on the page content=get_page(page)
            graph[page] = outlinks #associate with the page that is crawled, the outgoing links from that page
            union(tocrawl, outlinks) #add outlinks, to avoid having duplicate in tocrawl
            crawled.append(page) #keep track of the pages that we have crawled: add page to the list crawled
    return index, graph

#crawl_web() #need to add if we want crawl_web to fonction on its one
