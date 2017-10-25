#put all the links got from get_all_links to the list tocrawl

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)
