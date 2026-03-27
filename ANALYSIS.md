# Where Singapore's Dementia Burden Falls
### A Geographic Burden Study — March 2026

---

## The Question

Singapore had an estimated 74,000 persons living with dementia in 2023,
a figure derived from the WiSE 2023 study and confirmed by MOH in a
parliamentary Q&A in November 2025. By 2030, the government projects
that number will roughly double to 152,000 — driven almost entirely by
the ageing of the existing population rather than any change in the
underlying disease. The 85+ age cohort, Singapore's fastest-growing
demographic, carries a prevalence rate of nearly one in two.

The policy response has focused on national totals: expanding day care
places from 1,000 in 2015 to 4,200 by 2021, increasing polyclinic
memory clinic coverage, raising public awareness. What has not been
publicly examined is whether the infrastructure that does exist is
located where the burden is actually concentrated. This study tries to
answer that question with the data available.

---

## Why a Burden Study, Not a Gap Analysis

This is deliberately framed as a geographic burden study rather than a
gap analysis. A gap analysis requires two things you can actually
measure: demand on one side, supply on the other. Singapore's public
data provides the demand side cleanly. The supply side does not hold up
under scrutiny.

The AIC E-care Locator gives facility locations, not capacity. No
published source provides the number of day care places per facility,
whether those places are occupied, what the waitlists look like, or how
many staff are on roster. The most recent national capacity figure —
4,200 places — is from a 2021 parliamentary speech and has never been
disaggregated by planning area. A review of MOH, OECD, and regional
comparators — Japan, Taiwan, Hong Kong — found no published benchmark
ratio for dementia day care places per population anywhere. There is no
external standard to measure against.

The honest question this data can answer is narrower: are facilities
located in the planning areas where dementia burden is highest, or is
there a spatial mismatch between where people with dementia live and
where formal care exists? That is what this study maps.

---

## Building the Demand Surface

The demand surface starts with WiSE 2023 — the Well-being of the
Singapore Elderly study, a nationally representative survey of 2,010
residents conducted by the Institute of Mental Health and published in
*Alzheimer's & Dementia* in 2025. It is the most current and
authoritative Singapore-specific prevalence estimate available.

WiSE 2023 provides three age-specific prevalence rates: 3.0% for
residents aged 60–74, 18.2% for 75–84, and 48.6% for 85 and above.
These were applied to SingStat's resident population counts for all 55
URA Master Plan planning areas as of June 2024, producing an estimated
PWD count per planning area — modelled, not measured, but transparent
and methodologically consistent with how MOH constructs its own
national projections.

The resulting national estimate is approximately 95,600 persons with
dementia. This is higher than WiSE 2023's published figure of ~73,900
for two reasons: the population data used here is June 2024, capturing
further ageing after the survey period; and population definition
differences mean slightly more residents fall within the 60+ age bands
when applied at the planning area level. Both figures are
methodologically legitimate. This study uses the derived estimate and
discloses the basis explicitly.

---

## What the Data Shows

Dementia burden is not evenly distributed. Singapore's ten
highest-burden planning areas — Bedok, Tampines, Hougang, Ang Mo Kio,
Bukit Merah, Jurong West, Toa Payoh, Yishun, Woodlands, and Sengkang —
account for roughly half of all estimated PWDs nationally. These are the
mature HDB towns built in the 1970s and 1980s, whose original resident
populations have aged largely in place.

Of the 55 planning areas in the URA Master Plan, 28 have no formal
dementia care facility. Thirteen of these are genuine non-residential
areas — industrial zones, military land, water catchment reserves,
uninhabited islands — where zero facilities is the correct and expected
outcome. The analytically meaningful number is the remaining 15:
populated planning areas with no formal dementia care presence.

Among those 15, three stand out. Bukit Timah has an estimated 2,215
persons with dementia and no facility. Tanglin has 540. Rochor has 465.
The rest of the no-facility populated areas have estimated PWD counts
small enough to sit within the uncertainty range of the prevalence
calculation itself — they are worth noting but not the headline finding.

Among planning areas that do have facilities, the relationship between
estimated burden and care presence varies sharply — and not in the
direction one might expect. The highest-burden planning area, Bedok, has
one of the more favourable ratios: 12 facilities serving an estimated
8,197 PWDs, at 683 per facility. Marine Parade, a much smaller area,
has a single facility serving an estimated 1,573 PWDs. Jurong East has
two facilities for 2,101 estimated PWDs at 1,050 per facility. Choa Chu
Kang has three facilities for 3,036 at 1,012 per facility.

This is the finding the data surfaces most clearly. Raw burden — the
total number of estimated PWDs — and relative strain — how many
estimated PWDs each facility serves — tell different stories about
different places, and point toward different policy responses. A
city-level planner prioritising investment by absolute need and a
neighbourhood-level service provider thinking about accessibility would
draw different conclusions from the same maps.

The full ranking is in the [live dashboard](https://singapore-dementia-analysis.streamlit.app/).

---

## What This Cannot Tell You

Three things constrain what this analysis can claim.

**Facility count is not capacity.** A planning area with one large,
well-staffed centre may serve more people than one with three small
under-resourced ones. The locational data used here cannot distinguish
between them. The PWDs-per-facility ratio is a geographic accessibility
indicator — it measures whether a facility exists in the area, not
whether it can or does serve the people who need it.

**Informal care is invisible.** A substantial proportion of dementia
caregiving households in Singapore employ a foreign domestic worker as
primary caregiver. This parallel care system does not appear in any
public dataset. A planning area that appears underserved by formal
services may have significant FDW-based care coverage. The analysis
cannot distinguish between a genuine service vacuum and a household
that has made or been forced into a different care arrangement.

**Prevalence rates are national proxies applied locally.** WiSE 2023
rates are applied uniformly across all 55 planning areas. Sub-national
dementia prevalence has not been directly measured in any published
study. Planning areas with higher proportions of Malay or Indian
elderly residents may face structurally higher burden than the uniform
rates suggest — peer-reviewed evidence indicates elevated prevalence
in both groups relative to Chinese — but applying ethnic adjustment
factors at the planning area level requires Census ethnic composition
data and introduces additional modelling assumptions not included in
this version of the analysis.

---

## What Would Make This More Useful

Three extensions would convert this descriptive mapping study into a
genuine gap analysis.

A short caregiver survey in two or three target planning areas — asking
about travel time to the nearest facility, awareness of available
options, current care arrangement, and reasons for non-use — would
provide the utilisation evidence that formal data cannot supply. It does
not require ethics approval for an anonymous survey.

Hospital outcomes data — dementia-related A&E presentations or
unplanned hospitalisations by planning area, sourced from NHG or
SingHealth — would shift the frame from infrastructure counts to health
consequences. A planning area with high dementia-related hospital
admissions and low formal care presence is the most compelling possible
evidence that spatial mismatch has real clinical costs.

FDW care geography modelling — using MOM employment data combined with
Census household composition by planning area — would make the invisible
informal care layer partially visible, enabling a more honest assessment
of total coverage and a more nuanced reading of what formal service
mismatch means in different neighbourhood contexts.

---

*Data sources: SingStat June 2024 resident population; URA Master Plan
2019 planning area boundaries (data.gov.sg); AIC E-care Locator
snapshot, 12 March 2026 (148 facilities); WiSE 2023 prevalence rates
(Subramaniam et al., Alzheimer's & Dementia, 2025). Analysis conducted
March 2026.*