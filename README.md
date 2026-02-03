# 🇮🇳 UIDAI Operational Intelligence Center (Project: Ghost-Buster)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uidai-hackathon-2026-by-jeevan-kumar-qmgthsawuappb5rv9nqxjcj.streamlit.app)
[![Watch the Video Demo](https://img.shields.io/badge/📺_Watch_Video_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/UYScKyTWv6M)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Hackathon%20Submission-success)]()

> **"Shifting Aadhaar Integrity from Reactive Complaints to Proactive Intelligence."**

---

##Table of Contents
- [Problem Statement](#-problem-statement)
- [Proposed Solution](#-proposed-solution)
- [Key Investigation: The "Ghost Center" Discovery](#-key-investigation-the-ghost-center-discovery)
- [Real-World Impact](#-real-world-impact)
- [Tech Stack](#-tech-stack)
- [Live Demo & Screenshots](#-live-demo--screenshots)
- [Installation & Setup](#-installation--setup)
- [Algorithmic Logic](#-algorithmic-logic)
- [Future Roadmap](#-future-roadmap)
- [Author](#-author)

---

##Problem Statement
The Aadhaar ecosystem handles millions of transactions daily. While enrolment saturation is high, a critical vulnerability exists: **Fraudulent Enrolment Centers ("Ghost Centers").**

These rogue operators:
1.  **Farm "Biometric Updates"** (which are faster and less scrutinized) to hijack accounts or launder money.
2.  **Report Zero "New Enrolments"** (avoiding the rigorous new-user verification process).
3.  **Burn Government Resources** and compromise data integrity.

**The Challenge:** Detecting these anomalies in a dataset of billions of rows is like finding a needle in a haystack.

---

##Proposed Solution
I have developed the **UIDAI Operational Intelligence Center**—a real-time, AI-driven dashboard that ingests Enrolment, Biometric, and Demographic data to flag anomalies instantly.

### Key Features:
* ** Geospatial Heatmaps:** Instantly visualize "Hot Zones" of suspicious activity on an interactive map.
* ** The "Suspicion Score":** A custom statistical metric that ranks every Pincode in India by fraud probability.
* ** Trend Analysis:** Compare "Healthy" vs. "Anomalous" center behavior over time.

---

##  Key Investigation: The "Ghost Center" Discovery
During my analysis for the UIDAI Hackathon 2026, the algorithm flagged a massive anomaly in **South West Delhi**.

| Metric | Normal Center | **⚠️ Pincode 110086 (Identified Anomaly)** |
| :--- | :--- | :--- |
| **Biometric Updates** | ~150 - 500 / month | **7,625 / month** |
| **New Enrolments** | ~50 - 200 / month | **0 (Zero)** |
| **Suspicion Score** | < 10.0 | **7,625.0 (Critical Risk)** |

---

## Real-World Impact
This is not just a theoretical project. I have formally reported this specific anomaly to UIDAI officials for immediate investigation.

* **Official Case ID 1:** `SRN-S2054469731000`
* **Official Case ID 2:** `SRN-S2019698585000`

---

## Tech Stack
This project was built using a high-performance Data Science stack:
* **Frontend:** [Streamlit](https://streamlit.io/) (for rapid, interactive dashboarding)
* **Data Processing:** [Pandas](https://pandas.pydata.org/) (Data merging & aggregation)
* **Visualization:** [Plotly Express](https://plotly.com/python/plotly-express/) (Geospatial mapping & interactive charts)
* **Deployment:** Streamlit Community Cloud

---

## Live Demo & Screenshots

### [ Click Here to View Live Dashboard](https://uidai-hackathon-2026-by-jeevan-kumar-qmgthsawuappb5rv9nqxjcj.streamlit.app)

---

## 🎥 Video Demonstration
A complete walkthrough of the project, including the Problem Statement, Live Dashboard Demo, Scalability Test (on 2.9 Million Records), and Proof of Real-World Action (UIDAI Grievance Reporting).

### **👇 Click the button below to watch on YouTube**
[![Watch the Video Demo](https://img.shields.io/badge/📺_Watch_Video_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/UYScKyTWv6M)

*(Duration: 2:05 minutes)*

#### 1. The Operational Dashboard
Check screenshots folder
*Real-time metrics showing total updates vs. enrolments.*

#### 2. The "Ghost Center" Detection (Map View)
Check screenshots folder
*Red dots indicate high-risk pincodes with massive updates but zero enrolments.*


---

## Installation & Setup

### 1. Clone the Repository

git clone [https://github.com/Jeevang1-epic/UIDAI-Hackathon-2026-BY-JEEVAN-KUMAR.git](https://github.com/Jeevang1-epic/UIDAI-Hackathon-2026-BY-JEEVAN-KUMAR.git)
cd UIDAI-Hackathon-2026-BY-JEEVAN-KUMAR

2. Install Dependencies
pip install -r requirements.txt

3. Generate the Data
(I use a synthetic data generator to mimic the UIDAI dataset structure for privacy)
python data_setup.py

4. Run the Dashboard
streamlit run dashboard.py

## Algorithmic Logic
I define a Suspicion Score S for every location L to normalize fraud risk:
S_L = Total Biometric Updates/Total New Enrolments + 1

* **If S < 10:** Normal Operation (Balanced mix of services).
* **If S > 100:** High Risk (Investigation recommended).
* **If S > 1000:** **CRITICAL ANOMALY** (Immediate suspension recommended).


## Future Roadmap
* **Phase 1 (Current):** Statistical Rule-Based Detection.
* **Phase 2:** Integration of **Unsupervised Machine Learning (Isolation Forests)** to detect subtler fraud patterns.
* **Phase 3:** Real-time API integration with UIDAI's live server for T+0 detection.

---

## Team
**Team ID:** UIDAI_11980
* **Jeevan Kumar** - *Lead Developer & Data Analyst*

---

*"Built with 🇮🇳 for a safer Digital India."*
