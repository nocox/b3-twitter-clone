# B3Twiiter
> B3研究室Webアプリ(Django)勉強会用のサンプルアプリケーション

## ソースコードの取得と環境構築

#### [ windowsの場合 ]
Anaconda Promptから
```bash
git clone [URL]
cd B3Twitter
python -m venv venv
venv¥Scripts¥activate
(venv) pip install -r requirements.txt
```

#### [ その他 ]
コンソールから
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
(vevn) python manage.py runserver
```
上記のコマンドの実行後、ブラウザのURLに以下のアドレスを入力
> http://localhost:8080


## 学習方法
1. Tutorial_1.md を読みながら、Djangoの処理の流れを確認
2. Tutorial_2.md で機能を追加する課題で実装方法を確認
3. 自分で考えた機能を追加してみる
4. docディレクトリからその他の技術を確認

※ 4に関しては、順次追加します
