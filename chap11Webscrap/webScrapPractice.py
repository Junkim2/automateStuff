import webbrowser, requests, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s ** %(levelname)s ** %(message)s')
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print(exc)
playFile=open('RomeandJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()