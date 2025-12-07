# AI Agent 開發對話紀錄

**日期:** 2025年12月7日
**專案:** HW5 - Q1 AI / Human 文章偵測器
**Agent:** GitHub Copilot (Gemini 3 Pro Preview)

## 1. 需求分析
**User:**
請幫我設計 HW5 的 Q1 — AI / Human 文章偵測器。
需求包含：
- 輸入文本 -> 顯示 AI% / Human%
- 使用 Streamlit UI
- 可採用 sklearn / transformers
- 需附上 GitHub 和 Streamlit Demo 連結

**Agent (思考過程):**
- 用戶需要一個快速可用的 AI 偵測器 demo。
- 考慮到準確度與實作難度，使用 Hugging Face 的 `transformers` 搭配現成的預訓練模型是最快且效果不錯的方案。
- 模型選擇：`Hello-SimpleAI/chatgpt-detector-roberta` 是一個常見且針對 ChatGPT 優化的模型，適合此題目。
- UI 框架：Streamlit 是最適合快速建立數據應用程式的工具。

## 2. 專案結構規劃
**Agent:**
我將建立以下檔案結構：
- `Q1_AI_Detector/`
    - `app.py`: Streamlit 主程式
    - `requirements.txt`: 依賴套件
    - `README.md`: 說明文件

## 3. 程式碼實作

### 3.1 建立依賴列表 (requirements.txt)
**Agent:**
首先定義需要的 Python 套件：
```text
streamlit
transformers
torch
scipy
```

### 3.2 開發 Streamlit 應用 (app.py)
**Agent:**
撰寫 `app.py`，主要邏輯如下：
1.  使用 `st.set_page_config` 設定頁面。
2.  使用 `@st.cache_resource` 快取模型載入過程，避免每次互動都重新下載模型。
3.  使用 `transformers.pipeline("text-classification", ...)` 載入 `Hello-SimpleAI/chatgpt-detector-roberta`。
4.  設計 UI：包含標題、側邊欄說明、文字輸入框 (`st.text_area`) 和按鈕。
5.  處理邏輯：當按下按鈕後，呼叫模型進行預測，並解析回傳的 label 和 score。
6.  視覺化：使用 `st.metric` 和 `st.progress` 顯示 AI 與 Human 的機率。

### 3.3 撰寫文件 (README.md)
**Agent:**
提供清楚的安裝與執行步驟，以及如何部署到 Streamlit Cloud 的指引。

## 4. 測試與驗證
**Agent:**
- 確認程式碼無語法錯誤。
- 確認模型名稱正確。
- 確認 Streamlit 的 API 使用正確 (如 `st.cache_resource` 取代舊版的 `st.cache`)。

## 5. 交付
**Agent:**
完成所有檔案建立，並整理在 `Q1_AI_Detector` 資料夾中，供用戶上傳至 GitHub。

## 6. 除錯與優化 (Debug & Refactor)

### 6.1 解決長文本錯誤
**User:**
回報錯誤：`The expanded size of the tensor (833) must match the existing size (514)...`

**Agent:**
- **原因**: 輸入文本長度超過模型限制 (512 tokens)。
- **解法**: 在 `classifier` 呼叫中加入 `truncation=True` 與 `max_length=512` 參數。
- **結果**: 修正 `app.py` 並推送更新。

### 6.2 專案結構重構
**User:**
希望不要將檔案放在 `Q1_AI_Detector` 子資料夾中。

**Agent:**
- 將所有檔案移動至根目錄。
- 更新 `README.md` 連結。
- 刪除空資料夾。
- 提醒用戶更新 Streamlit Cloud 的部署設定 (Main file path)。

### 6.3 文件更新與 PDF 匯出
**User:**
- 請求更新 GitHub 上的 README 內容。
- 詢問如何將對話紀錄匯出成 PDF。
- 要求將最後的對話紀錄也寫入 `conversation_log.md`。

**Agent:**
- 更新 `README.md`：新增功能說明、Demo 連結區塊、以及對話紀錄的連結。
- 提供 PDF 匯出教學：建議使用 VS Code 的 Markdown Preview 列印功能。
- 即時更新 `conversation_log.md`：將上述所有互動過程補齊至文件中，確保紀錄完整。
