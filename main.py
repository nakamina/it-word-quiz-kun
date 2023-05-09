import random
from typing import Dict, Final

import streamlit as st

QUESTIONS: Final[Dict[str, str]] = {
    "どの通信も信頼できないという前提で検査する": "ゼロトラスト",
    "端末側で処理してサーバーの負荷や遅延を減らす": "エッジコンピューティング",
    "難問を解くことを期待されているコンピュータ": "量子コンピュータ",
    "データやデジタル技術で企業のビジネスモデルを変革する": "DX",
    "携帯電話での第5世代の無線通信技術": "5G",
    "人工知能の能力が人間を超えるという仮説": "シンギュラリティ",
    # "事務処理等の業務を自動化する": "RPA",
    # "低消費電力で長距離の通信を実現した無線通信技術": "LPWA",
    # "LTEの空いた帯域を使用するIoT通信規格": "LTE-M",
    # "新世代のネットワーク基盤": "NGN",
    # "LANと同じ方法でインターネットに接続する接続方法": "IPoE",
    # "ITを活用してあらゆる交通機関を統合して利用": "MaaS",
    # "1台でシンプルなサーバー構成を実現できるインフラ製品": "HCI",
    # "複数の小さなサービスに分割してアプリケーションを構成": "マイクロサービス",
    # "分散型ネットワークと暗号技術を使ったデータ管理手法": "ブロックチェーン",
}


def main():
    # # 問題をシャッフルする
    # questions_items = list(QUESTIONS.items())
    # random.shuffle(questions_items)

    st.title("IT 単語クイズくん🐶")

    num_correct = 0

    for question, answer in QUESTIONS.items():
        user_answer = st.text_input(label=question, value="")
        if user_answer == answer:
            num_correct += 1

    if st.button("解答"):
        score = int((num_correct / len(QUESTIONS)) * 100)
        st.markdown(f"## あなたのスコアは {score} 点です")
        if score <= 50:
            st.markdown("### :blue[残念！もう少し勉強しましょう🐶]")
        elif 50 < score < 80:
            st.markdown("### :green[覚えてきましたね。あともう少し！🐶]")
        elif 80 <= score < 100:
            st.markdown("### :orange[素晴らしい！あともう少しで満点です！🐶]")
        else:
            st.markdown("# :red[🌸🌸 満点です 🌸🌸]")


if __name__ == "__main__":
    main()
