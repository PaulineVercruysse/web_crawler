def get_page(url):
    try:
        import urllib
        content = urllib.urlopen(url).read()
        return content
    except:
        return ""


