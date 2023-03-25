import random

# 問題と回答のディクショナリ
questions = {
    "どの通信も信頼できないという前提で検査する": "ゼロトラスト",
    "端末側で処理してサーバーの負荷や遅延を減らす": "エッジコンピューティング",
    "難問を解くことを期待されているコンピュータ": "量子コンピュータ",
    "データやデジタル技術で企業のビジネスモデルを変革する": "DX",
    "携帯電話での第5世代の無線通信技術": "5G",
    "人工知能の能力が人間を超えるという仮説": "シンギュラリティ",
    "事務処理等の業務を自動化する": "RPA",
    "低消費電力で長距離の通信を実現した無線通信技術": "LPWA",
    "LTEの空いた帯域を使用するIoT通信規格": "LTE-M",
    "新世代のネットワーク基盤": "NGN",
    "LANと同じ方法でインターネットに接続する接続方法": "IPoE",
    "ITを活用してあらゆる交通機関を統合して利用": "MaaS",
    "1台でシンプルなサーバー構成を実現できるインフラ製品": "HCI",
    "複数の小さなサービスに分割してアプリケーションを構成": "マイクロサービス",
    "分散型ネットワークと暗号技術を使ったデータ管理手法": "ブロックチェーン",
}

# 問題をシャッフルする
questions_items = list(questions.items())
random.shuffle(questions_items)

# クイズを開始する
score = 0
answered_questions = 0
for question, answer in questions_items:
    print(f"Q.{question}")
    user_answer = input("A. ")
    answered_questions += 1

    if user_answer == answer:
        print("正解です！！")
        score += 1
    else:
        print(f"残念！正解は{answer}でした。")
    print("--------------------------------")

    user_input = input("終了しますか？[y/n]")
    if user_input.lower() == "y":
        break

# スコアを表示する
total_score = answered_questions
percentage = int(score / total_score * 100) if total_score > 0 else 0
print(f"あなたのスコアは{score}/{total_score}で、正答率は{percentage}%でした")
