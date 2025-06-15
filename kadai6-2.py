import requests
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json"
response = requests.get(url)
data = response.json()

time_series = data[0]["timeSeries"][0]

for area in time_series["areas"]:
    if area["area"]["name"] == "北西部":
        print("千葉北西部の天気予報")
        for date, weather in zip(time_series["timeDefines"], area["weathers"]):
            print(f"{date} の天気：{weather}")
# 気象庁 天気予報データ
# エンドポイント：https://www.jma.go.jp/bosai/forecast/data/forecast
# 機能　今日、明日、明後日の天気を確認できる
# 使い方　地域コードを入れることで天気を表示できる 例）千葉県＝120000
