#FIFTH (part2)
#procedure with 3 inputs: index (a list), url ( a string) and the content of the page (string)

def add_page_to_index(index, url, content):
    words = content.split() #used the building procedure of python to split the content of the page into keyword by splitting at spaces
    for word in words:
        add_to_index(index, word, url)

#FIFTH (part 1)
#procedure as inputs: an index, a keyword: a string that we want to add to the index, URL: a string that encodes the url where that keyword appears

def add_to_index(index, keyword, url):
    if keyword in index: #index in a dictionary
        for element in index[keyword]:
            if element == url:#url already in the list associated with keyword, no need to add the url
                return
            else:
                index[keyword].append(url) #add new url matching the keyword
    else: 
         #not found, add new keyword to index
        index[keyword] = [url]