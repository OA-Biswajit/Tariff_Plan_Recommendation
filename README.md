# PriceApp (npn-hackthon)

A Decision Tree-based tariff plan recommendation system for telecom customers.

**Live App:** https://tariffplanrecommendation.streamlit.app/

## Overview

This project uses machine learning to recommend optimal tariff plans to telecom customers based on their usage patterns (minutes, calls, international usage, voicemail, etc.).

- **Model:** Decision Tree Classifier
- **Purpose:** Segment customers and recommend tailored pricing plans
- **Framework:** Streamlit (web UI) + Scikit-learn (ML)

## Project Structure

```
├── main.py                      # Streamlit app entry point
├── EDA_Biswajit.ipynb          # Exploratory Data Analysis
├── Final_good_Recom.ipynb      # Full analysis & recommendation pipeline
├── tariff_recomend.pkl         # Pre-trained Decision Tree model
├── requirements.txt            # Python dependencies
├── page_photo.png             # UI asset
└── README.md
```

## Requirements

- Python 3.10+
- See `requirements.txt` for dependencies

## Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
source .venv/Scripts/activate  # on Windows (bash)
# or: source .venv/bin/activate  # on Unix-like
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the App

### Streamlit Web UI

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`.

**Navigation:**
- **Home** - Project overview
- **About** - Model details and input features
- **Prediction** - Enter customer usage data to get a tariff recommendation

### Jupyter Notebooks

```bash
jupyter notebook
```

- `EDA_Biswajit.ipynb` - Data exploration and visualization
- `Final_good_Recom.ipynb` - Complete ML pipeline with clustering and recommendations

## Sample Login Credentials (if enabled)

If login is active in the app:
- **Mobile Number:** `382-4657`
- **Password:** `pass123`

## Features

- **Customer Segmentation:** Identifies 11+ distinct customer segments based on usage patterns
- **Outlier Detection:** Uses Autoencoder and IQR methods for anomaly detection
- **Plan Recommendations:** Top 3 tailored tariff plans per customer segment
- **Cluster Analysis:** K-Means, DBSCAN, and Agglomerative clustering methods

## Model Output

The model returns:
- **Cluster ID** - Customer segment (0-19)
- **Top 3 Recommended Plans** - Plan name + monthly price (₹)

Example:
```
✅ Recommended Tariff Plan: 5
Top 3 Recommended Plans:
- Basic Saver: ₹199
- Basic Global: ₹299
- Standard: ₹399
```
