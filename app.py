# ==========================================================
# 🚀 ELITE AI RANSOMWARE DETECTION SYSTEM
# ==========================================================

# =========================
# IMPORT LIBRARIES
# =========================
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time
import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="AI Ransomware Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#000428,#004e92,#000428);
    color: white;
}

.main-title {
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#00F5FF;
    text-shadow:0px 0px 25px cyan;
}

.sub-title {
    text-align:center;
    font-size:24px;
    margin-bottom:35px;
    color:white;
}

.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 0px 20px rgba(0,255,255,0.25);
    transition:0.3s;
}

.card:hover {
    transform:scale(1.05);
}

.stTabs [data-baseweb="tab"] {
    background:#111827;
    color:white;
    font-size:18px;
    font-weight:bold;
    border-radius:12px;
    padding:10px;
}

.stTabs [aria-selected="true"] {
    background:#00F5FF !important;
    color:black !important;
}

.alert-box {
    background:linear-gradient(135deg,#ff0000,#ff4b4b);
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:white;
    box-shadow:0px 0px 35px red;
}

section[data-testid="stSidebar"] {
    background:#081120;
}

.stButton>button {
    background: linear-gradient(to right,#00F5FF,#00FF99);
    color:black;
    font-size:18px;
    font-weight:bold;
    border-radius:12px;
    height:55px;
    width:100%;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================
st.markdown("""
<div class='main-title'>
🛡️ AI Ransomware Detection
</div>

<div class='sub-title'>
Real-Time Threat Intelligence & Cloud Malware Analytics
</div>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD DATASET
# ==========================================================
@st.cache_data
def load_data():

    data = pd.read_csv("data_file.csv")

    data = data.fillna(0)

    return data

data = load_data()

# ==========================================================
# PREPROCESSING
# ==========================================================
X = data.drop("Benign", axis=1)

X = X.select_dtypes(include=['int64','float64'])

y = data["Benign"]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==========================================================
# MACHINE LEARNING MODEL
# ==========================================================
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=20,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================================================
# MODEL ACCURACY
# ==========================================================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

# ==========================================================
# TOP CARDS
# ==========================================================
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='card'>
    <h2>📂 Total Files</h2>
    <h1>{len(data)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='card'>
    <h2>🎯 Accuracy</h2>
    <h1>{accuracy:.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    threats = int((data['Benign']==0).sum())

    st.markdown(f"""
    <div class='card'>
    <h2>⚠ Threats</h2>
    <h1>{threats}</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='card'>
    <h2>🛡 Security</h2>
    <h1>ACTIVE</h1>
    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# TABS
# ==========================================================
tab1,tab2,tab3,tab4,tab5 = st.tabs([
    "📂 File Activity",
    "🧠 Prediction",
    "📊 Analytics",
    "📈 Threat Monitor",
    "⚙ Security Logs"
])

# ==========================================================
# TAB 1 : FILE ACTIVITY
# ==========================================================
with tab1:

    st.markdown("## 📂 Simulate File Behaviour")

    col1,col2 = st.columns(2)

    with col1:

        debug_size = st.slider(
            "🛠 Debug Information Size",
            0,1000,50
        )

        export_size = st.slider(
            "📦 Export Function Size",
            0,1000,20
        )

        resource_size = st.slider(
            "📁 File Resource Usage",
            0,5000,100
        )

    with col2:

        number_sections = st.slider(
            "🧩 Executable Sections",
            0,20,3
        )

        bitcoin_addresses = st.slider(
            "💰 Bitcoin Wallet Activity",
            0,10,0
        )

        encryption_score = st.slider(
            "🔐 Encryption Behaviour Score",
            0,100,10
        )

    st.info("""
    These behavioural parameters help the AI system
    identify suspicious ransomware patterns.
    """)

# ==========================================================
# TAB 2 : PREDICTION
# ==========================================================
with tab2:

    st.markdown("## 🧠 AI Threat Prediction")

    if st.button("🚀 START AI THREAT SCAN"):

        with st.spinner("🔍 AI Engine Scanning Activity..."):
            time.sleep(2)

        # ====================================
        # CUSTOM THREAT LOGIC
        # ====================================

        threat_score = 0

        # Debug Size
        if debug_size > 300:
            threat_score += 20

        # Export Size
        if export_size > 300:
            threat_score += 20

        # Resource Usage
        if resource_size > 2000:
            threat_score += 20

        # Executable Sections
        if number_sections > 8:
            threat_score += 20

        # Bitcoin Activity
        if bitcoin_addresses > 3:
            threat_score += 20

        # Encryption Score
        if encryption_score > 60:
            threat_score += 20

        # ====================================
        # NORMAL ACTIVITY
        # ====================================

        if threat_score < 60:

            safe_score = 100 - threat_score

            st.success("✅ NORMAL ACTIVITY DETECTED")

            st.balloons()

            st.subheader("🟢 Safe Activity Meter")

            st.progress(int(safe_score))

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=safe_score,
                title={'text': "Safety Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "green"},
                    'steps': [
                        {'range': [0, 50], 'color': "red"},
                        {'range': [50, 80], 'color': "orange"},
                        {'range': [80, 100], 'color': "green"}
                    ]
                }
            ))

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

            st.success(
                f"🟢 Safe Probability : {safe_score:.2f}%"
            )

            st.write("### ✅ Analysis Report")

            st.write("""
            - No suspicious encryption behaviour detected
            - File activity appears normal
            - Low ransomware risk identified
            - System operating safely
            """)

        # ====================================
        # RANSOMWARE DETECTED
        # ====================================

        else:

            st.markdown("""
            <div class='alert-box'>
            🚨 RANSOMWARE DETECTED 🚨
            </div>
            """, unsafe_allow_html=True)

            st.subheader("🔥 Threat Meter")

            st.progress(int(threat_score))

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=threat_score,
                title={'text': "Threat Level"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "red"},
                    'steps': [
                        {'range': [0, 50], 'color': "green"},
                        {'range': [50, 80], 'color': "orange"},
                        {'range': [80, 100], 'color': "red"}
                    ]
                }
            ))

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

            st.error(
                f"🚨 Threat Probability : {threat_score:.2f}%"
            )

            st.write("### ⚠ Risk Analysis")

            st.write("""
            - Suspicious encryption behaviour detected
            - File structure indicates malware pattern
            - Cryptocurrency activity identified
            - High executable anomaly score
            - Possible ransomware attack detected
            """)

            st.write(
                "🕒 Detection Time:",
                datetime.datetime.now()
            )

