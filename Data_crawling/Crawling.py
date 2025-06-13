Sales_all = pd.DataFrame([])
Luxury_Sales = pd.DataFrame([])
Non_Luxury_Sales = pd.DataFrame([])
Rent_all = pd.DataFrame([])

for year in range(112,114,1):
  for season in range(1,5,1):
    url = f"https://plvr.land.moi.gov.tw/DownloadSeason?season={year}S{season}&type=zip&fileName=lvr_landcsv.zip"
    response = requests.get(url)
    with zipfile.ZipFile('lvr_landcsv.zip', mode='r') as zf:
        nameList = zf.namelist()
        for name in nameList:
            zf.extract(name, r'zipfolder')
    path = "/content/zipfolder/a_lvr_land_a.csv"
    df = pd.read_csv(path)
    df = df.drop(0)    #remove the first row(translation of each column)
    Non_Luxury_Sales = pd.concat([Non_Luxury_Sales,df])
    df = df.drop(columns=['主建物面積','附屬建物面積','陽台面積','電梯','移轉編號'])
    Sales_all = pd.concat([Sales_all,df])
