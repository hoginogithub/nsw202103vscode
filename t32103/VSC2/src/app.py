import json, pickle
import pandas as pd
from lightgbm import LGBMRegressor
from flask import Flask, request, jsonify

# 保存したモデルを読み込む
with open("../models/onsen.pkl", "rb") as f:
    model = pickle.load(f)

# 特徴量の一覧を読み込む
with open("../models/feature.txt", "r") as f:
    feature_sequence = json.load(f)

# Flask web appの作成
app = Flask(__name__)

# '/ready' endpoint
# モデルのロード完了
@app.route("/ready")
def http_ready():
    return "READY!"

# 予測を行う'/predict' エンドポイント
@app.route("/predict", methods=["POST"])
def http_predict():
    # JSON bodyからデータを取得する
    request_data = request.get_json()

    # データを配列に変換
    X = pd.DataFrame(request_data["data"])[feature_sequence].values

    # 予測
    preds = model.predict(X)
    pred = [int(s) for s in preds.tolist()]

    # return answers
    return jsonify({
        "predictions": pred
    })

# サーバーの実行
if __name__ == "__main__":
    try:
        app.run(port=8080)
    except Exception as ex:
        print(ex)