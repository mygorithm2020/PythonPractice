# from selenium import webdriver
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://apply.lh.or.kr/lhapply/apply/wt/wrtanc/selectWrtancInfo.do"
req = Request(url,headers={'User-Agent':'Mozila/5.0'})
webpage = urlopen(req)
soup = BeautifulSoup(webpage)
print(soup)
#