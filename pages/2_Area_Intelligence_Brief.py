# Page 2 of 2 — Area Intelligence Brief (Cairn Agent)

import sys
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Singapore Dementia Care Analysis",
    layout="wide"
)

_ROOT = Path(__file__).parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from agent.agent import generate_brief

# ---------------------------------------------------------------------------
# Planning area selectbox
# ---------------------------------------------------------------------------

PLANNING_AREAS = [
    "Ang Mo Kio", "Bedok", "Bishan", "Boon Lay", "Bukit Batok",
    "Bukit Merah", "Bukit Panjang", "Bukit Timah",
    "Central Water Catchment", "Changi", "Changi Bay",
    "Choa Chu Kang", "Clementi", "Downtown Core", "Geylang",
    "Hougang", "Jurong East", "Jurong West", "Kallang",
    "Lim Chu Kang", "Mandai", "Marina East", "Marina South",
    "Marine Parade", "Museum", "Newton", "North-Eastern Islands",
    "Novena", "Orchard", "Outram", "Pasir Ris", "Paya Lebar",
    "Pioneer", "Punggol", "Queenstown", "River Valley", "Rochor",
    "Seletar", "Sembawang", "Sengkang", "Serangoon", "Simpang",
    "Singapore River", "Southern Islands", "Straits View",
    "Sungei Kadut", "Tampines", "Tanglin", "Tengah", "Toa Payoh",
    "Tuas", "Western Islands", "Western Water Catchment",
    "Woodlands", "Yishun",
]

st.title("Area Intelligence Brief")

st.markdown("""
<style>
.selector-label {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.25rem;
    color: #1A1A1A;
}
.selector-helper {
    font-size: 0.9rem;
    color: #666666;
    margin-bottom: 0.75rem;
}
.brief-card {
    background-color: #F5F5F5;
    border-radius: 8px;
    padding: 1.5rem 2rem;
    margin-bottom: 1rem;
}
.brief-card h4 {
    color: #C84B31;
    margin-top: 0;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="selector-label">Planning area</p>', unsafe_allow_html=True)
st.markdown('<p class="selector-helper">Select a planning area to generate its brief.</p>', unsafe_allow_html=True)

selected_area = st.selectbox(
    label="planning_area",
    options=PLANNING_AREAS,
    index=None,
    placeholder="Type or scroll to select...",
    label_visibility="collapsed",
)

generate_btn = st.button("Generate Brief", type="primary", disabled=selected_area is None)

# ---------------------------------------------------------------------------
# Brief generation — cached with 30-day TTL
# ---------------------------------------------------------------------------

@st.cache_data(ttl=2_592_000)
def get_brief(planning_area: str) -> dict:
    return generate_brief(planning_area)

# ---------------------------------------------------------------------------
# Session state — persist brief across page navigation
# ---------------------------------------------------------------------------

if "last_brief" not in st.session_state:
    st.session_state.last_brief = None
if "last_area" not in st.session_state:
    st.session_state.last_area = None

if generate_btn and selected_area:
    with st.spinner(f"Generating brief for {selected_area}..."):
        try:
            brief = get_brief(selected_area)
            st.session_state.last_brief = brief
            st.session_state.last_area = selected_area
        except Exception as e:
            st.error(f"Brief generation failed: {e}")

# ---------------------------------------------------------------------------
# Display — card layout
# ---------------------------------------------------------------------------

if st.session_state.last_brief:
    brief = st.session_state.last_brief
    area = st.session_state.last_area

    st.markdown(f"#### Brief: {area}")

    sections = [
        ("1. Demand Snapshot", "burden_snapshot"),
        ("2. Care Infrastructure", "formal_care_presence"),
        ("3. Policy Context", "policy_context"),
        ("4. Operational Implications", "operational_considerations"),
    ]

    for label, key in sections:
        st.markdown(
            f'<div class="brief-card"><h4>{label}</h4>{brief[key]}</div>',
            unsafe_allow_html=True,
        )

st.divider()
st.page_link("pages/1_Care_Gap_Analysis.py", label="← Care Gap Analysis", icon="📊")
