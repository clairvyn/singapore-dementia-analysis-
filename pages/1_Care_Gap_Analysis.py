# Page 1 of 2 — Care Gap Analysis

import streamlit as st
import geopandas as gpd
import plotly.express as px

st.set_page_config(
    page_title="Singapore Dementia Care Analysis",
    layout="wide"
)

@st.cache_data
def load_data():
    gdf = gpd.read_file("data/processed/planning_areas_dashboard.geojson")
    return gdf

gdf = load_data()

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

st.subheader("PWDs per Formal Care Facility by Planning Area")

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
    labels={"PLN_AREA_N": " ", "pwd_per_facility": "PWDs per Facility", "pwd_estimate": "PWDs (estimate)", "facility_count": "Facilities"},
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style="background-color: #f8f4f0; border-left: 4px solid #c0392b; padding: 1rem 1.25rem; margin: 1rem 0; border-radius: 0 6px 6px 0;">
<p style="margin: 0 0 0.5rem 0; font-size: 0.95rem; line-height: 1.6; color: #2c2c2c;">Singapore's dementia burden is geographically concentrated.</p>
<p style="margin: 0 0 0.5rem 0; font-size: 0.95rem; line-height: 1.6; color: #2c2c2c;">The ten highest-burden planning areas account for roughly half of all estimated PWDs nationally: Bedok, Tampines, Hougang, Ang Mo Kio, Bukit Merah, Jurong West, Toa Payoh, Yishun, Woodlands, and Sengkang.</p>
<p style="margin: 0; font-size: 0.95rem; line-height: 1.6; color: #2c2c2c;">Most of them are the mature HDB towns built in the 1970s and 1980s, whose original resident populations have aged largely in place.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Coverage Strain by Planning Area")
st.write("Planning areas with formal care facilities, ranked by PWDs per facility. Reference line shows the national average of 619.9.")

bar_df = gdf[gdf['facility_count'] > 0][['PLN_AREA_N', 'pwd_per_facility']].copy()
bar_df = bar_df.sort_values('pwd_per_facility', ascending=True).reset_index(drop=True)

bar_fig = px.bar(
    bar_df,
    x='pwd_per_facility',
    y='PLN_AREA_N',
    orientation='h',
    labels={'PLN_AREA_N': 'Planning Area', 'pwd_per_facility': 'PWDs per Facility'},
    color='pwd_per_facility',
    color_continuous_scale='Reds',
    height=700
)

bar_fig.add_vline(
    x=619.9,
    line_dash="dash",
    line_color="black",
    annotation_text="National average: 619.9",
    annotation_position="top right"
)

bar_fig.update_layout(showlegend=False, coloraxis_showscale=False)
st.plotly_chart(bar_fig, use_container_width=True)

table_df = gdf[gdf['facility_count'] > 0][['PLN_AREA_N', 'pwd_estimate', 'facility_count', 'pwd_per_facility']].copy()
table_df = table_df.sort_values('pwd_per_facility', ascending=False).reset_index(drop=True)
table_df.columns = ['Planning Area', 'PWDs (estimate)', 'Facilities', 'PWDs per Facility']
table_df['PWDs per Facility'] = table_df['PWDs per Facility'].round(0).astype(int)
st.dataframe(table_df, use_container_width=True, hide_index=True)

st.markdown("""
<div style="background-color: #f8f4f0; border-left: 4px solid #c0392b; padding: 1rem 1.25rem; margin: 1rem 0; border-radius: 0 6px 6px 0;">
<p style="margin: 0 0 0.5rem 0; font-size: 0.95rem; line-height: 1.6; color: #2c2c2c;">Not all planning areas with facilities are equally covered.</p>
<p style="margin: 0 0 0.5rem 0; font-size: 0.95rem; line-height: 1.6; color: #2c2c2c;">Bedok has 12, the most of any planning area, but also the highest estimated PWD population at 8,197, putting it at 683 per facility.</p>
<p style="margin: 0; font-size: 0.95rem; line-height: 1.6; color: #2c2c2c;">Marine Parade tells the opposite story. One facility serving an estimated 1,573 PWDs, more than twice the national average strain.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Planning Areas with No Formal Care Facility")

unserved_df = gdf[(gdf['facility_count'] == 0) & (gdf['pwd_estimate'] > 0)][['PLN_AREA_N', 'pwd_estimate']].copy()
unserved_df = unserved_df.sort_values('pwd_estimate', ascending=False).reset_index(drop=True)
unserved_df.columns = ['Planning Area', 'Est. PWDs']

total_unserved = unserved_df['Est. PWDs'].sum()

card1, card2, card3 = st.columns(3)

with card1:
    card1.metric("Total PWDs in unserved planning areas", f"{total_unserved:,}")

with card2:
    card2.metric("Populated planning areas with no formal dementia care presence", "15")

with card3:
    card3.metric("Most PWDs with no facility: Bukit Timah", "2,215")
st.dataframe(unserved_df, use_container_width=True, hide_index=True)

st.write("The remaining 13 planning areas without population and facilities are excluded. They are industrial zones, military land, or water catchment reserves (e.g. Tuas, Western Islands).")

st.caption(" ")
st.caption("PWD estimates are modelled, not direct counts. Estimates are derived from SingStat resident population data (June 2024) and WiSE 2023 prevalence rates.<br>Facility data from AIC Care Services (148 facilities, snapshot: 12 March 2026).<br>Planning area boundaries from URA Master Plan 2019 (data.gov.sg).", unsafe_allow_html=True)
st.caption(" ")
st.caption("Limitations: Facility counts reflect presence, not capacity. Informal care arrangements (e.g. foreign domestic workers) are not captured in public data. Geographic proximity does not guarantee access — cultural, financial, and informational barriers may also affect uptake.")

st.divider()
st.page_link("pages/2_Area_Intelligence_Brief.py", label="→ Area Intelligence Brief", icon="🗺️")
