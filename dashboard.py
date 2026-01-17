import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="UIDAI Intel Center", page_icon="🇮🇳", layout="wide")

# --- TITLE & HEADER ---
st.title("🇮🇳 UIDAI Operational Intelligence Center")
st.markdown("""
<style>
    .metric-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("### 🕵️ Anomaly Detection & Predictive Resource Allocation")
st.markdown("---")

# --- DATA LOADER (Cached for speed) ---
@st.cache_data
def load_data():
    # 1. Load the Master Data
    try:
        df = pd.read_csv("master_data.csv")
    except FileNotFoundError:
        st.error("⚠️ 'master_data.csv' not found! Please run data_setup.py first.")
        st.stop()
    
    # 2. Convert Date
    df['date'] = pd.to_datetime(df['date'])
    
    # 3. Ensure Pincode is String for merging
    df['pincode'] = df['pincode'].astype(str).str.split('.').str[0] 

    # 4. Calculate Suspicion Score
    # Avoid division by zero by adding 1
    df['suspicion_score'] = df['bio_update_adult'] / (df['enrol_18_plus'] + 1)
    
    return df

@st.cache_data
def load_lat_long():
    # Fetching Open Source Pincode Directory
    try:
        url = "https://raw.githubusercontent.com/workforce-data-initiative/India-Pincodes/master/India-Pincodes.csv"
        geo_df = pd.read_csv(url)
        # Select and rename columns to match our master data
        geo_df = geo_df[['pincode', 'Latitude', 'Longitude', 'District']]
        geo_df.columns = ['pincode', 'lat', 'lon', 'geo_district']
        # Ensure Pincode is String
        geo_df['pincode'] = geo_df['pincode'].astype(str)
        return geo_df
    except Exception as e:
        # Fail silently if internet is down, handled in main loop
        return None

# --- LOAD DATA ---
with st.spinner("Loading Secure Data Pipeline..."):
    df = load_data()
    geo_df = load_lat_long()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Intel")
selected_state = st.sidebar.selectbox("Select State", ["All"] + sorted(df['state'].unique().tolist()))

if selected_state != "All":
    filtered_df = df[df['state'] == selected_state]
else:
    filtered_df = df

selected_metric = st.sidebar.radio("View Mode", ["⚠️ Fraud/Anomalies", "👶 Child Enrolment Trends"])

# --- KPI METRICS ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Records Processed", f"{len(filtered_df):,}")
c2.metric("Total Biometric Updates", f"{filtered_df['bio_update_adult'].sum():,}")
c3.metric("Total New Enrolments", f"{filtered_df['enrol_18_plus'].sum():,}")
high_risk_count = len(filtered_df[filtered_df['suspicion_score'] > 50])
c4.metric("High Risk Pincodes", f"{high_risk_count}", delta="Action Required", delta_color="inverse")

st.markdown("---")

# --- MAIN VISUALIZATION ---
st.subheader("📍 Geospatial Anomaly Heatmap")

if geo_df is not None:
    # Aggregate data by Pincode for the map
    map_data = filtered_df.groupby('pincode').agg({
        'suspicion_score': 'max',
        'bio_update_adult': 'sum',
        'state': 'first',
        'district': 'first'
    }).reset_index()
    
    # Merge with coordinates
    map_data = pd.merge(map_data, geo_df, on='pincode', how='inner')
    
    if selected_metric == "⚠️ Fraud/Anomalies":
        # Plotting High Risk Areas
        fig_map = px.scatter_mapbox(
            map_data[map_data['suspicion_score'] > 2], # Threshold filter
            lat="lat", lon="lon",
            color="suspicion_score",
            size="suspicion_score",
            hover_name="district",
            hover_data=["pincode", "bio_update_adult"],
            color_continuous_scale="Reds",
            size_max=30,
            zoom=3.5,
            mapbox_style="open-street-map",
            title="High-Risk Centers (Updates exceeding Enrolments)"
        )
    else:
        # Plotting Enrolment Hubs
        fig_map = px.scatter_mapbox(
            map_data,
            lat="lat", lon="lon",
            color="bio_update_adult",
            size="bio_update_adult",
            color_continuous_scale="Viridis",
            zoom=3.5,
            mapbox_style="open-street-map",
            title="Biometric Update Volume Centers"
        )
    
    # RENDER THE MAP (This was the missing link)
    st.plotly_chart(fig_map, use_container_width=True)

else:
    st.warning("⚠️ Internet connection required to fetch Map Coordinates. Showing Charts only.")

# --- DEEP DIVE CHARTS ---
c_left, c_right = st.columns(2)

with c_left:
    st.subheader("📊 Top 10 Anomalous Districts")
    top_districts = filtered_df.groupby('district')['suspicion_score'].mean().sort_values(ascending=False).head(10)
    fig_bar = px.bar(top_districts, orientation='h', title="Avg Suspicion Score by District", color=top_districts.values, color_continuous_scale='Reds')
    st.plotly_chart(fig_bar, use_container_width=True)

with c_right:
    st.subheader("📈 Trend Over Time")
    daily_trend = filtered_df.groupby('date')[['bio_update_adult', 'enrol_18_plus']].sum().reset_index()
    fig_line = px.line(daily_trend, x='date', y=['bio_update_adult', 'enrol_18_plus'], title="Updates vs Enrolments Timeline")
    st.plotly_chart(fig_line, use_container_width=True)

# --- THE "GOLDEN" LIST ---
st.subheader("📋 Top Priority Investigation List")
suspicious_list = filtered_df.sort_values(by='suspicion_score', ascending=False).head(50)
st.dataframe(suspicious_list[['date', 'state', 'district', 'pincode', 'bio_update_adult', 'enrol_18_plus', 'suspicion_score']])