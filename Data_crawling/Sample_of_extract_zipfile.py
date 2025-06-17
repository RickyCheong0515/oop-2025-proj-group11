import requests
import zipfile
url = "https://plvr.land.moi.gov.tw/DownloadSeason?season=114S1&type=zip&fileName=lvr_landcsv.zip"
response = requests.get(url)
response.raise_for_status()
with open('lvr_landcsv.zip', 'wb') as f:
    f.write(response.content)
with zipfile.ZipFile('lvr_landcsv.zip', mode='r') as zf:
    nameList = zf.namelist()
    for name in nameList:
        zf.extract(name, r'zipfolder', pwd='123'.encode('utf-8'))
