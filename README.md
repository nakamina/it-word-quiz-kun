# IT 単語クイズくん🐶

IT 初心者が抑えるべき単語を元にクイズを出します。

![](https://github.com/nakamina/nakamina/assets/122137298/8ae4c976-eff9-4841-86e2-c5ea601c709d)

- pyenv と pyenv-virtualenv を使用します

```shell
cd /path/to/it-word-quiz-kun
pyenv virtualenv 3.9.9 it-word-quiz-kun
pyenv local it-word-quiz-kun

pip install -U pip setuptools wheel poetry
```
- poetryを使用して依存ライブラリをインストールします

```shell
poetry install
```

## 動かし方

```shell
streamlit run main.py

#
# http://localhost:8501/ にアクセスして下さい
#
```