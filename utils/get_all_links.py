def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

#THIRD (part2)
#to keep doing in the procedure get_next_target (by using while True) 
# we know that we are at the end of all of URL in the page when the return is None

def get_all_links(page):
    links = [] #will be the list containing all the url links
    while True:
        url, endpos = get_next_target(page) #endpos correspond to the end_link of the tested link;  
        if url: # to test if we have a URL and not a "None" and if we do not have a value None (it means True)
            links.append(url) #give a list with all the url
            page = page[endpos:] #advance the page to the next position by end_quote
        else: #means that get_next_target did not find a link
            break
    return links #return the list containing all the url of the page
