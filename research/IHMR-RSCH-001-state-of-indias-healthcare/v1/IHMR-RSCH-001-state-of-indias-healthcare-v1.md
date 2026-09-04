---
id: IHMR-RSCH-001
type: research
title: The State of India's Healthcare, September 2026
status: evidence
version: 1
authors:
  - Tejas Parthasarathi Sudarshan
orcid: https://orcid.org/0009-0008-6765-7281
created: 2026-09-04
updated: 2026-09-04
topics:
  - india
  - population-health
  - health-systems
  - non-communicable-disease
  - health-financing
  - digital-health
related:
  - IHMR-Q-001
  - IHMR-Q-005
  - IHMR-Q-006
ai_disclosure: substantially-ai-assisted
ai_tools:
  - claude-fable-5
signed_off_by:
signed_off_date:
doi:
license: CC-BY-4.0
lang: en
---

# The State of India's Healthcare, September 2026

> **AI disclosure:** Substantially AI-assisted · Awaiting human sign-off
>
> Research was retrieved and drafted by AI, then every claim was independently checked against
> its cited source by a separate verification pass. **It has not yet been signed off by a
> person, and until it is, nothing here should be cited.** See
> [how we use AI](https://projectihmr.org/about/how-we-use-ai).

*An IHMR research article. IHMR is an open research project on Indian health infrastructure. Everything below is drawn from published, verifiable sources; every figure carries its source and the period the data actually describes.*

---

## 0. How to read this

This article is dated September 2026. Much of the data in it is not, and you should know that before you read a single number.

India has not counted its population since 2011. The 2021 census was postponed because of COVID-19, and the 16th census - Census 2027 - was notified in the Gazette of India on 16 June 2025 (S.O. 2681(E), under the Census Act 1948) with a reference date of 00:00 hours on 1 March 2027, and 1 October 2026 for Ladakh and the snow-bound areas of Jammu & Kashmir, Himachal Pradesh and Uttarakhand. That means every official population denominator in this article - the totals, the age shares, the urban share - rests on projections published in July 2020 from a census base that is now fifteen years old. The same vintage problem runs through the whole system: the latest facility census is as on 31 March 2023, the latest National Health Accounts describe 2022-23, the only national treatment-cascade measurements come from surveys fielded in 2017-21, and the newest household survey (NFHS-6, fieldwork 2023-24, fact sheets released May 2026) is still labelled provisional. We state the data period next to every figure. This is not an apology; it is one of the findings. A health system's ability to describe itself is part of its condition, and anyone serious about Indian health data checks the dates before the values.

Three rules govern what follows. First, only claims that survived independent verification against primary sources appear here; where a verified claim was later superseded by a newer official release (several were, between the first draft and this one), the newer figure is used and the older one kept for the trend. Second, where credible sources disagree - and they disagree on things as basic as how many people live in India - we report the range and do not average. Third, where a number in this article is our own arithmetic (for example, applying a survey percentage to a population estimate), it is labelled *derived* and the inputs are named.

Sections 1 to 9 lay out the facts: who the people are, what they suffer and die from, how much of their illness is found and treated, how long they live, who delivers and pays for care, and what the digital layer records. Section 10 turns those facts into a single table: the questions India's health information systems can and cannot currently answer. Section 11 lists what we could not establish at all. Section 12 gives the sources in full.

---

## 1. The people

Start with the most basic fact a health system needs: how many people it serves. India cannot currently answer this with a count.

The official domestic projection - the Technical Group on Population Projections, published July 2020 from the 2011 Census base - puts India's population at 142.3 crore (1,423 million) as on 1 March 2026, on a path from 136.1 crore in 2021 to 151.8 crore in 2036 (National Commission on Population, MoHFW, 2020). The United Nations series says India had 1,463.9 million people in 2025 (World Population Prospects 2024 revision, via UNFPA). Interpolating the domestic series to 2025 gives roughly 1,411 million. The two official-grade estimates therefore differ by about 50 million people - more than the population of Kerala and Punjab combined - and only Census 2027 will resolve it. Every prevalence-to-headcount conversion in this article, and in Indian health planning generally, is sensitive to which denominator is chosen.

[CHART: india-population-projections-2011-2036 | Total population, age-group shares, dependency ratios and urban share, 2011 census count and official projections to 2036]

### Ageing is the structural story

Whichever denominator you prefer, the age structure is moving one way. On the official projections (2011 base, published 2020):

- The share aged 60 and above rises from 8.4% in 2011 to a projected 11.5% in 2026 and 15.0% in 2036. In absolute terms the 60+ population more than doubles, from 10.2 crore in 2011 to a projected 16.3 crore in 2026 and 22.8 crore in 2036.
- The share of children (0-14) falls from 30.9% (2011) to a projected 19.8% (2036). The working-age (15-59) share peaks around 65.2% in 2031.
- The median age rises from 24.9 years (2011) to a projected 30.4 (2026) and 34.7 (2036).
- The total dependency ratio falls from 646 per 1,000 working-age persons (2011) to a projected floor of 533 around 2031, then edges back up - because the old-age ratio rises from 138 (2011) to a projected 231 (2036) even as the young-age ratio falls from 508 to 305. From the early 2030s, ageing rather than fertility drives the dependency burden.

And the projections may be running behind reality. NFHS-6 (fieldwork 28 May 2023 to 31 December 2024; fact sheets released May 2026, provisional, excluding Manipur) measured the 60+ share of the surveyed household population at 12.9%, up from 11.8% in NFHS-5 (2019-21) - already ahead of the projected track of roughly 11% for 2024 (MoHFW/IIPS, 2026). Survey household shares are not strictly comparable to projected de-facto population shares, but the direction of the discrepancy suggests ageing may be running faster than the 2011-based projections assume.

[CHART: nfhs-age-structure-comparison | Measured age structure of the household population, NFHS-5 (2019-21) vs NFHS-6 (2023-24): the 60+ share rose from 11.8% to 12.9%]

Beyond the projection horizon, the India Ageing Report 2023 (UNFPA-IIPS) projects the elderly share to double to over 20% of the population by 2050, with the elderly surpassing the number of children (0-15) around 2046 and the 80+ population growing by around 279% between 2022 and 2050 (UNFPA India release, 2023).

### Fertility, the dividend, and urbanisation

Fertility is at or below replacement on every recent measure: NFHS-6 puts the total fertility rate at 2.0 children per woman (urban 1.6, rural 2.1; 2023-24, provisional), UNFPA's State of World Population 2025 puts it at 1.9, and the official projections assume a decline to 1.72 by 2031-35. Report the range, 1.9 to 2.0; do not average. The implication is the same either way: future growth in chronic-disease load comes from ageing and population momentum, not from high fertility.

The Economic Survey 2018-19 (Ministry of Finance, using 2011-base projections) projects the demographic dividend to peak around 2041, when the 20-59 working-age share hits 59%. The working-age population grows by 96.5 million during 2021-31 but only 41.5 million during 2031-41, and starts declining in 11 of the 22 major states during 2031-41. A widely quoted claim that India's demographic window runs from 2005-06 to 2055-56 could be traced only to secondary summaries citing UNFPA, not to a retrievable primary document; treat it as folklore with a plausible shape, and anchor instead on the Economic Survey's 2041 peak.

The urban share is projected to rise from 31.1% in 2011 to 36.2% in 2026 and, per the projection report's own Table 10, 39.6% in 2036 - though the same report's summary text says 38.6%, an internal inconsistency the report never resolves. No census has measured the urban share since 2011; every urbanisation figure for 2021-2036 is a model output. The projections attribute 73% of the total 2011-2036 population increase of 30.7 crore to urban growth (Technical Group on Population Projections, 2020).

---

## 2. What Indians die of and live with

### What the death registers say

The best current cause-of-death data comes with a large caveat attached to it. The Medical Certification of Cause of Death (MCCD) report for 2023 (Registrar General of India, published 2025) covers only the 19.0 lakh deaths that were medically certified - 22.0% of the 86.6 lakh deaths registered that year. Certified deaths skew urban and hospital-based, so these shares are not nationally representative. With that stated: diseases of the circulatory system were the leading cause group, at 36.4% of medically certified deaths in 2023, followed by respiratory diseases (11.5%), infectious and parasitic diseases (8.7%), genitourinary diseases (4.9%, of which renal failure alone is 78.5%), cancers (4.8%) and injuries and poisoning (4.3%). A further 11.9% fell under ill-defined symptoms and signs - deaths certified, but not usefully explained.

[CHART: mccd-2023-cause-shares | Share of medically certified deaths by cause group, India 2023 - noting that only 22% of registered deaths were medically certified at all]

### The non-communicable turn

The canonical measurement of India's epidemiological transition remains the ICMR/PHFI/IHME India State-Level Disease Burden Initiative: the share of deaths due to non-communicable diseases rose from 37.9% in 1990 to 61.8% in 2016, and the NCD share of total disease burden (DALYs) rose from 30% to 55% over the same period (published 2017; still the figures MoHFW itself cites). WHO's estimate for 2019 is higher: NCDs caused 66% of all deaths in India - over 60.46 lakh deaths - and a 30-year-old Indian had a 22% probability of dying before age 70 from an NCD (WHO, *Invisible Numbers*, 2022, via secondary report). Two credible figures, 61.8% (2016) and 66% (2019); report both.

The double burden is still real. In 2016, three of the five leading individual causes of DALYs were non-communicable (ischaemic heart disease, COPD, stroke) but five of the top ten were still infectious or nutritional: diarrhoeal diseases, lower respiratory infections, iron-deficiency anaemia, preterm birth complications and tuberculosis - with India's DALY rates for diarrhoea, anaemia and TB 2.5 to 3.5 times higher than in comparable countries (ICMR/PHFI/IHME, 2017; data period 2016). No India-ranked GBD 2021 cause list could be retrieved to update this, a gap noted in Section 11.

The chronic-disease headcounts, with their vintages:

- **Hypertension**: an estimated 315 million adults aged 20+ (35.5%), per ICMR-INDIAB, the nationally representative metabolic survey (fieldwork phased 2008-2020, projected to 2021, published 2023).
- **Diabetes**: 101 million adults (11.4%), plus 136 million with prediabetes (15.3%) - same source, same vintage.
- **Cardiovascular disease**: prevalent cases more than doubled from 25.7 million (1990) to 54.5 million (2016) (GBD 2016, Lancet Global Health 2018).
- **COPD**: 28.1 million cases (1990) to 55.3 million (2016); India carried 32% of the world's chronic respiratory disease DALYs in 2016, with 53.7% of COPD DALYs attributable to air pollution (GBD 2016, Lancet Global Health 2018).
- **Chronic kidney disease**: estimates disagree badly. GBD 2021 puts prevalence at 128.0 million people (9.3%); a 2025 meta-analysis of community studies pools prevalence at 16.38% among those 15+ for 2018-2023 studies, up from 11.12% in 2011-2017 studies. Definitions and eGFR equations differ; report the range, do not average.
- **Cancer**: an estimated 14,61,427 new cases in 2022 (crude rate 100.4 per 100,000), projected to reach about 15.7 lakh in 2025; roughly one in nine Indians will develop cancer in their lifetime (ages 0-74) (ICMR-NCDIR National Cancer Registry Programme, Indian Journal of Medical Research, 2022).
- **Mental disorders**: the National Mental Health Survey (2015-16, 12 states) found 10.6% of adults had a current mental disorder, with treatment gaps of 70.4-86.3% across disorder groups. GBD 2017 estimates, using broader definitions, put 197.3 million Indians (14.3%) as having a mental disorder, including 45.7 million with depressive and 44.9 million with anxiety disorders. The two figures measure different things; NMHS-2, covering all states, was still unpublished as of September 2026.
- **Road injuries**: 2024 was the worst year on record - 1,77,175 deaths across 4,87,707 accidents, with 4,71,441 injured (MoRTH, *Road Accidents in India 2024*, released June 2026), up 2.5% on 2023's 1,72,890 deaths. More than two-thirds of the dead in 2023 were aged 18-45, for the fourth consecutive year.

NFHS-6 adds a measured, current signal on the metabolic conditions. Among adults 15+ in 2023-24, high or very high random blood glucose (>140 mg/dl) or being on diabetes medication rose to 17.8% of women and 20.9% of men, from 13.5% and 15.6% in NFHS-5 (2019-21). Measured elevated blood pressure (≥140/90) or being on BP medication edged *down*: 19.4% of women and 22.1% of men, from 21.3% and 24.0% (MoHFW/IIPS, May 2026, provisional). These are single random measurements, not clinical diagnoses, and are not comparable with ICMR-INDIAB's methodology - but the blood-sugar trend is fast and in one direction.

[CHART: nfhs-clinical-indicators-trend | Measured blood sugar and blood pressure among adults 15+, NFHS-5 (2019-21) vs NFHS-6 (2023-24): sugar up sharply, blood pressure slightly down]

### What disables is not what kills

The leading causes of years lived with disability differ from the leading killers. In the last retrievable India-specific ranking (GBD 2015), iron-deficiency anaemia was the single largest cause of YLDs in India and low back and neck pain the second. Globally in GBD 2021, the top three YLD causes were low back pain, depressive disorders and headache disorders (Lancet, 2024). The India ranking is a decade old and should be treated as indicative, not current - another self-knowledge gap logged in Section 11.

### Tuberculosis: large, improving

India still accounts for about 25% of the world's TB cases - the largest share of any country - but the trend is strongly favourable. TB incidence fell 21%, from 237 per lakh population in 2015 to 187 per lakh in 2024, almost double the global rate of decline (12%), and TB mortality fell from 28 to 21 per lakh (WHO Global TB Report 2025, via MoHFW). 26.18 lakh TB patients were diagnosed in 2024 against an estimated incidence of 27 lakh; treatment coverage reached 92%, up from 53% in 2015.

[CHART: tb-trend-who-india | India TB incidence, mortality and treatment coverage, 2015 vs 2024 (WHO Global TB Report 2025)]

### The maternal and child mortality success story

Whatever else is said in this article, this deserves saying plainly: the twenty-year decline in maternal and child deaths is one of the largest public-health achievements anywhere in this period.

India's maternal mortality ratio was 301 per 100,000 live births in 2001-03. The latest Sample Registration System bulletin puts it at 87 for 2022-24 (95% CI 78-95), after 88 in both 2020-22 and 2021-23 (ORGI, SRS Special Bulletins; the 2022-24 bulletin released 2026). That is a fall of more than 70% in two decades. The SDG target of below 70 is not yet met, but it is in sight.

[CHART: mmr-trend-srs | India's maternal mortality ratio by rolling three-year SRS period, 130 (2014-16) down to 87 (2022-24)]

Infant mortality fell to 24 per 1,000 live births in 2024 - from 40 in 2013 and 129 in 1971 - meaning roughly one in 42 infants still dies before its first birthday (SRS Statistical Report 2024, released May 2026). Under-five mortality was 27 and neonatal mortality 18 per 1,000 live births in 2024. Deaths are increasingly concentrated in the newborn period: about 73% of infant deaths now occur within the first month of life, up from 61% in 2003 (SRS, via Data For India analysis) - which is what success looks like, because the easier-to-prevent post-neonatal deaths have fallen fastest, leaving the hardest clinical problem as the residual.

[CHART: imr-trend-srs | India's infant mortality rate, SRS annual series 2013-2023 (40 down to 25; 24 in 2024 per the latest report)]

One measurement note: the NFHS-6 fact sheets, unlike NFHS-5's, report no infant or under-five mortality rates at all, so the SRS remains the only current source for mortality outcomes (see Section 11).

---

## 3. The undiagnosed fraction

This section is the heart of the article. India now has reasonable estimates of how many people have the major chronic conditions. What it measures far less well - and what no national system currently reports - is how many of them know, how many are treated, and how many are controlled. The published answer, wherever it has been measured, is: a small fraction.

### Hypertension: roughly one in twelve is controlled

The largest analysis is of NFHS-5 (fieldwork 2019-21), covering 1.69 million adults aged 18+ (Varghese et al., JAMA Network Open, 2023). Hypertension prevalence was 28.1%. Of those with hypertension:

- **36.9%** had ever been diagnosed;
- **17.7%** were on medication;
- **8.5%** had controlled blood pressure.

Those are the paper's headline figures, each expressed as a share of everyone with hypertension. Read as conditional steps, they mean that roughly **48% of the diagnosed** reach treatment, and roughly **48% of the treated** reach control (both derived: 17.7/36.9 and 8.5/17.7).

A note on a discrepancy, because it matters for anyone re-deriving these. The paper also reports step-conditional figures of 44.7% and 52.5%, and those do not multiply through to the marginals: 36.9% x 44.7% gives 16.5%, not 17.7%. The two sets use different analytic denominators, most likely differing subsamples with complete measurements at each step. **We use the marginals throughout**, because they share one denominator and because the absolute numbers below are derived from them. Anyone checking our arithmetic should do the same.

More than 90% of Indian adults with hypertension were undiagnosed, untreated, or treated but uncontrolled. Roughly one in twelve was controlled.

To put that in absolute terms, apply the NFHS-5 cascade percentages to ICMR-INDIAB's estimate of 315 million adults 20+ with hypertension (2021). These are *derived* figures - the two surveys use different age ranges (18+ vs 20+) and different years, and no published source reports national absolute counts - but the order of magnitude is the point:

- roughly **116 million** ever diagnosed (derived, 36.9% of 315M);
- roughly **56 million** on treatment (derived, 17.7% of 315M);
- roughly **27 million** controlled (derived, 8.5% of 315M);
- roughly **288 million** people walking around with uncontrolled high blood pressure (derived).

[CHART: hypertension-cascade-india-nfhs5 | The hypertension care cascade: from an estimated 315 million adults with hypertension down to roughly 27 million controlled - each bar labelled with source and derivation]

Other national measurements bracket the same picture. In the younger NFHS-5 reproductive-age sample (men 15-54, women 15-49; prevalence 18.3%), only 34.3% of people with hypertension were aware, 13.7% were on treatment and 7.8% were controlled (Lancet Regional Health - Southeast Asia, 2023). The National NCD Monitoring Survey (adults 18-69, fieldwork 2017-18) found 28.5% prevalence, with 27.9% aware, 14.5% on treatment and 12.6% controlled (Journal of Human Hypertension, 2022). Definitions differ across these studies - they should be reported side by side, never merged - but no study finds control above roughly one in eight.

### Diabetes: better diagnosed, poorly controlled

The diabetes cascade looks different depending on the measuring instrument, and the difference is itself informative.

- **NFHS-5 (2019-21, adults 18+, n=1.65 million)**: prevalence 6.5%; 74.2% of people with diabetes diagnosed; 59.4% of the diagnosed on medication; 65.5% of the diagnosed with glucose in the control range (JAMA Internal Medicine, 2023). The high "diagnosed" share is partly an artefact: self-reported diagnosis is part of the case definition.
- **NNMS (2017-18, adults 18-69, fasting glucose)**: prevalence 9.3%; 45.8% aware; 36.1% on treatment; only 15.7% controlled (Frontiers in Public Health, 2022).
- **LASI (2017-19, adults 45+, HbA1c-based)**: prevalence 19.8% - about 50.4 million people 45+ - with 60.1% aware, 49.4% on medication, and 45.7% of the diagnosed at HbA1c below 7% (Lancet Global Health, 2025).

[CHART: diabetes-cascade-india-two-sources | The diabetes cascade measured two ways: NFHS-5 (self-report plus random glucose) vs NNMS (fasting glucose) - the definitions disagree, the conclusion does not]

The best-case end of the cascade is measured by ICMR-INDIAB-13 (fieldwork 2008-2020): among people who *already know* they have diabetes, only 36.3% achieved glycaemic control (HbA1c <7%), 48.8% blood-pressure control, 41.5% LDL control - and just **7.7% achieved all three targets together** (Lancet Diabetes & Endocrinology, 2022). Even for the diagnosed and engaged, the system delivers guideline-level care to fewer than one in twelve.

### What the programme counts, and what it cannot say

Set against these survey cascades, the government's own programme numbers are large and genuinely unprecedented in scale - and they measure something different. The most recent directly sourced figures, from the National NCD portal as reported to Parliament cumulative to 31 October 2025, are **38.79 crore hypertension screening events and 5.13 crore diagnosed**, and **36.05 crore diabetes screening events with 3.45 crore diagnosed**.

There is a wrinkle worth stating rather than smoothing over. An earlier August 2025 statement, which we could only reach through press reports rather than the primary reply, gave 38.9 crore for hypertension and 38.7 crore for diabetes. Cumulative counts cannot fall, and 38.7 crore in August cannot become 36.05 crore in October. Either the August press reports mis-transcribed the diabetes figure, or the two replies cover different portal scopes. **We use the October figures throughout**, because they came from the primary reply.

We mention it because it is a small instance of the larger point this article keeps arriving at: the numbers a health system publishes about itself are part of its condition, and two parliamentary answers two months apart should not be irreconcilable. Under the 75/25 initiative (launched May 2023, target 75 million on standard care by December 2025), 42.01 million people had received hypertension treatment and 25.27 million diabetes treatment as of 5 March 2025 - 89.7% of target (PIB, March 2025).

Three caveats keep these numbers from being a cascade. "Screened" counts events, not unique people - a person screened annually is counted each time. "Under treatment" means registration on the portal, not verified adherence or control. And in the PIB release covering January-June 2025, the "diagnosed" and "under treatment" columns are *identical* (1,11,83,850 for hypertension; 64,11,051 for diabetes) - suggesting the portal records treatment initiation at the moment of diagnosis, which makes the treatment column an echo of the diagnosis column rather than an independent fact (PIB release 2155451, August 2025).

### The weakest link: after the positive screen

No national statistic exists for the share of positive screens that are ever confirmed. The clearest published measurement is a decade old and sobering: in a population-based diabetes screening programme in rural Andhra Pradesh (2015-16; 35,475 screened), only **6.4%** of high-risk individuals successfully followed up (616 of 9,670) visited any health facility for diagnostic confirmation; 52.2% of those who did not go cited the absence of symptoms (Global Health Action, 2018). Of those who did seek confirmation, 62.5% went to private facilities. A single-block assessment of NPCDCS in rural Jaipur (2019-20) found the later cascade steps can hold once someone is diagnosed and enrolled - 82-85% of detected cases referred onward, and 92-93% of diagnosed cases still on treatment at 90 days - but that study measures retention among the already-captured, not the fate of screen-positives (JFMPC, 2022).

### The benchmark: TB shows what a measured cascade looks like

Tuberculosis is the one Indian condition with a comparably quantified national care cascade, and it is instructive both as method and as message. Of an estimated 2.7 million prevalent TB patients in 2013: 72% were evaluated at public diagnostic facilities, 60% were diagnosed, 53% registered for treatment, 45% completed treatment, and 39% achieved one-year recurrence-free survival (Subbaraman et al., PLoS Medicine, 2016). The data are 2013-vintage and NTEP has changed materially since - but the exercise itself, counting people at every step and publishing the losses, has never been replicated nationally for any NCD.

[CHART: tb-cascade-india-2013 | The TB cascade of care, public sector, 2013: 2.7 million prevalent patients down to 39% recurrence-free at one year - the only Indian condition with a published national cascade]

### And the cascade data is not getting fresher

NFHS-6 (2023-24), released May 2026, reports prevalence categories only - no awareness, treatment or control breakdown. Until its unit-level data is analysed, every national cascade estimate rests on fieldwork from 2017-21 or earlier, all of it predating the Ayushman Arogya Mandir scale-up, 75/25 and the screening drives. Whether the last five years of programme activity have moved the cascade is, at present, unknowable from public data.

---

## 4. How long people live, and how well

Life expectancy at birth in India is 70.6 years for 2020-24, the latest Sample Registration System abridged life tables (ORGI, released 2026). The series ran 49.7 years in 1970-75, 69.4 in 2014-18, then flattened through the pandemic window (70.0 in 2016-20, 69.8 in 2017-21, 69.9 in 2018-22) before resuming its rise: 70.3 in 2019-23, 70.6 in 2020-24. A gain of about 21 years in five decades, with the COVID plateau now visibly ended in the official series.

[CHART: life-expectancy-trajectory-india | Life expectancy at birth, India, 1970-75 to 2018-22 (SRS) - 49.7 to 69.9, with the latest life tables extending the series to 70.6 for 2020-24]

WHO's modelled series tells the pandemic story more sharply: 70.7 years in 2019, falling to 67.3 in 2021 because WHO models excess COVID mortality year by year, where the SRS pools five years of field data (WHO Global Health Estimates, 2024). The two are methodologically different estimates of overlapping periods; both are reported here, and they should not be averaged.

On the 2020-24 tables, female life expectancy (72.8) exceeds male (68.7) by 4.1 years, and urban (73.2) exceeds rural (69.4) by 3.8 - the sex gap has widened and the urban-rural gap narrowed relative to 2018-22.

### Years lived in poor health

WHO's healthy life expectancy (HALE) estimate for India was 58.1 years in 2021, down from 60.9 in 2019 (WHO GHO; no post-2021 HALE published as of September 2026). Subtracting HALE from life expectancy gives the years an average Indian can expect to live in poor health: about 9.8 years on 2019 data, about 9.2 on 2021 data (derived from two WHO series; the smaller 2021 gap reflects COVID compressing total life expectancy, not better health). Read alongside Section 3, the arithmetic is uncomfortable: life expectancy is rising, and nearly a decade of it is lived with disease - much of it the undiagnosed, uncontrolled chronic disease the cascade section describes.

[CHART: le-hale-gap-india-who | Life expectancy vs healthy life expectancy, India (WHO): the gap is about nine to ten years lived in poor health]

On premature NCD mortality specifically: the unconditional probability of dying between ages 30 and 70 from the four major NCDs was 24.4% in 2010 and was projected by ICMR-NCDIR to fall only to 21.0% by 2025 - a 13.9% reduction against the WHO "25 by 25" target of 25%, which India will therefore miss; at current rates the WHO target is reachable around 2039 and the SDG 2030 target around 2053 (Kulothungan et al., *Sustainable Development*, 2024, via secondary report).

### The state spread: several countries in one

The all-India averages conceal gaps of a decade or more between states.

- **Life expectancy (2020-24)**: from 64.7 years in Chhattisgarh to 75.6 in Kerala - a 10.9-year spread, wider than the 10.4 years of 2018-22. Himachal Pradesh (74.7), Jammu & Kashmir (74.6) and Delhi (73.9) sit near the top; Madhya Pradesh (68.0), Uttar Pradesh (68.7) and Assam (69.0) near the bottom. For females the extremes are 67.1 (Chhattisgarh) and 78.7 (Kerala).
- **Maternal mortality (2022-24)**: Kerala at 24 per 100,000 live births against Uttar Pradesh at 154 - roughly six-fold. Madhya Pradesh 135, Chhattisgarh 124, Odisha 124, Assam 84 (much improved). The EAG-states-plus-Assam group averages 116 against 41 for the southern states (SRS Special Bulletin 2022-24). State-level confidence intervals are wide; the ranking of neighbours is soft, the EAG-versus-South gap is not.
- **Infant mortality (2024)**: the range across states runs from 2 (Manipur) to 36 (Chhattisgarh, now alone at the top; in 2023 it was 37 in Chhattisgarh, MP and UP against Kerala's 5) (SRS Statistical Report 2024).

[CHART: life-expectancy-by-state-2018-22 | Life expectancy at birth by state, SRS 2018-22 - Kerala 74.8 to Chhattisgarh 64.4; the 2020-24 tables widen the spread to 64.7-75.6]

[CHART: mmr-by-state-2020-22 | Maternal mortality ratio by state with 95% confidence intervals, SRS 2020-22 - the 2022-24 bulletin moves UP (154) above MP and brings Assam down to 84]

[CHART: imr-by-state-2023 | Infant mortality rate by state, SRS 2023 - Kerala 5 to 37 in Chhattisgarh, MP and UP; the 2024 report narrows the top to Chhattisgarh at 36]

---

## 5. Who delivers care

### The public network on paper

The most recent facility census - Health Dynamics of India 2022-23, data as on 31 March 2023, and still the latest edition as of early 2026 - counts 1,69,615 sub-centres, 31,882 primary health centres (PHCs), 6,359 community health centres (CHCs), 1,340 sub-divisional hospitals, 714 district hospitals and 362 medical colleges (MoHFW, published September 2024). The primary-care network is overwhelmingly rural: 1,65,639 of the sub-centres, 25,354 of the PHCs and 5,491 of the CHCs.

Against the IPHS population norms, rural India is short 22% of the sub-centres, 30% of the PHCs and 36% of the CHCs it should have - with the shortfalls concentrated where the disease burden is heaviest: Bihar is short 57% of sub-centres, Jharkhand 73% of PHCs, Telangana 84% and Bihar 71% of CHCs (HDI 2022-23, via PRS).

[CHART: public-health-infrastructure-2023 | The public facility pyramid as on 31 March 2023, rural/urban split and shortfall against norms]

Quality, measured against the government's own standards, is thinner still: as of 22 January 2025, with 93% of public facilities assessed, only 14% complied with more than 80% of IPHS norms, and 45% complied with less than half (MoHFW assessment, via PRS). Only 17% of CHCs had all four mandated specialists on board, and only 44% of PHCs functioned 24x7 (2022-23).

The one piece of infrastructure that has grown visibly past its target is the Ayushman Arogya Mandir (formerly Health and Wellness Centre) layer bolted onto sub-centres and PHCs: 1,76,325 operational as on 31 January 2025, 1,78,154 by 15 July 2025, 1,81,873 by 30 November 2025 - against an original target of 1.5 lakh - with cumulative footfall of 494.71 crore and 41.93 crore teleconsultations (PIB; MoHFW year-end review 2025).

[CHART: aam-operationalisation-timeline | Ayushman Arogya Mandirs operational, January to November 2025 - past the 1.5 lakh target and still growing]

### Where people actually go

The public network is half the story at most. The last all-India utilisation survey - NSS 75th round, July 2017 to June 2018, now eight years old and predating both COVID and PM-JAY's scale-up - found private hospitals handled 55% of hospitalisation cases (excluding childbirth) against 42% in government hospitals and 3% in charitable facilities; the public share was 46% rural and 35% urban, and fell as low as 21% in Telangana. For outpatient care the private share was 66%. The only newer behavioural signal is NFHS-5 (2019-21): 50% of households said they do not generally use government health facilities, rising to 80% in Bihar (via PRS).

[CHART: care-seeking-public-private | Public vs private shares of hospitalisation and outpatient care, NSS 2017-18 - the most recent national utilisation survey is eight years old]

---

## 6. Who does the work

### The headline ratios, and what they hide

India's official position (Rajya Sabha reply, February 2026) is that there are 13,88,185 registered allopathic doctors and 7,51,768 registered AYUSH practitioners, and that - assuming 80% of both are available - the doctor-population ratio is 1:811. Strip out AYUSH and the Economic Survey 2024-25 figure is one allopathic doctor per 1,263 people (as of 2024). Both are computed from cumulative registration stock, which includes the retired, emigrated and deceased; the true active workforce is unknown, which is why the ministry itself applies an assumed 80% discount. Nursing: 39.40 lakh registered nursing personnel (a category spanning RNs, midwives, ANMs and LHVs), yielding an assumed-active ratio of 2.23 per 1,000; 5,310 nursing institutions produce about 3.82 lakh nursing personnel a year (same reply).

[CHART: registered-health-workforce-density | Registered doctors, AYUSH practitioners and nurses, with the assumed-availability ratios the ministry publishes]

### The community workforce: the system's largest layer

The frontline of Indian public health is not doctors. It is roughly 3.5 million women:

- **10.29 lakh ASHAs** in position under the National Health Mission (as on 30 June 2024; 93,554 of them urban, as on 30 June 2025);
- about **2.13 lakh ANMs** in position at rural sub-centres and PHCs (as on 31 March 2023), plus 27,497 urban ANMs (June 2025) and 90,846 NHM-contractual ANMs (June 2024);
- **1,18,776 Community Health Officers** at rural sub-centres, against 1,46,132 sanctioned and 1,57,923 required (March 2023);
- **13,48,135 Anganwadi Workers** and **10,23,068 Anganwadi Helpers** (as on 31 December 2023, Ministry of Women and Child Development).

The NHM additionally supports about 3.89 lakh contractual clinical and paramedical staff in the states (June 2024).

[CHART: community-workforce | The community and frontline workforce by cadre, with as-of dates - roughly 3.5 million people, mostly women]

### Vacancies rise with skill level

The staffing data (all as on 31 March 2023, HDI 2022-23) shows a consistent gradient: the closer a post is to basic care, the better it is filled; the more specialised, the emptier.

- ANMs at rural sub-centres: 1,86,147 in position against 2,27,605 sanctioned - 18.6% vacant, but only 7% short of the requirement.
- Doctors at rural PHCs: 32,901 in position against 41,931 sanctioned - 22.3% of sanctioned posts vacant, yet only 3.8% short of the one-doctor-per-PHC norm, because sanctions exceed the norm.
- Specialists at rural CHCs: **4,413 in position against 21,964 required - a 79.9% shortfall.** Even against the 13,232 posts actually sanctioned, 67.8% were vacant. By cadre, the shortfall against requirement was 83% for surgeons, 82% for physicians, 81% for paediatricians and 74% for obstetrician-gynaecologists. PRS notes this shortfall has worsened from 46% in 2005 to 80% in 2023. In Mizoram and Sikkim the specialist shortfall is 100%; in Arunachal Pradesh and Meghalaya, 96%.

[CHART: rural-hr-sanctioned-vs-position-2023 | Required vs sanctioned vs in-position posts for key rural cadres, March 2023 - the specialist tier is four-fifths empty]

Read this against Section 3: a care cascade that requires confirmation, titration and follow-up of hundreds of millions of chronic cases runs, at its referral tier, on one-fifth of the specialists the government's own norms require.

---

## 7. Who pays

### The national accounts

The latest National Health Accounts describe 2022-23 and were published in May 2026 - a three-year lag, and they predate the October 2024 expansion of PM-JAY to everyone aged 70+. Headlines (NHSRC/MoHFW):

- Total health expenditure: Rs 8,81,359 crore - 3.37% of GDP (new 2022-23 GDP series), Rs 6,373 per capita.
- Government health expenditure: 1.48% of GDP on the new series (1.43% on the 2011-12 series, up from 1.15% in 2013-14); Rs 2,786 per capita, roughly 2.7 times the 2013-14 figure in nominal terms; 43.7% of total health expenditure, up from 28.6% in 2013-14. The 2021-22 spike to 1.84% of GDP was one-time COVID spending and has unwound.
- Out-of-pocket expenditure: 43.4% of total health expenditure - Rs 3,82,629 crore, Rs 2,767 per capita. Down from 64.2% in 2013-14, but *up* from 39.4% in 2021-22; the NHA itself flags that the 2021-22 low was a denominator artefact of COVID spending. Per capita OOP spending has risen in nominal terms every single year.

[CHART: ghe-share-of-gdp-trajectory | Government health expenditure as a share of GDP, 2013-14 to 2022-23 - the COVID spike and the settling at about 1.4-1.5%]

[CHART: oope-share-of-the-trajectory | Out-of-pocket share of total health expenditure, 64.2% (2013-14) to 43.4% (2022-23) - real progress, with a COVID-artefact dip in the middle]

What the money buys: preventive care was 8.88% of current health expenditure in 2022-23 against about 57.3% on curative care; pharmaceuticals absorbed 29.6%. Government spending on primary care has more than doubled, from about Rs 0.5 lakh crore (2013-14) to Rs 1.4 lakh crore (2022-23); primary care takes 51% of government current health expenditure.

### What out-of-pocket payment does to households

The catastrophic-expenditure estimates are old, which is itself a gap: the best figures rest on the 2011-12 NSS consumer expenditure survey - 17.9% of households incurred catastrophic health expenditure (out-of-pocket payments above 10% of consumption), and about 55 million people were pushed below the poverty line in that year by health payments, 38 million by spending on medicines alone (Selvaraj et al., BMJ Open, 2018). A newer analysis of the 2017-18 NSS round finds 16.8% of households facing catastrophic expenditure (Soni et al., Frontiers in Public Health, 2026). Different years, different methods; a range of roughly 16.8-17.9%, and nothing more recent than 2017-18 data exists. Note what both predate: PM-JAY at scale.

### The insurance layer

Ayushman Bharat PM-JAY covers about 12 crore poor and vulnerable families - roughly 55 crore people, the bottom 40% - for Rs 5 lakh per family per year of secondary and tertiary *hospitalisation*, expanded in September-October 2024 to all citizens aged 70+ regardless of income (about 6 crore seniors). The benefit package spans 1,961 procedures across 27 specialties (as of the July 2026 parliamentary reply; 1,949 as described in 2024), including three days of pre- and fifteen days of post-hospitalisation costs. Routine outpatient consultations, outpatient medicines and outpatient diagnostics are not covered - by design, the scheme pays for admissions, not for the chronic-disease management that Section 3 shows is the system's largest unmet task.

Scale so far: 44.73 crore Ayushman cards generated (Rajya Sabha reply of 28 July 2026, via press; cumulative cards, not active unique holders) and 12.69 crore hospital admissions authorised worth Rs 1.92 lakh crore as of 30 June 2026 (Rajya Sabha reply, via press) - up from 5 crore admissions worth Rs 61,501 crore by May 2023.

[CHART: pmjay-cumulative-milestones | PM-JAY cumulative admissions and treatment value: 5 crore (2023) to 12.69 crore admissions worth Rs 1.92 lakh crore (June 2026)]

Coverage in the broader sense is now a majority phenomenon: NFHS-6 finds 60.2% of households had at least one member covered by a health insurance or financing scheme in 2023-24 (rural 62.0%, urban 56.4%), up from 41.0% in NFHS-5 (2019-21). But "coverage" here includes hospitalisation-only schemes like PM-JAY, so it is not equivalent to comprehensive insurance. The regulator's count: about 57 crore lives were covered by health insurance in 2023-24 (roughly 45% government-sponsored, 45% group, 10% individual policies; premium Rs 1,07,681 crore), rising to 58 crore lives in 2024-25 (42.3% government, 47.4% group, 10.3% individual; premium Rs 1,17,505 crore) (IRDAI Annual Reports 2023-24 and 2024-25). The structural point sits in the small share: only about one covered life in ten holds an individual policy; the rest depend on the state or an employer.

Private insurance has meanwhile grown from 3.4% to 9.19% of total health expenditure over the decade to 2022-23, and social security expenditure (including PM-JAY) from 6% to 9.9% (NHA 2022-23).

---

## 8. The digital layer

India has built, in five years, one of the largest digital health identity systems anywhere. What it has not yet built is the layer that would make those identities clinically meaningful.

As of the 3rd ABDM Mission Steering Group meeting (10 July 2026, MoHFW):

- **93.95 crore ABHA numbers** (Ayushman Bharat Health Accounts) created;
- **over 105 crore digital health records** linked to those accounts - a mean of roughly 1.1 records per account, and the distribution is not published, so how many accounts hold zero records is unknown;
- **5.33 lakh facilities** registered on the Health Facility Registry, of which **2.72 lakh** - roughly half - have adopted ABDM-enabled software;
- **9.85 lakh professionals** on the Healthcare Professionals Registry;
- nearly **24 crore Scan & Share tokens** generated for OPD registration - in our reading, the highest-volume live patient-facing use of the ABDM rails to date.

[CHART: abdm-created-vs-used | ABDM: what has been created or registered versus what is actively used, July 2026 - 94 crore identities, ~1.1 records each, half of registered facilities transacting]

The service layer is younger still. The Unified Health Interface - the transaction layer intended to let patients discover and book services across providers - was formally launched in late June 2026, five years after ABDM itself, with four citizen services activated and no transaction volumes yet published.

The platforms that carry real volume are the vertical ones:

- **eSanjeevani** (telemedicine): more than 43 crore consultations as of 23 November 2025 (Rajya Sabha reply); more than 46.7 crore per the government's June 2026 note - a time series, not competing totals.
- **U-WIN** (immunisation registry): 17.39 crore registered beneficiaries, 3.2 crore vaccination sessions and 75.36 crore doses recorded as on 2 June 2026. What share of all national immunisation doses U-WIN captures is not published.
- **CoWIN**, the precedent for all of this: over 220 crore COVID vaccine doses administered end-to-end on one platform (16 January 2021 to 6 January 2023), with 97% of eligible beneficiaries receiving at least one dose.

[CHART: digital-platform-volumes | Cumulative volumes of the major public digital health platforms, with as-of dates - eSanjeevani, U-WIN, CoWIN, AAM footfall]

Money: the Union Budget 2026-27 allocated Rs 1,06,530.42 crore to MoHFW in total, with Rs 39,390 crore for the National Health Mission (up 6.2% on the revised estimate) and Rs 9,500 crore for PM-JAY; ABDM itself received no separately published line, described only as "enhanced" (Budget documents via DD News/PRS).

The pattern across this section is consistent and worth stating neutrally: the layer that identifies people is enormous and growing; the layer that records what happened to them clinically is thin (one record per identity, on average); and the layer that would coordinate what happens *next* - referral, follow-up, booking - launched months ago with four services. The registries know who you are. They mostly do not yet know what you need.

---

## 9. Public health programmes - and what happens after a positive screen

India's flagship NCD programme, NP-NCD, delivered through the sub-centre/PHC network and the Ayushman Arogya Mandirs (1,80,906 operational as of 31 October 2025), has screened at a scale with few parallels: cumulative screening events of 38.79 crore for hypertension, 36.05 crore for diabetes, 31.88 crore for oral cancer, 14.98 crore for breast cancer and 8.15 crore for cervical cancer (NP-NCD portal figures, Rajya Sabha reply, cumulative to 31 October 2025).

[CHART: npncd-cumulative-screenings | NP-NCD cumulative screening events by condition, to October 2025 - events, not unique people]

Now walk the steps that follow a positive screen, using every published number that exists:

1. **Screening**: 38.79 crore hypertension screening events (October 2025). Events, not people; annual re-screening is counted each time.
2. **Confirmation**: no national figure exists - not on the portal, not in parliamentary replies, not in PIB releases. The only published measurements are sub-national: 6.4% of followed-up high-risk screenees completed diagnostic confirmation in rural Andhra Pradesh (2015-16); an implementation study in northern India showed 69.6-91.2% confirmation turnout is achievable when health workers add home-based reminders (2024). Between those two numbers lies the difference between a screening programme and a detection programme, and no national data says where India currently sits.
3. **Treatment initiation**: 4.20 crore people on hypertension treatment and 2.53 crore on diabetes treatment under 75/25 (March 2025) - 89.7% of the 7.5 crore target. But treatment counts and screening counts have incompatible denominators (unique persons vs events, eight months apart), and the portal's diagnosed and under-treatment columns are identical, so initiation is recorded as an automatic consequence of diagnosis.
4. **Retention and control**: not reported by any programme system. The last national measurement is the NNMS survey - fieldwork 2017-18, before any of the current programmes scaled: of adults with hypertension, 27.9% aware, 14.5% treated, 12.6% controlled.

[CHART: ncd-post-screen-cascade-studies | Everything published about what happens after a positive NCD screen: one 2015-16 district study (6.4% confirmation), one 2019-20 block study, and national treatment counts with incompatible denominators]

The contrast with the immunisation and TB programmes is instructive, because both show the machinery *can* close loops when it is built to. Full immunisation coverage among children 12-23 months (card-based series) rose from 77.9% (NFHS-4, 2015-16) to 83.8% (NFHS-5) to 87.1% (NFHS-6, 2023-24); rotavirus coverage jumped from 36.4% to 85.4% across the last two rounds; Mission Indradhanush has vaccinated more than 5.46 crore children and 1.32 crore pregnant women across twelve phases since December 2014 (GoI NFHS-6 note, June 2026). NTEP notified about 26.2 lakh TB cases in 2024 - its highest ever, reported in the range 26.07-26.30 lakh depending on source - with 92% treatment coverage and a 90% treatment success rate (WHO Global TB Report 2025). These programmes count people, not events, and publish what happened to them at each stage. The NCD programme, as yet, does neither.

[CHART: full-immunisation-coverage-nfhs | Full immunisation coverage, children 12-23 months, card-based: 77.9% to 83.8% to 87.1% across NFHS-4/5/6]

---

## 10. What the system can and cannot answer

Everything above reduces to a short list of questions - the questions any health system must answer about the people it serves - and whether India's information systems, as publicly documented in September 2026, can answer them. Every row below is defensible from the sections cited.

| Question | Can the system answer it? | Evidence |
|---|---|---|
| **Who is this person?** | **Yes, largely.** 93.95 crore ABHA identities exist; CoWIN proved identity-linked delivery at 220-crore-dose scale. | Section 8 |
| **How many people are there to serve?** | **Not precisely.** No census since 2011; the domestic projection and the UN series differ by ~50 million. Resolution waits on Census 2027. | Section 1 |
| **What do people die of?** | **Partially.** Cause-of-death data covers only the 22% of registered deaths that are medically certified, skewed urban and hospital-based; 11.9% of even those are ill-defined. | Section 2 |
| **Who has a chronic disease?** | **In aggregate, yes; individually, mostly no.** Survey estimates exist (315M hypertension, 101M diabetes), but roughly 63% of hypertension and - depending on instrument - 26-54% of diabetes is undiagnosed. | Sections 2, 3 |
| **Was this person screened?** | **As an event, yes; as a person, no.** 38.79 crore hypertension screening events are counted; unique individuals are not distinguished from repeat screens. | Section 9 |
| **Was an abnormal result followed up?** | **Generally no.** No national confirmation or referral-completion figure exists anywhere in the published record; the only measurements are one district study (6.4%) and one block study. | Sections 3, 9 |
| **Is this person actually taking treatment?** | **No.** "Under treatment" means portal registration; the diagnosed and under-treatment columns are identical in the government's own releases. | Sections 3, 9 |
| **Is the condition controlled?** | **Only by survey, and the surveys are old.** Latest national cascade fieldwork: 2019-21 (NFHS-5) and 2017-18 (NNMS). NFHS-6 measured prevalence only. Answer then: ~8.5% of hypertension controlled. | Section 3 |
| **What did the encounter record?** | **Rarely.** 105 crore records against 94 crore identities - a mean of ~1.1 records per lifetime per person; the zero-record share is unpublished. | Section 8 |
| **Can the person afford the care?** | **For hospitalisation, increasingly; for the chronic outpatient care most people need, no.** PM-JAY covers admissions only; outpatient consultations, medicines and diagnostics - the daily cost of chronic disease - remain out of pocket, and OOP is still 43.4% of all health spending. | Section 7 |
| **Is there someone to deliver the next step?** | **At the frontline, mostly; at the referral tier, mostly not.** ANM posts are ~7% short of the norm; the rural specialist tier is 80% short. | Section 6 |
| **What should happen next for this person?** | **No.** No public system links a screening result to a confirmation, a confirmation to a treatment record, or a treatment record to an outcome. The service layer intended to coordinate care launched in mid-2026 with four services and no published volumes. | Sections 8, 9 |

The table needs no argument appended to it. A system that can identify a billion people, insure the bottom 40% for hospitalisation, and screen at the scale of continents - but cannot say whether an abnormal result was ever followed up - has a specific, describable shape. Readers can draw their own conclusions about what should be built next.

---

## 11. What we could not establish

Honesty about gaps is part of the method. The following could not be established from any retrievable primary source as of early September 2026.

**Data that does not exist (or is not published):**

- Any national figure for post-screen diagnostic confirmation, referral completion, or treatment adherence under NP-NCD. The consolidated results of the Intensified Special NCD Screening Drive (February-March 2025) were never published as an outcome release.
- Any NFHS-6-based awareness/treatment/control cascade: the fact sheets report prevalence categories only, and no unit-level analysis had been published. All cascade estimates rest on 2017-21 fieldwork.
- NFHS-6 mortality estimates: unlike NFHS-5, the fact sheets contain no infant, neonatal or under-five mortality rates; the full report with mortality tables could not be located. SRS remains the sole current mortality source.
- The distribution of linked records across ABHA accounts (how many are empty), U-WIN's completeness against all doses delivered, and any UHI transaction volumes.
- An official Indian estimate of avoidable or amenable mortality; an official active-workforce count (as opposed to registration stock with an assumed 80% availability); a verified rural-urban split of doctors; an official district-hospital shortfall against the one-per-district norm; a verified count of registered allied health professionals under NCAHP.
- A nationally representative catastrophic-health-expenditure estimate using data newer than 2017-18.
- NMHS-2 (national mental health survey covering all states): fieldwork complete, results unpublished as of September 2026.

**Contested or divergent estimates (report the range, never average):**

- India's population: ~1,411 million (domestic 2011-based projection) vs 1,463.9 million (UN WPP 2024) for 2025.
- NCD share of deaths: 61.8% (ICMR/GBD, 2016) vs 66% (WHO, 2019).
- Chronic kidney disease prevalence: 9.3% (GBD 2021) vs 16.38% (2018-23 community-study meta-analysis).
- Mental disorder prevalence: 10.6% (NMHS clinical point prevalence, 2015-16) vs 14.3% (GBD definitions, 2017).
- TFR: 1.9 (UN) vs 2.0 (NFHS-6). TB notifications 2024: 26.07-26.30 lakh depending on source.
- The demographic window "2005-06 to 2055-56": secondary attribution only; no retrievable primary document.

**Stale foundations under current claims:**

- All population denominators: 2011 census base, projections published 2020.
- The facility and staffing picture: as on 31 March 2023 (HDI 2022-23 remains the latest edition).
- The public/private utilisation split: 2017-18 (NSS 75th round), pre-COVID and pre-PM-JAY-scale.
- The canonical NCD-transition shares: 2016 data. The India YLD ranking: 2015. The TB cascade: 2013. The catastrophic-expenditure headline: 2011-12. ICMR-INDIAB prevalence: fieldwork spread over 2008-2020.
- Several primary government pages (PIB releases, some parliamentary replies) block automated retrieval; where used, figures were corroborated across multiple independent reports, and this is flagged in Section 12.

---

## 12. The data behind this

Every figure in this article comes from a dataset you can download and check. They live in
[`ihmr-engine/datasets`](https://github.com/ihmrlabs/ihmr-engine/tree/main/datasets), one folder
each, with a `SOURCE.md` recording the publisher, the URL, the date we retrieved it, and the
period the data actually covers as distinct from when it was published.

Browse them at [projectihmr.org/datasets](https://projectihmr.org/datasets), or take the whole
lot from the repository.

Two things to know before you use them. Our work on the datasets is CC BY 4.0, but **the
underlying data belongs to whoever published it** and keeps their licence, recorded in each
`SOURCE.md`. And every `Verified by` field is currently blank: retrieval and cross-checking were
automated, and a person still needs to read each one against the original. We would rather tell
you that than let you assume otherwise.

If you find an error in any of them, that is one of the most useful things you could tell us.

---

## 13. Sources

**Population and projections**

- Registrar General and Census Commissioner of India. Gazette notification S.O. 2681(E), 16 June 2025, under the Census Act 1948 (Census 2027; reference date 1 March 2027). Corroborated via India Briefing, "India's Census 2027: Key Dates and Policy Implications" (2025). https://www.india-briefing.com/news/indias-next-population-census-set-for-2027-38072.html/
- National Commission on Population, MoHFW. *Population Projections for India and States 2011-2036*, Report of the Technical Group on Population Projections (July 2020). https://nhm.gov.in/New_Updates_2018/Report_Population_Projection_2019.pdf
- UNFPA. World Population Dashboard - India (WPP 2024 revision). https://www.unfpa.org/data/world-population/IN
- UNFPA India. *India Ageing Report 2023* release. https://india.unfpa.org/en/news/india-ageing-elderly-make-20-population-2050-unfpa-report
- Ministry of Finance. *Economic Survey 2018-19*, Vol. 1, Ch. 7, "India's Demography at 2040". https://www.indiabudget.gov.in/budget2019-20/economicsurvey/doc/vol1chapter/echap07_vol1.pdf

**Surveys**

- IIPS/MoHFW. *National Family Health Survey (NFHS-6) 2023-24: India and State/UT Fact Sheets* (provisional; released 29 May 2026; excludes Manipur). https://www.nfhsiips.in/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-2024%20Fact%20Sheets.pdf
- Government of India. *NFHS-6 (2023-24): Key Findings and Long-Term Trends*, media note, 13 June 2026. https://indiainatlanta.gov.in/public_files/assets/pdf/NFHS_6_Note_for_International_Media_13062026v2.pdf
- NIMHANS/MoHFW. *National Mental Health Survey of India 2015-16: Summary*. https://indianmhs.nimhans.ac.in/phase1/Docs/Summary.pdf

**Mortality and vital statistics**

- ORGI. *SRS Based Abridged Life Tables 2020-24* (released ~May 2026). https://censusindia.gov.in/nada/index.php/catalog/47148/download/51393/SRS-Abridged_Life_Tables_2020-2024.pdf ; and *2018-22* (June 2025). https://censusindia.gov.in/nada/index.php/catalog/45566/download/49763/SRS-Abridged_Life_Tables_2018-2022.pdf
- ORGI. *SRS Statistical Report 2024* (released May 2026). https://censusindia.gov.in/nada/index.php/catalog/47152/download/51396/SRS_STAT_2024.pdf ; and *2023*. https://censusindia.gov.in/nada/index.php/catalog/46172/download/50420/SRS_STAT_2023.pdf
- ORGI. *Special Bulletin on Maternal Mortality in India 2022-24*. https://censusindia.gov.in/nada/index.php/catalog/47151/download/51395/SRS_MMR_Bulletin_2022_2024.pdf ; and *2020-22*. https://censusindia.gov.in/nada/index.php/catalog/45569/download/49766/SRS_MMR_Bulletin_2020_2022.pdf
- ORGI. *Report on Medical Certification of Cause of Death 2023* (2025). https://dc.crsorgi.gov.in/assets/download/Annual-Reports/mccd/2023.pdf
- WHO. Global Health Observatory, indicators WHOSIS_000001 (life expectancy) and WHOSIS_000002 (HALE), India. https://data.who.int/countries/356
- MoRTH. *Road Accidents in India 2024* (released June 2026; mirrored at OpenCity). https://data.opencity.in/dataset/road-accidents-in-india-2024
- Data For India. Infant mortality analysis (neonatal share of infant deaths). https://www.dataforindia.com/infant-mortality/

**Disease burden and cascades**

- ICMR/PHFI/IHME. *India: Health of the Nation's States* - Executive Summary (2017). https://www.icmr.gov.in/icmrobject/static/icmr/dist/images/pdf/reports/2017_India_State_Level_Disease_Burden_Initiative_Executive_Summary.pdf
- PIB. "Status of Non-Communicable Diseases (NCDs) in India", 8 Feb 2022 (PRID 1796435).
- The Federal, reporting WHO *Invisible Numbers* (2022): NCDs 66% of Indian deaths, 2019. https://thefederal.com/health/noncommunicable-diseases-caused-66-deaths-in-india-in-2019-who
- Anjana RM et al. ICMR-INDIAB-17, *Lancet Diabetes & Endocrinology* 2023;11(7):474-89. https://www.thelancet.com/journals/landia/article/PIIS2213-8587(23)00119-5/fulltext
- Varghese JS et al. Hypertension diagnosis, treatment, and control in India. *JAMA Network Open* 2023;6(10):e2339098. https://pmc.ncbi.nlm.nih.gov/articles/PMC10594142/
- Hypertension treatment cascade among men and women of reproductive age, NFHS-5. *Lancet Regional Health - Southeast Asia* 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10884964/
- Hypertension treatment cascade in India: NNMS. *Journal of Human Hypertension* 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC10156594/
- Varghese JS et al. National estimates of the adult diabetes care continuum in India. *JAMA Internal Medicine* 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10391358/
- Prevalence, awareness, treatment and control of diabetes: NNMS. *Frontiers in Public Health* 2022;10:748157. https://pmc.ncbi.nlm.nih.gov/articles/PMC8964146/
- ICMR-INDIAB-13: treatment targets in self-reported diabetes. *Lancet Diabetes & Endocrinology* 2022. https://www.thelancet.com/journals/landia/article/PIIS2213-8587(22)00072-9/abstract
- Diabetes in adults 45+ (LASI). *Lancet Global Health* 2025;13(9). https://pmc.ncbi.nlm.nih.gov/articles/PMC12397963/
- Subbaraman R et al. The tuberculosis cascade of care in India's public sector. *PLoS Medicine* 2016;13(10):e1002149. https://pubmed.ncbi.nlm.nih.gov/27780217/
- Are people at high risk for diabetes visiting health facilities for confirmation? *Global Health Action* 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5769807/
- Assessment of NPCDCS in rural Jaipur. *Journal of Family Medicine and Primary Care* 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9648218/
- GBD 2016 CVD in India. *Lancet Global Health* 2018. https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(18)30407-8/fulltext
- GBD 2016 chronic respiratory diseases in India. *Lancet Global Health* 2018. https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(18)30409-1/fulltext
- CKD burden, GBD 2021. *International Urology and Nephrology* 2025 (online). https://link.springer.com/article/10.1007/s11255-025-04987-0 ; CKD meta-analysis, *Nephrology* 2025. https://onlinelibrary.wiley.com/doi/10.1111/nep.14420
- Sathishkumar K et al. Cancer incidence estimates for 2022 and projection for 2025, NCRP. *Indian Journal of Medical Research* 2022;156(4&5):598-607. https://ijmr.org.in/cancer-incidence-estimates-for-2022-projection-for-2025-result-from-national-cancer-registry-programme-india/
- Burden of mental disorders across the states of India, GBD 1990-2017. *Lancet Psychiatry* 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7029418/
- GBD 2015 YLD paper. https://pmc.ncbi.nlm.nih.gov/articles/PMC5055577/ ; GBD 2021, *The Lancet* 2024. https://www.sciencedirect.com/science/article/pii/S0140673624007578
- Kulothungan V et al. Premature NCD mortality projections (ICMR-NCDIR), *Sustainable Development* 2024, via Down to Earth. https://www.downtoearth.org.in/health/india-won-t-meet-un-targets-to-reduce-premature-mortality-from-major-non-communicable-diseases-icmr-ncdir-92475
- PIB, citing WHO Global TB Report 2025 (PRID 2189415, 12 Nov 2025). https://www.pib.gov.in/PressReleasePage.aspx?PRID=2189415

**Delivery and workforce**

- MoHFW. *Health Dynamics of India (Infrastructure and Human Resources) 2022-23* (published 2024; archived copy). https://web.archive.org/web/20260221012414/https://mohfw.gov.in/sites/default/files/Health%20Dynamics%20of%20India%20%28Infrastructure%20%26%20Human%20Resources%29%202022-23_RE%20%281%29.pdf ; summary: PIB PRID 2053070.
- PRS Legislative Research. *Demand for Grants Analysis: Health and Family Welfare*, 2025-26 and 2026-27. https://prsindia.org/files/budget/budget_parliament/2025/DFG_Analysis_2025-26-Health.pdf ; https://prsindia.org/files/budget/budget_parliament/2026/DfG_Analysis_2026-27-Health.pdf
- MoHFW. *Annual Report 2024-25*, Department of Health & Family Welfare. https://www.mohfw-dohfw.gov.in/static/uploads/2025/09/45b06af4508a53a059c74efc930d955e.pdf
- MoHFW/PIB. *Initiatives & Achievements 2025* (year-end review, January 2026). https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/jan/doc202611749801.pdf
- PIB releases: AAM update (PRID 2151239); health workforce availability (PRID 2225755, 10 Feb 2026); Anganwadi workers (PRID 2003433, 7 Feb 2024).

**Financing**

- NHSRC/MoHFW. *National Health Accounts Estimates for India 2022-23* (May 2026); PIB PRID 2265816. https://nhsrcindia.org/sites/default/files/2026-05/NHA%202022-23%20Report.pdf
- Selvaraj S, Farooqui HH, Karan A. *BMJ Open* 2018;8(5):e018020. https://pmc.ncbi.nlm.nih.gov/articles/PMC5988077/
- Soni A et al. *Frontiers in Public Health* 2026, doi:10.3389/fpubh.2026.1762886.
- PIB. *Six Years of Ayushman Bharat PM-JAY* backgrounder (23 Sep 2024). https://www.pib.gov.in/PressNoteDetails.aspx?NoteId=153181&ModuleId=3&reg=3&lang=1
- Rajya Sabha replies on PM-JAY, July-August 2026, via Daily Pioneer (28 July 2026) https://dailypioneer.com/news/over-44-73-crore-ayushman-cards-created-under-ab-pmjay-govt and Morung Express (4 Aug 2026) https://morungexpress.com/ab-pmjay-enables-1269-crore-cashless-hospital-admissions-worth-rs-192-lakh-crore-govt (press reports of parliamentary replies; original PDFs not retrievable).
- IRDAI. *Annual Report 2023-24* (Dec 2024) and *Annual Report 2024-25* (Dec 2025). https://irdai.gov.in/annual-reports

**Digital health and programmes**

- MoHFW/NHA. 3rd ABDM Mission Steering Group meeting readout, 10 July 2026, via GKToday (PIB page blocks automated retrieval; corroborated across multiple outlets). https://www.gktoday.in/ayushman-bharat-digital-mission-crosses-93-95-crore-health-accounts/
- PIB. UHI launch (PRID 2278987), via Digital Health News. https://www.digitalhealthnews.com/jp-nadda-launches-unified-health-interface-for-seamless-healthcare-access
- eSanjeevani Rajya Sabha reply, via Digital Health News. https://www.digitalhealthnews.com/esanjeevani-crosses-43-crore-consultations-as-india-strengthens-digital-health-network
- Economic Survey 2022-23 CoWIN figures (PIB PRID 1894907). https://www.pib.gov.in/PressReleasePage.aspx?PRID=1894907&reg=3&lang=2
- NP-NCD and AAM Rajya Sabha replies, via DD News. https://ddnews.gov.in/en/india-operationalizes-1-8-lakh-ayushman-arogya-mandirs-over-130-crore-ncd-screenings-complete/
- 75/25 initiative: PIB PRID 2110390 (11 Mar 2025) https://www.pib.gov.in/PressReleasePage.aspx?PRID=2110390 and Medical Dialogues. https://health.medicaldialogues.in/health-topics/metabolic-health/government-treats-over-42-million-hypertension-25-million-diabetes-patients-under-75-by-25-initiative-144777
- PIB. "Steps taken to Control Hypertension and Diabetes" (PRID 2155451, 12 Aug 2025). https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2155451
- Union Budget 2026-27 health allocations, via DD News. https://ddnews.gov.in/en/union-budget-2026-27-health-ministry-gets-%E2%82%B91-06-lakh-crore-allocation/
- WHO Global TB Report 2025 India figures, via Drishti IAS. https://www.drishtiias.com/daily-updates/daily-news-analysis/who-global-tuberculosis-tb-report-2025

*Retrieval note: PIB and some MoHFW pages return HTTP 403 to automated fetching. Wherever a PIB-sourced figure appears above, it was verified either by direct retrieval, through the search index of the release itself, or through at least two independent secondary reports, and the finding is flagged accordingly in the text.*

---

*Prepared for IHMR, September 2026. Corrections and additions are welcome; every claim above is intended to be checkable against the sources listed.*
