import zipfile
from zipfile import ZipFile
url = "https://plvr.land.moi.gov.tw/DownloadSeason?season=114S1&type=zip&fileName=lvr_landcsv.zip"
response = requests.get(url)
with zipfile.ZipFile('lvr_landcsv.zip', mode='r') as zf:
    nameList = zf.namelist()
    for name in nameList:
        zf.extract(name, r'zipfolder', pwd='123'.encode('utf-8'))
