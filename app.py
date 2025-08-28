import streamlit as st
import time
import random

def initialize_session_state():
    """チャットの履歴を初期化"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def get_bot_response(user_message):
    """シンプルなボットの応答を生成"""
    responses = [
        f"「{user_message}」について興味深いですね！",
        "それはとても良い質問ですね。",
        "なるほど、もう少し詳しく教えていただけますか？",
        "それについてどう思われますか？",
        f"「{user_message}」に関して、私も同じように考えています。",
        "とても面白い観点ですね！",
        "それは素晴らしいアイデアだと思います。",
    ]
    
    # ランダムに応答を選択
    response = random.choice(responses)
    
    # より自然な応答のために少し遅延を追加
    time.sleep(1)
    
    return response

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