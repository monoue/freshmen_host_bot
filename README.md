# freshmen_host_bot
42 Tokyo の Discord 本科サーバにて、主に「新入生コアタイム」イベントの運営の自動化を担う Bot
## 使用言語
Python
## 機能（7/10 現在。最新の情報は Issues 等にて）
### 実装済み
- イベント開催の通知メッセージの送信
    - コマンド入力による
- ボイスチャンネルへの振り分けの通知
    - 特定のメッセージに特定のリアクションをしたユーザーに対するもの
    - コマンド入力による

### 未実装
- 新入生に対する、新入生ロールの付与
- イベント開催の通知メッセージの送信
    - ロールによるメンションを含める
    - 毎朝定時に自動で送信
- ボイスチャンネルへの振り分けの通知
    - 曜日ごとの開始時刻に、自動で送信
