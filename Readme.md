# B3Twiiter
> B3Webアプリ勉強会用のサンプルアプリケーション

## 概要
- 画像などを使って説明
- できることを説明


## ソースコードの取得と環境構築
- gitクライアントの用意方法について

#### [ winの場合 ]
Anaconda Promptを起動
```bash
git clone [URL]
cd B3Twitter
python -m venv venv
venv¥Scripts¥activate
(venv) pip install -r requirements.txt
```

#### その他
コンソールを起動
```bash
git clone [URL]
cd B3Twitter
virtualenv venv
source venv/bin/activate
(vevn) pip install -r requirements.txt
```


## ローカル環境で実行
- ローカル環境の意味を説明する？

```bash
(vevn) cd b3twitter
(vevn) python manage.py migrate
(vevn) python manage.py runserver 0.0.0.0:8080
```
上記のコマンドの実行後、ブラウザのURLに以下のアドレスを入力
> http://localhost:8080


## 学習方法
1. Tutorial_1.md を読みながら、Djangoの処理の流れを確認
2. Tutorial_2.md で機能を追加する課題で実装方法を確認
3. 自分で考えた機能を追加してみる
4. docディレクトリから細かい処理の概要を知る

※ 4に関しては、順次追加します
