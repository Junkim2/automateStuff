import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('jun', exist_ok=True) #jun이라는 폴더를 만들고 이미 있는 경우 pass한다.
while not url.endswith('#'):      #.endswith('text') < text로 끝나지 않는 경우.
    #Todo: download the page.
    res = requests.get(url)                 #url을 다운로드받아 객체로 저장한다.
    res.raise_for_status()                  #res객체에 문제가 있는경우 오류를 내보내고 프로그램을 중단시킨다.
    soup = bs4.BeautifulSoup(res.text)      #res를 텍스트화 후 bs4 모듈을 통해 HTML 구문 텍스트를 soup에 저장한다.
    comicElem = soup.select('#comic img')   #Beatuifulsoup로 떠낸 객체에 .select('엘리먼트')는 해당 엘리먼트가 포함 된 구문들을 리스트로 반환한다.
    if comicElem == []:
        print('Nothing to download')
    else:
        comicUrl=comicElem[0].get('src')    # comic이라는 아이디를 쓰고 img라는 엘리먼트를 가진 HTML구문들 중 src의 속성을 가진 값을 추출한다.
        res = requests.get(comicUrl)        # comicUrl 주소에서 다운받는다.
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        #imageFile이라는 파일을 생성하며 그 파일이 생성 될 경로를 지정한다.
        #os.path.join('폴더명','하위파일명') < 방식으로 만들 것인데 이 때 파일명을 comicUrl에서 다운로드 받은 파일명으로 저장하기 위해
        #os.path.basename(comicUrl)로 한다. os.path.basename(인자)는 인자 안의 마지막 항목만을 텍스트로 추출해서 반환한다.
        for chunk in res.iter_content(100000):      # 여기서 res는 comicUrl에서 받아온 객체이다.
            imageFile.write()                       # res를 iter_content메소드를 통해 파일화하고, 이것을 imageFile파일에 쓴다.
    prevLink = soup.select('a[rel="prev"]')[0]      # soup로 떠낸 객체에서 a[rel="prev"] 라는 엘리먼트를 가진 객체를 prevLink에 저장한다.
    url = 'http://xkcd.com' + prevLink.get('href')  # prevLink에서 href 속성을 가진 값을 추출하여 url로 만든다.

