# DriedPotato

DriedPotato は、チームの欲しいを管理するアプリケーションです。

## 動作環境

- Python 3.10+
- Django 5.0.x
- django-mathfilters
- asgiref
- sqlparse

## 初期設定

### 必要なパッケージのインストール

Python のインストールについては、省略します。

Python がインストール出来たら、以下のコマンドで必要なパッケージをインストールします。
	
```
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

### データベースの設定

[DriedPotato/settings.py](DriedPotato/settings.py) の `DATABASES` を編集します。

細部は、[データベース | Django ドキュメント | Django](https://docs.djangoproject.com/ja/5.0/ref/databases/)を参照してください。

### データベースへのテーブル作成

以下のコマンドを実行します。

```
$ python manage.py migrate
```

### 管理ユーザーの作成

以下のコマンドを実行し、ユーザー名、メールアドレス、パスワードを設定します。

```
$ python manage.py createsuperuser
```

## 開発サーバーの起動

お試しで動作させたいなら、開発サーバーを起動するのが簡単です。

```
$ python manage.py runserver
```

オプションを指定しない場合、[http://127.0.0.1:8000/](http://127.0.0.1:8000/)でアプリケーションを表示できます。

管理サイトにアクセスする場合は、[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)にアクセスしてください。

## 管理サイトでの準備

- スタッフユーザー、一般ユーザーの作成
- 欲しいものの分類（Item categorys）の追加

### 各ユーザーの役割について

| 種別 | 役割 |
| ---- | ---- |
| 管理ユーザー | ユーザー管理、欲しいものの分類管理 |
| スタッフユーザー | 欲しいものの優先度変更、承認業務 |
| 一般ユーザー | 欲しいものの登録、欲しいものへのコメント |


## 運用環境へのデプロイ

運用環境へのデプロイについては、[Djangoをデプロイするには | Django ドキュメント | Django](https://docs.djangoproject.com/ja/5.0/howto/deployment/)を参照してください。
