# Q1 — AI / Human 文章偵測器 (AI Detector)

**GitHub Repository:** [https://github.com/XiaoYu0503/HomeWork5](https://github.com/XiaoYu0503/HomeWork5)

這是一個基於 Streamlit 和 Hugging Face Transformers 的簡單 AI 文章偵測工具。它使用預訓練模型來分析輸入文本是人類撰寫還是 AI 生成的可能性。

## 功能
- 輸入文本進行即時分析
- 顯示 AI 與 Human 的機率分佈
- 簡單直觀的 UI

## 安裝與執行

### 1. 安裝依賴套件
請確保您已安裝 Python (建議 3.8+)，然後執行以下指令安裝所需套件：

```bash
pip install -r requirements.txt
```

### 2. 執行 Streamlit 應用程式
在終端機中執行以下指令啟動應用程式：

```bash
streamlit run app.py
```

啟動後，瀏覽器應會自動開啟 `http://localhost:8501`。

## 部署至 Streamlit Cloud
1. 將此專案上傳至 GitHub Repository。
2. 前往 [Streamlit Cloud](https://streamlit.io/cloud)。
3. 連結您的 GitHub 帳號並選擇此 Repository。
4. 設定 Main file path 為 `app.py`。
5. 點擊 Deploy。

## 使用模型
本專案使用 [Hello-SimpleAI/chatgpt-detector-roberta](https://huggingface.co/Hello-SimpleAI/chatgpt-detector-roberta) 模型進行偵測。

## 檔案結構
- `app.py`: 主應用程式程式碼
- `requirements.txt`: 專案依賴列表
- `README.md`: 說明文件
- `conversation_log.md`: 開發過程對話紀錄
