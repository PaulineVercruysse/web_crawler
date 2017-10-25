Do your own web seacrh engine
===================


----------
A **web search engine** programmed through the help of online class of Udacity "[Intro to computer science](https://www.udacity.com/course/intro-to-computer-science--cs101)".

**IMPORTANT: the web crawler is not taking the politeness policy into the code.** The code should be modified to interger politness policy before using on the web.

### Principles
A web search engine is based on a **web crawler** and a **search tool**. The web crawler will **browse the web** (in this project: starting from a precise url).  During browsing internet, a index is built linking keywords and the urls where they appears. The search tool will allow, after the browsing, to **return the urls associated with the searched keyword**.

----------

Code
-------------

#### **MAIN CODE**: the web crawler
The main code for craling the web is `crawl_web`. 

From a seed url asked by the user or by default, the content of the page as a string is obtained by `get_page`. By the procedure `add_page_to_index`, the page (a string) will be splitted into small words, which will be added as keywords into a index and the current url will be associated with the keywords found. In addition, the urls expressed on the current page (outlinks) will be extracted by `get_all_links`. To keep crawling from one page to others, with the procedure `union`, the new outlinks will be at theirself also go into the procedure of crawling, get content, keywords and urls. To avoid crawling pages that were already crawled, 2 list ( `tocrawl` and `crawled`) will be used. During the `crawl_web` procedure a graphic showing all the interlinks will be contrusct and could be used in case of use of ranking pages (not included in this code).

The output of this procedure is an index with a list of all the urls where the keywords can be found. Another output is a graph representing all the oulinks that can be reached from each crawled page.

#### **MAIN CODE**: the lookup of the index
The main code to be able to look for urls associated with a keyword is `lookup`. This procedure include the procedure of `crawl_web` to build the index. 

`lookup` ask the user for a keyword. A list of urls where the keyword can be found is returned as output. There is no favorite or specific order for the returned urls.

#### **UTILS**

##### `get_page`
This procedure allows to obtain the contain of a html page as a string, given an url. The url has been previously obtained by the user in `crawl_web`. 
This procedure is based on Python module `urllib.request` for fetching URLs.

##### `add_page_to_index`
The procedure `add_page_to_index` construct the index of keyword with the list of urls associated. This procedure also use the procedure `add_to_index`.

`add_page_to_index` use the Python module `content.split` to split the content of the page (string) into small words. The spliting is realised at each space.
The procedure `add_to_index` will allowed to add the new words as keyword and to associated with it the current url of the page. If the word is already present as keyword in the index, the procedure check if the current url is already associated with the keyword. If it is not the case, the url of the current page will be added at the list of associated urls of the keyword.

##### `get_all_links`
The procedure `get_all_links` extract all the urls present on the current page. In this way, from the current page, we obtain the new urls which will be crawled. `get_all_links` also use the procedure `get_next_target`.

With `get_next_target` the current page, present as a string, is scanned to look for urls. The string `'<a href='` is the way to find where are located the url, then the url is extracted after this text until (`end_quote + 1`). With the `while` loop of `get_all_links`, the scanning is shift after this url and the procedure of scanning of `get_next_target` continue for the rest of the page. All the urls present in the current pages are returned as a list called `links`.

##### `union`
The small procedure `union` transfer all the returned `links` of `get_all_links` from the curent page (all the urls present in the current page) into `tocrawl`. Thus the urls present on the current page will be at their turn being crawled.

 




