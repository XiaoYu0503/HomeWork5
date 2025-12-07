import streamlit as st
from transformers import pipeline

# 設定頁面配置
st.set_page_config(
    page_title="AI / Human 文章偵測器",
    page_icon="🤖",
    layout="centered"
)

# 標題與說明
st.title("🤖 AI / Human 文章偵測器")
st.markdown("""
這是一個簡單的 AI vs Human 文章分類工具。
請在下方輸入一段英文文本，模型將會判斷這段文字是由 **AI (如 ChatGPT)** 生成的，還是由 **人類** 撰寫的。
""")

# 側邊欄資訊
with st.sidebar:
    st.header("關於")
    st.markdown("""
    此工具使用 Hugging Face 的 Transformers 庫與預訓練模型進行偵測。
    
    **使用模型:** `Hello-SimpleAI/chatgpt-detector-roberta`
    
    **注意:** AI 偵測器並非 100% 準確，結果僅供參考。
    """)

# 載入模型 (使用 st.cache_resource 避免重複載入)
@st.cache_resource
def load_pipeline():
    # 使用 Hello-SimpleAI/chatgpt-detector-roberta 模型
    # 這個模型專門用於偵測 ChatGPT 生成的文本
    return pipeline("text-classification", model="Hello-SimpleAI/chatgpt-detector-roberta")

# 初始化模型
try:
    classifier = load_pipeline()
    model_loaded = True
except Exception as e:
    st.error(f"模型載入失敗: {e}")
    model_loaded = False

# 用戶輸入區
user_input = st.text_area("請輸入要分析的文本 (建議 50 字以上):", height=200, placeholder="Paste your text here...")

# 分析按鈕
if st.button("開始分析", type="primary"):
    if not user_input.strip():
        st.warning("請輸入有效的文本內容！")
    elif not model_loaded:
        st.error("模型尚未準備好，請稍後再試。")
    else:
        with st.spinner("正在分析中..."):
            # 進行預測
            # 由於 pipeline 預設只返回最高分的 label，我們需要所有 scores 來顯示百分比
            # 但 text-classification pipeline 預設行為可能不同，這裡我們直接用預設並解析
            # 為了獲取所有標籤的分數，我們可以使用 return_all_scores=True (舊版) 或 top_k=None (新版)
            try:
                results = classifier(user_input, top_k=None)
                # results 是一個 list of list of dicts, e.g., [[{'label': 'ChatGPT', 'score': 0.9}, {'label': 'Human', 'score': 0.1}]]
                
                # 解析結果
                scores = {item['label']: item['score'] for item in results}
                
                # 假設模型標籤為 'ChatGPT' 和 'Human' (需視具體模型而定，此模型通常是這兩個)
                # 如果標籤不同，這裡可能需要調整
                ai_score = scores.get('ChatGPT', 0.0)
                human_score = scores.get('Human', 0.0)
                
                # 如果模型標籤是 Label_0 / Label_1，則需要映射 (通常 Label_1 是 AI)
                # 為了保險，如果找不到 key，我們印出 raw data 供除錯 (在實際 app 中可以隱藏)
                if 'ChatGPT' not in scores and 'Human' not in scores:
                    # 嘗試自動判斷 (假設較高的那個是 AI? 不，這不安全)
                    # 針對 Hello-SimpleAI/chatgpt-detector-roberta，標籤確實是 'ChatGPT' 和 'Human'
                    pass

                # 顯示結果
                st.subheader("分析結果")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("AI 生成機率", f"{ai_score:.2%}")
                    st.progress(ai_score)
                
                with col2:
                    st.metric("人類撰寫機率", f"{human_score:.2%}")
                    st.progress(human_score)
                
                # 最終判斷
                if ai_score > 0.5:
                    st.error(f"⚠️ 判斷結果: **AI 生成** (信心度: {ai_score:.2%})")
                else:
                    st.success(f"✅ 判斷結果: **人類撰寫** (信心度: {human_score:.2%})")
                    
            except Exception as e:
                st.error(f"分析過程中發生錯誤: {e}")

# 頁尾
st.markdown("---")
st.caption("HW5 - Advanced Topic | Q1 AI Detector Demo | [GitHub Repository](https://github.com/XiaoYu0503/HomeWork5)")
