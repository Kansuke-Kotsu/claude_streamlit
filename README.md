# Claude Streamlit チャットボット 🤖

Streamlitを使用したシンプルなチャットボットアプリケーションです。

## 機能

- 📝 リアルタイムチャット機能
- 💾 チャット履歴の自動保存
- 📊 チャット統計の表示
- 🗑️ チャット履歴のクリア機能
- ⚙️ ボット名のカスタマイズ
- 🎨 美しいUIデザイン

## セットアップ

### 必要な要件

- Python 3.7以上
- pip

### インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/Kansuke-Kotsu/claude_streamlit.git
cd claude_streamlit
```

2. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

## 使用方法

### アプリケーションの起動

```bash
streamlit run app.py
```

アプリケーションが起動すると、ブラウザで `http://localhost:8501` が自動的に開きます。

### チャットボットの使用

1. **メッセージを送信**: 画面下部のテキストボックスにメッセージを入力してEnterキーを押す
2. **チャット履歴**: 会話の履歴が自動的に画面に表示される
3. **設定**: サイドバーからボットの名前を変更したり、統計情報を確認
4. **履歴クリア**: サイドバーの「チャット履歴をクリア」ボタンで会話をリセット

## カスタマイズ

### ボットの応答をカスタマイズ

`app.py`の`get_bot_response`関数を編集することで、ボットの応答をカスタマイズできます。

```python
def get_bot_response(user_message):
    # ここに独自のロジックを追加
    responses = [
        "カスタム応答1",
        "カスタム応答2",
        # 応答を追加...
    ]
    return random.choice(responses)
```

### UIのカスタマイズ

Streamlitの設定やスタイルを変更することで、UIをカスタマイズできます。

## 開発

### 開発環境のセットアップ

```bash
# 開発用依存関係のインストール（将来の拡張用）
pip install -r requirements.txt

# アプリケーションを開発モードで実行
streamlit run app.py --server.runOnSave true
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

プルリクエストやイシューを歓迎します！

## サポート

何か問題があれば、GitHubのIssuesページでお知らせください。