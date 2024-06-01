import streamlit as st
import openai

# OpenAIのAPIキーを設定します
openai.api_key = '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'

st.title('事業計画書作成アプリ')

# ユーザーに入力してもらう10項目
fields = {
    '課題意識': '',
    '目標': '',
    'スタッフ': '',
    '食材確保の方法': '',
    '対象者': '',
    '活動頻度': '',
    '活動場所': '',
    '安全管理方法': '',
    '行っている活動': '',
    '今後の運営方針': ''
}

inputs = {}
for field in fields:
    inputs[field] = st.text_input(field)

if st.button('事業計画書を生成'):
    input_text = '\n'.join([f'{key}: {value}' for key, value in inputs.items()])

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ]
        )

        st.subheader('事業計画書')
        st.write(response['choices'][0]['message']['content'])
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

   
