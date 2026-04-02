import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# 1. 系統設定 (符合 Integ-CRF v9.0 核心命脈區規範)
# ==========================================
st.set_page_config(
    page_title="炊事組二天一夜 - 智慧導覽系統",
    page_icon="🍲",
    layout="centered"
)

# ==========================================
# 2. 大地色系 UI 視覺架構 (符合 UIUX-CRF v9.0 規範)
# ==========================================
st.markdown("""
    <style>
    /* 大地色系背景與字體 */
    .stApp {
        background-color: #F5F5DC; /* 米色大地底 */
        color: #4B3621; /* 深咖啡色字體 */
    }
    
    /* 標題與卡片樣式 */
    .itinerary-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #8B4513; /* 鞍褐點綴 */
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .time-tag {
        color: #FFFFFF !important;
        background-color: #556B2F; /* 橄欖綠 */
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 0.8em;
        font-weight: bold;
    }
    
    h1, h2, h3 {
        color: #3E2723 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 行程數據結構 (符合 Code-CRF v9.0 遍歷性原則)
# ==========================================
itinerary_data = {
    "Day 1: 啟程與部落地圖": [
        {"time": "08:30 - 09:00", "event": "集合出發", "desc": "校門口集合，清點炊事器材與食材。"},
        {"time": "09:00 - 11:30", "event": "前進部落", "desc": "沿途欣賞風景，預計抵達長濱鄉。"},
        {"time": "12:00 - 13:30", "event": "大地午餐", "desc": "炊事組首航：簡易輕食與在地食材對接。"},
        {"time": "14:00 - 17:00", "event": "部落文化導覽", "desc": "南溪部落巡禮，認識「海~我們的冰箱」。"},
        {"time": "18:00 - 20:00", "event": "營火晚宴", "desc": "正式炊事挑戰：原民風味料理製作。"}
    ],
    "Day 2: 採集與歸途": [
        {"time": "07:30 - 08:30", "event": "部落早餐", "desc": "營養均衡配比，準備今日體力。"},
        {"time": "09:00 - 11:00", "event": "海邊採集體驗", "desc": "實地觀察漁獵與海洋資源利用。"},
        {"time": "12:00 - 13:30", "event": "成果午宴", "desc": "使用採集食材進行創意料理（Foting/Kalang）。"},
        {"time": "14:00 - 16:00", "event": "結業與心得分享", "desc": "Falahan 老師指導，心得交換。"},
        {"time": "16:30 - 19:00", "event": "賦歸", "desc": "帶著滿滿的回憶與技術平安回家。"}
    ]
}

# ==========================================
# 4. APP 主介面邏輯 (符合 Custom-CRF v9.0 ROI 矩陣)
# ==========================================
st.title("🍲 炊事組：二天一夜智慧導覽")
st.write("Code-CRF v9.0 驅動 | 高效能文化保存架構")

# 建立分頁 (Tabs)
tab1, tab2 = st.tabs(["📅 Day 1 行程", "🌊 Day 2 行程"])

with tab1:
    st.header("第一天：探索與紮營")
    for item in itinerary_data["Day 1: 啟程與部落地圖"]:
        st.markdown(f"""
        <div class="itinerary-card">
            <span class="time-tag">{item['time']}</span>
            <h3>{item['event']}</h3>
            <p>{item['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("第二天：深耕與賦歸")
    for item in itinerary_data["Day 2: 採集與歸途"]:
        st.markdown(f"""
        <div class="itinerary-card">
            <span class="time-tag">{item['time']}</span>
            <h3>{item['event']}</h3>
            <p>{item['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 5. 決策校準層 (符合 10-1 模組 B 規範)
# ==========================================
with st.sidebar:
    st.subheader("🛡️ 系統狀態監控")
    st.info("架構版本：v9.0 (Institutional)")
    st.success("🟢 Tier 1: 運行中")
    
    st.divider()
    st.subheader("📝 炊事組備忘錄")
    task = st.checkbox("確認食材保鮮度")
    task2 = st.checkbox("確認 GitHub 代碼同步")
    
    if st.button("啟動緊急熔斷 (Hard Stop)"):
        st.error("⚠️ 根據憲法原則：系統已停止所有非核心進程。")

# 頁尾
st.caption("© 2026 智慧旅遊架構師系統 | 遵循二天一夜專案特定邏輯")
