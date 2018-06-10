# narou-GetUsersTitle
「小説家になろう」に投稿されている小説のタイトルをユーザ単位で取得します．

# 概要
[なろう小説API](http://dev.syosetu.com/man/api/)を用いることで，「小説家になろう」に投稿されている小説の情報を取得することが可能です．  
このプログラムでは，なろう小説APIを利用して，「小説家になろう」に投稿されている小説のタイトルを取得することができます．  
小説家になろうAPIは，各条件に対して情報が取得できる小説の上限数が2000件のため，このプログラムではユーザ単位で小説の情報を取得しています．　　

# 使用方法
## 設定
config.pyの内容を書き換えることによって，小説のタイトルを取得するユーザの範囲や，情報を取得する時間間隔などを設定できます．  
ユーザの範囲指定は，取得を開始するユーザのIDと終了するユーザのIDを指定することで設定が可能です．

## 実行
GetTitle.pyを実行することで，タイトルの取得を開始します．
```
python GetTitle.py
```
デフォルトでは，title.txtにタイトルデータが書き出され，log.txtにログが表示されます．

# 制限
現在(2018/06/10)，なろう小説APIの利用制限は休止しているようですが，本来の制限として，  
１日あたり，
  
* 利用上限80,000
* 転送量上限400MByte

です．  
  
詳しくは[なろう小説API](http://dev.syosetu.com/man/api/)の利用制限の項目を確認してください．
