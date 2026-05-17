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
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="AI Ransomware Detection",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#000428,#004e92,#000428);
    color:white;
}

.main-title{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#00F5FF;
    text-shadow:0px 0px 25px cyan;
}

.sub-title{
    text-align:center;
    font-size:22px;
    margin-bottom:30px;
}

.card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 0px 20px rgba(0,255,255,0.2);
}

.alert-box{
    background:linear-gradient(135deg,#ff0000,#ff4b4b);
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:white;
}

.stButton>button{
    background:linear-gradient(to right,#00F5FF,#00FF99);
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
# LOAD DATA
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

# Keep numeric columns only
X = X.select_dtypes(include=['int64','float64'])

y = data["Benign"]

# Scaling
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Train test split
X_train,X_test,y_train,y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==========================================================
# MODEL
# ==========================================================
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=20,
    random_state=42
)

model.fit(X_train,y_train)

# Accuracy
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

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
    <h1>{accuracy*100:.2f}%</h1>
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
    st.markdown("""
    <div class='card'>
    <h2>🛡 Security</h2>
    <h1>ACTIVE</h1>
    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# TABS
# ==========================================================
tab1,tab2,tab3,tab4 = st.tabs([
    "📂 File Activity",
    "🧠 Prediction",
    "📊 Analytics",
    "📈 Threat Monitor"
])

# ==========================================================
# TAB 1
# ==========================================================
with tab1:

    st.subheader("📂 Simulate File Activity")

    col1,col2 = st.columns(2)

    with col1:

        debug_size = st.slider(
            "🛠 Debug Size",
            0,1000,100
        )

        export_size = st.slider(
            "📦 Export Size",
            0,1000,50
        )

        resource_size = st.slider(
            "📁 Resource Size",
            0,5000,500
        )

    with col2:

        number_sections = st.slider(
            "🧩 Number Of Sections",
            0,20,4
        )

        bitcoin_addresses = st.slider(
            "💰 Bitcoin Addresses",
            0,10,1
        )

        encryption_score = st.slider(
            "🔐 Encryption Score",
            0,100,30
        )

# ==========================================================
# TAB 2
# ==========================================================
with tab2:

    st.subheader("🧠 AI Threat Prediction")

    if st.button("🚀 START AI SCAN"):

        with st.spinner("Scanning Threat Activity..."):
            time.sleep(2)

        # ==================================================
        # THREAT SCORE LOGIC
        # ==================================================
        threat_score = (
            debug_size * 0.10 +
            export_size * 0.10 +
            resource_size * 0.05 +
            number_sections * 5 +
            bitcoin_addresses * 15 +
            encryption_score * 0.8
        )

        # Normalize
        threat_score = min(threat_score,100)

        # ==================================================
        # ML PREDICTION
        # ==================================================
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

        # ==================================================
        # FINAL PREDICTION LOGIC
        # ==================================================
        if threat_score > 60 or prediction[0] == 0:

            st.markdown("""
            <div class='alert-box'>
            🚨 RANSOMWARE DETECTED 🚨
            </div>
            """, unsafe_allow_html=True)

            st.progress(int(threat_score))

            # Gauge Chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=threat_score,
                title={'text':"Threat Level"},
                gauge={
                    'axis':{'range':[0,100]},
                    'bar':{'color':"red"},
                    'steps':[
                        {'range':[0,40],'color':"green"},
                        {'range':[40,70],'color':"orange"},
                        {'range':[70,100],'color':"red"}
                    ]
                }
            ))

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.error(
                f"⚠ Threat Probability : {threat_score:.2f}%"
            )

            st.markdown("## 🔥 AI Risk Analysis")

            st.write("""
            - Suspicious encryption behaviour detected
            - Cryptocurrency activity identified
            - File structure anomaly detected
            - Potential ransomware payload behaviour
            """)

            st.write(
                "🕒 Detection Time:",
                datetime.datetime.now()
            )

        else:

            st.success(
                "✅ NORMAL ACTIVITY DETECTED"
            )

            st.balloons()

# ==========================================================
# TAB 3
# ==========================================================
with tab3:

    st.subheader("📊 Threat Analytics")

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

    # Heatmap
    st.subheader("📈 Correlation Heatmap")

    fig,ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        data.select_dtypes(include=np.number).corr(),
        cmap="coolwarm"
    )

    st.pyplot(fig)

# ==========================================================
# TAB 4
# ==========================================================
with tab4:

    st.subheader("📈 Live Threat Monitoring")

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

    st.markdown("## 🚨 Recent Threat Alerts")

    alerts = pd.DataFrame({

        "Threat":[
            "Encryption Attack",
            "Crypto Activity",
            "Suspicious Payload",
            "Malicious Executable",
            "Ransomware Pattern"
        ],

        "Severity":[
            "High",
            "Critical",
            "Medium",
            "High",
            "Critical"
        ]
    })

    st.dataframe(alerts)

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("""
<hr>

<center>

<h3 style='color:#00F5FF;'>

🔐 Elite AI Cloud Security Dashboard

</h3>

</center>
""", unsafe_allow_html=True)