import requests, bs4, logging

logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format=('%(asctime)s    %(level)s    %(message)s'))
exampleFile = open('example.html')
exampleBS = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleBS.select('#author')
pElems = exampleBS.select('p')
print(pElems[0].getText())      # 엘리먼트가 제거 된 Value text만 받을 수 있다.
print(str(pElems[0]))           # 엘리먼트를 포함, HTML에 그대로 입력 된 텍스트를 가져올 수 있다.
print(elems[0].attrs)           # 셀렉터를id로 넣은경우 id:선택자를 딕셔너리 형태로 받을 수 있다.
pElems0 = exampleBS.select('p')[0]
