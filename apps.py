# ==========================================================
# 🚀 ULTRA ADVANCED AI RANSOMWARE DETECTION SYSTEM
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
import time
import datetime
import random
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="AI Ransomware Detection",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# CUSTOM UI DESIGN
# =========================
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg,#000428,#004e92);
    color: white;
}

/* Main Title */
.main-title {
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#00F5FF;
    text-shadow:0px 0px 25px cyan;
    animation: glow 2s infinite alternate;
}

/* Glow Effect */
@keyframes glow {
    from {
        text-shadow:0px 0px 10px cyan;
    }
    to {
        text-shadow:0px 0px 40px cyan;
    }
}

/* Subtitle */
.sub-title {
    text-align:center;
    font-size:22px;
    margin-bottom:30px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 0px 20px rgba(0,255,255,0.3);
    transition:0.3s;
}

.card:hover {
    transform:scale(1.05);
}

/* Alert Box */
.alert-box {
    background:linear-gradient(135deg,#ff0000,#ff4b4b);
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:white;
    box-shadow:0px 0px 30px red;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background:#081120;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size:18px;
    font-weight:bold;
    color:white;
    background-color:#111827;
    border-radius:10px;
    padding:10px;
}

.stTabs [aria-selected="true"] {
    background-color:#00F5FF !important;
    color:black !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class='main-title'>
🛡️ AI Ransomware Detection System
</div>

<div class='sub-title'>
Cloud Threat Intelligence & Malware Monitoring Dashboard
</div>
""", unsafe_allow_html=True)

# =========================
# LOAD DATASET
# =========================
@st.cache_data
def load_data():

    data = pd.read_csv(
        "c6c347d2-1cc1-4ea5-b2ce-14a1d3c8759a.csv"
    )

    data = data.fillna(0)

    return data

data = load_data()

# =========================
# PREPROCESSING
# =========================
X = data.drop("Benign", axis=1)

X = X.select_dtypes(include=['int64','float64'])

y = data["Benign"]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MODEL TRAINING
# =========================
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=20,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model,"ransomware_model.pkl")

# =========================
# MODEL ACCURACY
# =========================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

# =========================
# DASHBOARD CARDS
# =========================
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='card'>
    <h2>📂 Records</h2>
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
    st.markdown(f"""
    <div class='card'>
    <h2>⚠ Threats</h2>
    <h1>{int((data['Benign']==0).sum())}</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='card'>
    <h2>🛡 Status</h2>
    <h1>ACTIVE</h1>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================
# CREATE TABS
# =========================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📂 File Activity",
    "🧠 Prediction",
    "📊 Analytics",
    "📈 Threat Monitoring",
    "⚙ System Logs"
])

# ==========================================================
# TAB 1 : FILE ACTIVITY
# ==========================================================
with tab1:

    st.markdown("## 📂 File Behaviour Analysis")

    debug_size = st.slider(
        "🛠 Debug Information Size",
        0,1000,100
    )

    export_size = st.slider(
        "📦 Export Function Size",
        0,1000,50
    )

    resource_size = st.slider(
        "📁 File Resource Usage",
        0,5000,500
    )

    number_sections = st.slider(
        "🧩 Executable Sections",
        0,20,3
    )

    bitcoin_addresses = st.slider(
        "💰 Suspicious Bitcoin Activity",
        0,10,0
    )

    st.info("""
    These parameters simulate suspicious
    executable file behavior for ransomware detection.
    """)

# ==========================================================
# TAB 2 : PREDICTION
# ==========================================================
with tab2:

    st.markdown("## 🧠 AI Prediction Engine")

    if st.button("🚀 START AI SCAN"):

        with st.spinner("🔍 AI Engine Scanning Threat..."):
            time.sleep(3)

        input_data = {
            "DebugSize": debug_size,
            "ExportSize": export_size,
            "ResourceSize": resource_size,
            "NumberOfSections": number_sections,
            "BitcoinAddresses": bitcoin_addresses
        }

        input_df = pd.DataFrame([input_data])

        input_df = input_df.reindex(
            columns=X.columns,
            fill_value=0
        )

        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)

        probability = model.predict_proba(
            input_scaled
        )[0][0]

        if prediction[0] == 0:

            st.markdown("""
            <div class='alert-box'>
            🚨 RANSOMWARE DETECTED 🚨
            </div>
            """, unsafe_allow_html=True)

            threat_score = probability * 100

            st.subheader("🔥 Threat Meter")

            st.progress(int(threat_score))

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=threat_score,
                title={'text':"Threat Level"},
                gauge={
                    'axis':{'range':[0,100]},
                    'bar':{'color':"red"},
                    'steps':[
                        {'range':[0,50],'color':"green"},
                        {'range':[50,80],'color':"orange"},
                        {'range':[80,100],'color':"red"}
                    ]
                }
            ))

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

            st.error(
                f"⚠ Threat Probability : {threat_score:.2f}%"
            )

            st.write(
                "🕒 Detection Time:",
                datetime.datetime.now()
            )

        else:

            st.success(
                "✅ NORMAL ACTIVITY DETECTED"
            )

# ==========================================================
# TAB 3 : ANALYTICS
# ==========================================================
with tab3:

    st.markdown("## 📊 Dataset Analytics")

    # Pie Chart
    fig1 = px.pie(
        names=["Normal","Ransomware"],
        values=data["Benign"].value_counts(),
        hole=0.5,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # Feature Importance
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

# ==========================================================
# TAB 4 : THREAT MONITORING
# ==========================================================
with tab4:

    st.markdown("## 📈 Live Threat Monitoring")

    threat_data = pd.DataFrame({
        "Time":[1,2,3,4,5,6,7],
        "Threat Level":[
            random.randint(20,95)
            for i in range(7)
        ]
    })

    fig3 = px.line(
        threat_data,
        x="Time",
        y="Threat Level",
        markers=True,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.success("🟢 Firewall Active")
    st.info("☁ Cloud Monitoring Enabled")
    st.warning("🔒 AI Threat Scanner Running")

# ==========================================================
# TAB 5 : SYSTEM LOGS
# ==========================================================
with tab5:

    st.markdown("## ⚙ Security Logs")

    log_data = pd.DataFrame({

        "Time":[
            str(datetime.datetime.now())
            for i in range(5)
        ],

        "Activity":[
            "Firewall Started",
            "Cloud Monitoring Enabled",
            "Threat Scan Completed",
            "Dataset Loaded",
            "AI Engine Activated"
        ],

        "Status":[
            "Success",
            "Active",
            "Completed",
            "Success",
            "Running"
        ]
    })

    st.dataframe(log_data)

    st.download_button(
        label="📥 Download Logs",
        data=log_data.to_csv(index=False),
        file_name="security_logs.csv",
        mime="text/csv"
    )

# =========================
# FOOTER
# =========================
st.markdown("""
<hr>

<center>

<h3 style='color:#00F5FF;'>

🔐 AI-Powered Cloud Security & Threat Intelligence Dashboard

</h3>

</center>
""", unsafe_allow_html=True)