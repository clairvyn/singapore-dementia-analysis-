# Singapore Dementia Care Burden Analysis

A geographic burden study examining whether the distribution of formal dementia 
care facilities across Singapore's 55 planning areas reflects where estimated 
dementia burden is concentrated.

**[→ Live dashboard](https://singapore-dementia-analysis.streamlit.app/)**
**[→ Read the full analysis](ANALYSIS.md)**

---

## What This Project Does

Singapore's dementia burden is not evenly distributed. Mature HDB towns whose 
resident populations have aged in place — Bedok, Tampines, Hougang, Ang Mo Kio 
— carry disproportionately high estimated PWD counts. This project quantifies 
that burden at the planning area level and maps it against the locations of 148 
formal dementia day care facilities, asking a practical question: does care 
infrastructure follow need?

This is a burden study, not a gap analysis. No sub-national capacity data exists 
to support a gap framing — the AIC E-care Locator gives facility locations, not 
places, staffing, or utilisation. The metric used here is estimated PWDs per 
formal care facility by planning area: a geographic accessibility indicator, not 
a measure of adequacy.

---

## Key Findings

- **95,647** estimated persons with dementia across 55 planning areas (WiSE 2023 
  rates applied to SingStat June 2024 population data)
- **28 of 55** planning areas have no formal dementia care facility
- **15 populated** planning areas have no facility, including Bukit Timah 
  (est. 2,215 PWDs) and Tanglin (est. 540 PWDs)
- Highest burden: **Bedok at 8,197 estimated PWDs**, followed by Tampines 
  (5,749) and Hougang (5,509)
- Highest strain ratio: **Marine Parade at 1,573 estimated PWDs per facility**, 
  Jurong East (1,050), Choa Chu Kang (1,012)

---

## Methodology

**Demand surface** — WiSE 2023 age-specific prevalence rates applied to SingStat 
resident population by planning area:

| Age band | Prevalence rate |
|---|---|
| 60–74 | 3.0% |
| 75–84 | 18.2% |
| 85+ | 48.6% |

Source: Subramaniam et al., *Alzheimer's & Dementia*, 2025. Confirmed by MOH 
in Parliamentary Q&A, November 2025.

**Supply proxy** — 148 AIC-listed dementia day care facilities geocoded via 
OneMap API and spatially joined to URA Master Plan 2019 planning area boundaries. 
Facility count is used as locational presence only — not capacity or utilisation.

**Primary metric** — Estimated PWDs per formal dementia care facility by planning 
area. Zero-facility areas are flagged separately rather than assigned a ratio.

---

## Data Sources

| Dataset | Source | Date |
|---|---|---|
| Resident population by planning area and age | SingStat | June 2024 |
| Planning area boundaries | URA Master Plan 2019, data.gov.sg | 2019 |
| Dementia day care facility locations | AIC E-care Locator snapshot | 12 March 2026 |
| Prevalence rates | WiSE 2023 (Subramaniam et al., 2025) | 2023 |

---

## Repo Structure
```
singapore-dementia-analysis-/
├── data/
│   ├── raw/           # Source files
│   └── processed/     # Pipeline outputs
├── notebooks/
│   ├── 01_geocode_facilities.ipynb
│   ├── 02_build_demand_surface.ipynb
│   ├── 03_merge_and_compute.ipynb
│   └── 04_streamlit_choropleth_dashboard.ipynb
├── app.py
└── requirements.txt
```

---

## Limitations

**Facility count ≠ capacity.** A planning area with one large centre may serve 
more people than one with three small ones. No sub-national capacity data is 
publicly available in Singapore.

**Informal care is invisible.** Roughly 50% of dementia caregiving households 
in Singapore employ a foreign domestic worker as primary caregiver (Yuan et al., 
*BMC Geriatrics*, 2022). This layer does not appear in any public dataset.

**Prevalence rates are national proxies.** WiSE 2023 rates are applied uniformly 
across planning areas. Sub-national dementia prevalence has not been directly 
measured.

**Supply figure is a lower bound.** The most recent national capacity figure — 
4,200 places — is from 2021. Actual 2026 capacity is likely higher; no updated 
figure has been published.

---

## Built With

Python · pandas · GeoPandas · Plotly · Streamlit  
Data: SingStat · data.gov.sg · AIC · OneMap API