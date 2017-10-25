def add_page_to_index(index, url, content):
    words = content.split() #spliting the page as small words
    for word in words:
        add_to_index(index, word, url)

def add_to_index(index, keyword, url):
    #the index is a Python dictionary
    if keyword in index: #the keyword is already present in the index
        for element in index[keyword]:
            if element == url:#url already in the list associated with keyword, no need to add the url
                return
            else:
                index[keyword].append(url) #add new url matching the keyword
    else: 
         #not found, add new keyword to index
        index[keyword] = [url]