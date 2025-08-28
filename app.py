import streamlit as st
import time
import os
from anthropic import Anthropic

def initialize_session_state():
    """チャットの履歴を初期化"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def get_bot_response(user_message):
    """Claude APIを使用してボットの応答を生成"""
    try:
        # 環境変数からAPIキーを取得
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            return "⚠️ APIキーが設定されていません。Streamlit Cloudの環境変数でANTHROPIC_API_KEYを設定してください。"
        
        # Anthropic clientを初期化
        client = Anthropic(api_key=api_key)
        
        # Claude APIに送信
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.7,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        return message.content[0].text
        
    except Exception as e:
        return f"⚠️ エラーが発生しました: {str(e)}"

def main():
    st.set_page_config(
        page_title="Claude Streamlit チャットボット",
        page_icon="🤖",
        layout="wide"
    )
    
    # セッション状態を初期化（最初に実行）
    initialize_session_state()
    
    st.title("🤖 Claude Streamlit チャットボット")
    st.markdown("---")
    
    # サイドバーに設定オプション
    with st.sidebar:
        st.header("⚙️ 設定")
        
        # チャット履歴をクリア
        if st.button("チャット履歴をクリア"):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()
        
        # ボットの設定
        st.subheader("ボット設定")
        bot_name = st.text_input("ボットの名前", value="Claude Bot")
        
        # 統計情報
        st.subheader("📊 統計")
        if st.session_state.messages:
            total_messages = len(st.session_state.messages)
            user_messages = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
            bot_messages = len([msg for msg in st.session_state.messages if msg["role"] == "assistant"])
            
            st.metric("総メッセージ数", total_messages)
            st.metric("ユーザーメッセージ", user_messages)
            st.metric("ボットメッセージ", bot_messages)
    
    # チャット履歴を表示
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # ユーザー入力
    if prompt := st.chat_input("メッセージを入力してください..."):
        # ユーザーメッセージを追加
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # ボットの応答を生成
        with st.chat_message("assistant"):
            with st.spinner(f"{bot_name}が応答を考えています..."):
                response = get_bot_response(prompt)
            st.markdown(response)
        
        # ボットの応答をセッション状態に追加
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # 使用方法の説明
    with st.expander("📖 使用方法"):
        st.markdown("""
        ### チャットボットの使用方法
        
        1. **メッセージを送信**: 下部のテキストボックスにメッセージを入力してEnterキーを押すか、送信ボタンをクリック
        2. **チャット履歴**: 会話の履歴が画面に表示されます
        3. **履歴のクリア**: サイドバーの「チャット履歴をクリア」ボタンで履歴を削除
        4. **統計情報**: サイドバーでチャットの統計を確認
        
        ### 機能
        - 📝 リアルタイムチャット
        - 💾 チャット履歴の保存
        - 📊 統計情報の表示
        - 🗑️ 履歴のクリア機能
        - ⚙️ ボット名のカスタマイズ
        """)

if __name__ == "__main__":
    main()