# @Author Yichen
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def make_soup(url):
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    thepage = urlopen(req).read()
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

def get_info(name):
    name_list = name.split()
    pre_url = "https://www.truepeoplesearch.com/results?name="
    url = pre_url + name_list[0] + "%20" + name_list[1]
    print("This is the first page of results for "+ name)
    print(url)
    soup = make_soup(url)
    print(soup.get_text()) #We can also use print(soup.prettyify())

get_info("Joe Smith")
get_info("John Smith")
get_info("Amy Smith")
get_info("Jeff Smith")
get_info("Matt Smith")