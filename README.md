# 🚀 Data Refinery: Cleaning 540K+ Online Retail Transactions

**Developed by Fahri – Dataworks**

## 💡 Project Logic

 HEAD
Most data cleaning examples stop at filling missing values. In real-world business environments, high-volume transactional data is far messier. This project demonstrates a professional, production-oriented workflow for refining large-scale retail datasets.
=======
Most "data cleaning" tutorials stop at filling missing values. In real-world retail and finance contexts, data preparation is far more complex. This project demonstrates a **professional, business-aware ETL workflow** for handling high-volume online retail transaction data.

The goal is not merely to remove bad records, but to **preserve financial accuracy and auditability**, ensuring the final dataset can be confidently used for revenue reporting, customer analytics, and executive decision-making.
 eed8a23 (Add production-ready ETL pipeline with documented Kaggle dataset samples)

Rather than blindly removing problematic rows, the data was structured using explicit business rules so that financial outputs — especially revenue figures — can be trusted by decision-makers such as finance leaders and executives.
 HEAD
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
=======
- **Cancellation-Aware Logic (`InvoiceNo` with `C` prefix)**
  Transactions marked as cancellations are explicitly flagged instead of deleted, enabling accurate **Gross vs Net revenue reconciliation**.

- **Customer Identity Integrity**
  Records with missing `CustomerID` values are removed to prevent ghost-customer bias in **Retention, Loyalty, and CLV analysis**.

- **Sales Validity Rules**
  Non-cancelled transactions are required to have positive `Quantity` and `UnitPrice`, eliminating zero-value and negative-value revenue noise.

- **Memory-Conscious Processing**
  Numerical columns are downcast to optimal data types to reduce memory usage and allow execution on cost-efficient local or cloud environments.

## 📂 Project Architecture

- `scripts/` — Contains `cleaner.py` (core ETL and business logic)
- `data/` — Local storage for raw inputs and refined outputs (excluded from Git for security)
- `requirements.txt` — Python dependency manifest

## 📊 Real-World Processing Results

- **Initial Records Ingested:** 541,909
- **Final Refined Records:** 406,789
- **Data Noise Removed / Isolated:** ~135,000 records
- **Execution Environment:** VS Code + Python Virtual Environment
- **Output Format:** Analysis-ready CSV

## 🚀 How to Run

1. **Clone Repository**

   ```bash
   git clone https://github.com/fahri-dataworks/business-data-cleaning.git
   cd business-data-cleaning
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the ETL Pipeline**

   ```bash
   python3 scripts/cleaner.py
   ```

All processing steps are logged and fully auditable via terminal output.

## 📌 Sample Output (Post-ETL)

| InvoiceNo | Quantity | UnitPrice | CustomerID | Is_Cancelled |
| --------- | -------- | --------- | ---------- | ------------ |
| 536365    | 6        | 2.55      | 17850      | False        |
| C536379   | -1       | 4.25      | 17850      | True         |
| 536370    | 2        | 3.75      | 12583      | False        |

> Cancellation records are intentionally retained for financial reconciliation and reporting accuracy.

## 📩 Let’s Talk Business

I am available for **freelance data engineering, ETL automation, and analytics projects**.

- **Upwork:** [https://www.upwork.com/freelancers/~017c3d7b28f4181c81](https://www.upwork.com/freelancers/~017c3d7b28f4181c81)
- **Email:** [fahriramadhanidris6@gmail.com](mailto:fahriramadhanidris6@gmail.com)
- **GitHub:** [https://github.com/fahri-dataworks](https://github.com/fahri-dataworks)

> _"I don’t just clean data — I prepare it for high-stakes business decisions."_
 eed8a23 (Add production-ready ETL pipeline with documented Kaggle dataset samples)
