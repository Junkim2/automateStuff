import requests, bs4, sys, webbrowser

print('Googling....')
# res = requests.get('http://google.co.kr/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('http://google.co.kr/search?q=' + '헬로월드')
try:
    res.raise_for_status()
except Exception as e:
    print(e)

#Todo: retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

#Todo: open a browser tab for each result.
linkElems = soup.select('.r a')
print(linkElems)
print(linkElems[0].get('href'))
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     webbrowser.open('http://google.co.kr/search?q=' + linkElems[i].get('href'))