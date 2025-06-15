import requests

API_ID = "1acabb863bcf389c6297633927544e9b9e6e3eb5"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# パラメータの設定
params = {
    "appId": API_ID,
    "statsDataId": "0003008332",
    "lang": "J"
}

response = requests.get(API_URL, params=params)

data = response.json()
# 結果を表示
result_list = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
for item in result_list[:15]:  # 15件表示
    print(f"年: {item['@time']}, 完全失業率: {item['$']}%")
    
# エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# データの種類:完全紙業率についての年次データ