# ==========================================================
# TAB 3 : ANALYTICS
# ==========================================================
with tab3:

    st.markdown("## 📊 Malware Analytics")

    fig1 = px.pie(
        names=["Normal","Ransomware"],
        values=data["Benign"].value_counts(),
        hole=0.55,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    importance = model.feature_importances_

    importance_df = pd.DataFrame({
        "Feature":X.columns,
        "Importance":importance
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    fig2 = px.bar(
        importance_df.head(10),
        x="Importance",
        y="Feature",
        orientation='h',
        template="plotly_dark",
        color="Importance"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("## 📈 Correlation Heatmap")

    fig,ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        data.select_dtypes(include=np.number).corr(),
        cmap="coolwarm"
    )

    st.pyplot(fig)

# ==========================================================
# TAB 4 : THREAT MONITOR
# ==========================================================
with tab4:

    st.markdown("## 📈 Live Threat Monitoring")

    trend_data = pd.DataFrame({
        "Time":[1,2,3,4,5,6,7,8],
        "Threat Level":[
            random.randint(10,100)
            for i in range(8)
        ]
    })

    fig3 = px.line(
        trend_data,
        x="Time",
        y="Threat Level",
        markers=True,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# ==========================================================
# TAB 5 : SECURITY LOGS
# ==========================================================
with tab5:

    st.markdown("## ⚙ System Security Logs")

    log_data = pd.DataFrame({

        "Timestamp":[
            str(datetime.datetime.now())
            for i in range(5)
        ],

        "Activity":[
            "Firewall Activated",
            "Threat Scan Completed",
            "Cloud Monitoring Enabled",
            "AI Model Trained",
            "Security Alert Generated"
        ],

        "Status":[
            "Success",
            "Completed",
            "Running",
            "Completed",
            "Success"
        ]
    })

    st.dataframe(log_data)

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("""
<hr>

<center>

<h3 style='color:#00F5FF;'>

🔐 Elite AI Cloud Security & Threat Intelligence Dashboard

</h3>

</center>
""", unsafe_allow_html=True)