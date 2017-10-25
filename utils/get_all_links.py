def get_next_target(page):
    start_link = page.find('<a href=') #spot url
    if start_link == -1: #reach the end of the page, no url spotted
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote] #extract url from the page
    return url, end_quote


def get_all_links(page):
    links = [] #will be the list containing all the url links of the page
    while True:
        url, endpos = get_next_target(page) #  
        if url: #if not obtain None meaning it is not the end of the page
            links.append(url)
            page = page[endpos:] #advance the scanning of page to the next position by end_quote
        else: #means that get_next_target did not find a link
            break
    return links #return the list containing all the url of the page
