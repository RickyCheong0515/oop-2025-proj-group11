Sales_all = pd.DataFrame([])
Luxury_Sales = pd.DataFrame([])
Non_Luxury_Sales = pd.DataFrame([])
Rent_all = pd.DataFrame([])

for year in range(101,114,1):
  for season in range(1,5,1):
    url = f"https://plvr.land.moi.gov.tw/DownloadSeason?season={year}S{season}&type=zip&fileName=lvr_landcsv.zip"
    response = requests.get(url)
    with zipfile.ZipFile('lvr_landcsv.zip', mode='r') as zf:
        nameList = zf.namelist()
        for name in nameList:
            zf.extract(name, r'zipfolder')
    #Get the Normal sales
    path = "/content/zipfolder/a_lvr_land_a.csv"
    df = pd.read_csv(path)
    df = df.drop(0)    #remove the first row(translation of each column)
    Non_Luxury_Sales = pd.concat([Non_Luxury_Sales,df])
    df = df.drop(columns=['主建物面積', '附屬建物面積', '陽台面積', '電梯', '移轉編號'])    #remove the no duplicates terms
    Sales_all = pd.concat([Sales_all,df])
    #Get the Luxury sales
    path = "/content/zipfolder/a_lvr_land_b.csv"
    df = pd.read_csv(path)
    df = df.drop(0)    #remove the first row(translation of each column)
    Luxury_Sales = pd.concat([Luxury_Sales,df])
    df = df.drop(columns=['建案名稱', '棟及號', '解約情形'])    #remove the no duplicates terms
    Sales_all = pd.concat([Sales_all,df])
    #Get the Rent
    path = "/content/zipfolder/a_lvr_land_c.csv"
    df = pd.read_csv(path)
    df = df.drop(0)    #remove the first row(translation of each column)
    Rent_all = pd.concat([Rent_all,df])

date = Sales_all['交易年月日']
for i in range(len(date)):
  date.iloc[i] = datetime.date(int(date.iloc[i][:3])+1911, int(date.iloc[i][3:5]), int(date.iloc[i][5:]))
Sales_all['交易年月日'] = date

date = Luxury_Sales['交易年月日']
for i in range(len(date)):
  date.iloc[i] = datetime.date(int(date.iloc[i][:3])+1911, int(date.iloc[i][3:5]), int(date.iloc[i][5:]))
Luxury_Sales['交易年月日'] = date

date = Non_Luxury_Sales['交易年月日']
for i in range(len(date)):
  date.iloc[i] = datetime.date(int(date.iloc[i][:3])+1911, int(date.iloc[i][3:5]), int(date.iloc[i][5:]))
Non_Luxury_Sales['交易年月日'] = date
