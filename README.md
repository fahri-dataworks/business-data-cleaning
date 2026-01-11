# 🚀 Data Refinery: Cleaning 500k+ Online Retail Transactions

**Developed by Fahri – Dataworks**

## 💡 Project Logic

Most data cleaning examples stop at filling missing values. In real-world business environments, high-volume transactional data is far messier. This project demonstrates a professional, production-oriented workflow for refining large-scale retail datasets.

Rather than blindly removing problematic rows, the data was structured using explicit business rules so that financial outputs — especially revenue figures — can be trusted by decision-makers such as finance leaders and executives.

## 🛠️ Engineering Decisions (The “Why”)

* **Handling the ‘C’ Prefix (Cancellations):**
  Transactions with a ‘C’ prefix were explicitly isolated and flagged instead of being deleted. This preserves financial traceability and enables accurate Gross vs Net revenue reporting.

* **The CustomerID Dilemma:**
  Records with missing CustomerID values were removed to prevent ghost-customer bias in loyalty, cohort, and retention analyses. This ensures customer-level KPIs are based only on identifiable entities.

* **Numerical Downcasting:**
  Numerical columns were converted to more memory-efficient data types (e.g., float64 → float32). This significantly reduced the dataset’s memory footprint, enabling processing on cost-effective cloud or local environments without sacrificing analytical reliability.

## 📂 Project Architecture

* `scripts/` — Contains `cleaner.py` (core data cleaning and transformation logic)
* `data/` — Local storage for raw inputs and refined outputs (excluded from version control)
* `requirements.txt` — Project dependency manifest

## 📊 Real-World Processing Results

* **Initial Records Ingested:** 541,909
* **Final Refined Records:** 397,884
* **Data Noise Removed:** ~144,025 records
* **Output:** Business-ready, memory-efficient retail transaction dataset

## 🚀 How to Run

1. **Clone**

   ```bash
   git clone https://github.com/fahri-dataworks/business-data-cleaning.git
   ```
2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Pipeline**

   ```bash
   python scripts/cleaner.py
   ```

## 📩 Let’s Talk Business

I am available for freelance data engineering, data cleaning, and automation projects involving high-volume or business-critical datasets.

* **Upwork:** View My Freelancer Profile
* **Email:** [fahriramadhanidris6@gmail.com](mailto:fahriramadhanidris6@gmail.com)

> “I don’t just clean data — I prepare it for real business de
