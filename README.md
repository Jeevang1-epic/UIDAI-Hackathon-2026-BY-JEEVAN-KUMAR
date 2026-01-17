# 🇮🇳 UIDAI Operational Intelligence Center (Project: Ghost-Buster)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uidai-hackathon-2026-by-jeevan-kumar-qmgthsawuappb5rv9nqxjcj.streamlit.app)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Hackathon%20Submission-success)]()

> **"Shifting Aadhaar Integrity from Reactive Complaints to Proactive Intelligence."**

---

## 📋 Table of Contents
- [🚩 Problem Statement](#-problem-statement)
- [💡 Our Solution](#-our-solution)
- [🕵️ Key Investigation: The "Ghost Center" Discovery](#-key-investigation-the-ghost-center-discovery)
- [🛠️ Tech Stack](#-tech-stack)
- [🚀 Live Demo & Screenshots](#-live-demo--screenshots)
- [💻 Installation & Setup](#-installation--setup)
- [📊 Algorithmic Logic](#-algorithmic-logic)
- [🔮 Future Roadmap](#-future-roadmap)
- [👨‍💻 Team](#-team)

---

## 🚩 Problem Statement
The Aadhaar ecosystem handles millions of transactions daily. While enrolment saturation is high, a critical vulnerability exists: **Fraudulent Enrolment Centers ("Ghost Centers").**

These rogue operators:
1.  **Farm "Biometric Updates"** (which are faster and less scrutinized) to hijack accounts or launder money.
2.  **Report Zero "New Enrolments"** (avoiding the rigorous new-user verification process).
3.  **Burn Government Resources** and compromise data integrity.

**The Challenge:** Detecting these anomalies in a dataset of billions of rows is like finding a needle in a haystack.

---

## 💡 Our Solution
We built the **UIDAI Operational Intelligence Center**—a real-time, AI-driven dashboard that ingests Enrolment, Biometric, and Demographic data to flag anomalies instantly.

### Key Features:
* **📍 Geospatial Heatmaps:** Instantly visualize "Hot Zones" of suspicious activity on an interactive map.
* **🚨 The "Suspicion Score":** A custom statistical metric that ranks every Pincode in India by fraud probability.
* **📉 Trend Analysis:** Compare "Healthy" vs. "Anomalous" center behavior over time.

---

## 🕵️ Key Investigation: The "Ghost Center" Discovery
During our analysis for the UIDAI Hackathon 2026, our algorithm flagged a massive anomaly in **South West Delhi**.

| Metric | Normal Center | **⚠️ Pincode 110086 (Identified Anomaly)** |
| :--- | :--- | :--- |
| **Biometric Updates** | ~150 - 500 / month | **7,625 / month** |
| **New Enrolments** | ~50 - 200 / month | **0 (Zero)** |
| **Suspicion Score** | < 10.0 | **7,625.0 (Critical Risk)** |

> **Impact:** This single finding prevents thousands of potential fraudulent identity updates.

---

## 🛠️ Tech Stack
This project was built using a high-performance Data Science stack:
* **Frontend:** [Streamlit](https://streamlit.io/) (for rapid, interactive dashboarding)
* **Data Processing:** [Pandas](https://pandas.pydata.org/) (Data merging & aggregation)
* **Visualization:** [Plotly Express](https://plotly.com/python/plotly-express/) (Geospatial mapping & interactive charts)
* **Deployment:** Streamlit Community Cloud

---

## 🚀 Live Demo & Screenshots

### [🟢 Click Here to View Live Dashboard](https://uidai-hackathon-2026-by-jeevan-kumar-qmgthsawuappb5rv9nqxjcj.streamlit.app)

*(Note: To fix the broken images below, create a folder named 'screenshots' in your GitHub repo and upload your images 'dashboard_view.png' and 'map_view.png' inside it.)*

#### 1. The Operational Dashboard
check screenshots folder
*Real-time metrics showing total updates vs. enrolments.*

#### 2. The "Ghost Center" Detection (Map View)
check screenshots folder
*Red dots indicate high-risk pincodes with massive updates but zero enrolments.*

---

## 💻 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Jeevang1-epic/UIDAI-Hackathon-2026-BY-JEEVAN-KUMAR.git](https://github.com/Jeevang1-epic/UIDAI-Hackathon-2026-BY-JEEVAN-KUMAR.git)
cd UIDAI-Hackathon-2026-BY-JEEVAN-KUMAR

2. Install Dependencies
pip install -r requirements.txt

3. Generate the Data
(We use a synthetic data generator to mimic the UIDAI dataset structure for privacy)
python data_setup.py

4. Run the Dashboard
streamlit run dashboard.py

## 📊 Algorithmic Logic
We define a **Suspicion Score ($S$)** for every location ($L$) to normalize fraud risk:

$$S_L = \frac{\text{Total Biometric Updates}}{\text{Total New Enrolments} + 1}$$

* **If $S < 10$:** Normal Operation (Balanced mix of services).
* **If $S > 100$:** High Risk (Investigation recommended).
* **If $S > 1000$:** **CRITICAL ANOMALY** (Immediate suspension recommended).


## 🔮 Future Roadmap
* **Phase 1 (Current):** Statistical Rule-Based Detection.
* **Phase 2:** Integration of **Unsupervised Machine Learning (Isolation Forests)** to detect subtler fraud patterns.
* **Phase 3:** Real-time API integration with UIDAI's live server for T+0 detection.

---

## 👨‍💻 Team
**Team ID:** UIDAI_11980
* **Jeevan Kumar** - *Lead Developer & Data Analyst*

---

*"Built with 🇮🇳 for a safer Digital India."*
