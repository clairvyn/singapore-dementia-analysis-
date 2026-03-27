import streamlit as st
import geopandas as gpd
import plotly.express as px

@st.cache_data
def load_data():
    gdf = gpd.read_file("data/processed/planning_areas_dashboard.geojson")
    return gdf

gdf = load_data()

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Singapore Dementia Care Gap Analysis")
st.write("Estimated persons with dementia (PWDs) versus formal dementia day care facilities across Singapore's planning areas.")

col1, col2, col3 = st.columns(3)

col1.metric("Estimated PWDs (National)", "95,649")
col2.metric("Formal Care Facilities", "148")
col3.metric("Avg PWDs per Facility", "619.9")

geojson = gdf.__geo_interface__

fig = px.choropleth_mapbox(
    data_frame=gdf,
    geojson=geojson,
    locations="PLN_AREA_N",
    featureidkey="properties.PLN_AREA_N",
    color="pwd_per_facility",
    color_continuous_scale="Reds",
    mapbox_style="carto-positron",
    height=600,
    zoom=11,
    center={"lat": 1.3521, "lon": 103.8198},
    opacity=0.7,
    hover_name="PLN_AREA_N",
    hover_data={"PLN_AREA_N": False, "pwd_estimate": True, "facility_count": True, "pwd_per_facility": ":.0f"},
    title="PWDs per Formal Care Facility by Planning Area",
    labels={"PLN_AREA_N":" ", "pwd_per_facility": "PWDs per Facility", "pwd_estimate": "PWDs (estimate)", "facility_count": "Facilities"},
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("Planning Areas by PWDs per Facility")

table_df = gdf[gdf['facility_count'] > 0][['PLN_AREA_N', 'pwd_estimate', 'facility_count', 'pwd_per_facility']].copy()
table_df = table_df.sort_values('pwd_per_facility', ascending=False).reset_index(drop=True)
table_df.columns = ['Planning Area', 'PWDs (estimate)', 'Facilities', 'PWDs per Facility']
table_df['PWDs per Facility'] = table_df['PWDs per Facility'].round(0).astype(int)

st.dataframe(table_df, use_container_width=True, hide_index=True)

st.subheader("Planning Areas with No Formal Care Facility")
st.write("These planning areas have an estimated PWD population but no formal dementia day care facility.")

unserved_df = gdf[(gdf['facility_count'] == 0) & (gdf['pwd_estimate'] > 0)][['PLN_AREA_N', 'pwd_estimate']].copy()
unserved_df = unserved_df.sort_values('pwd_estimate', ascending=False).reset_index(drop=True)
unserved_df.columns = ['Planning Area', 'Est. PWDs']

total_unserved = unserved_df['Est. PWDs'].sum()
st.metric("Total PWDs in unserved planning areas", f"{total_unserved:,}")

st.dataframe(unserved_df, use_container_width=True, hide_index=True)

st.write("Planning areas without population and facilities are excluded (e.g. Tuas, Western Islands)")

st.caption(" ")
st.caption("PWD estimates are modelled from SingStat population data and WiSE 2023 prevalence rates, not direct counts.<br>PWD estimates based on SingStat resident population data (June 2024) and WiSE 2023 prevalence rates. Facility data from AIC Care Services locator (snapshot: 12 March 2026).", unsafe_allow_html=True)
st.caption(" ")
st.caption("Limitations: Facility counts reflect presence, not capacity. Informal care arrangements (e.g. foreign domestic workers) are not captured in public data. Geographic proximity does not guarantee access — cultural, financial, and informational barriers may also affect uptake.")



