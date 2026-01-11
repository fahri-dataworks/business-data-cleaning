



# 🚀 Data Refinery: Cleaning 540K+ Online Retail Transactions

**Developed by Fahri – Dataworks**

## 💡 Project Overview

Most *“data cleaning”* tutorials stop at filling missing values.
In real-world **retail and finance environments**, data preparation is far more complex and risky.

This project demonstrates a **production-grade, business-aware ETL pipeline** for processing high-volume online retail transactions.
The goal is not simply to remove bad records, but to **preserve financial accuracy, auditability, and executive-level reporting integrity**.

The output dataset is suitable for:

* Revenue reporting
* Customer analytics
* Cohort, retention, and CLV modeling
* Executive dashboards

---

## 🛠️ Engineering Decisions (The “Why”)

### 1️⃣ Cancellation-Aware Revenue Logic

Invoices starting with `C` indicate **cancellations or returns**.
These are **flagged instead of deleted** so that:

* Gross revenue
* Net revenue
* Refund impact

can be accurately calculated and audited.

### 2️⃣ Customer Identity Integrity

Rows without `CustomerID` are removed.
This prevents **ghost customers** that would distort:

* Retention rates
* Loyalty metrics
* Lifetime value calculations

Only identifiable customers are included in customer-level analytics.

### 3️⃣ Sales Validity Rules

For non-cancelled invoices:

* `Quantity` must be positive
* `UnitPrice` must be positive

This removes:

* Zero-value transactions
* Data entry errors
* Negative revenue noise

### 4️⃣ Memory-Efficient Processing

Numerical columns are **downcast** (e.g., `float64 → float32`) to:

* Reduce RAM usage
* Allow processing on low-cost machines
* Maintain analytical precision

This makes the pipeline **cloud-friendly and scalable**.

---

## 📂 Project Architecture

```
business-data-cleaning/
│
├── scripts/
│   └── cleaner.py        # Core ETL & business logic
│
├── data/                # Raw & cleaned data (gitignored)
│
├── requirements.txt     # Python dependencies
│
└── README.md
```

---

## 📊 Real-World Processing Results

| Metric                     | Value                 |
| -------------------------- | --------------------- |
| Initial Records            | 541,909               |
| Final Refined Records      | 406,789               |
| Records Removed / Isolated | ~135,000              |
| Output Format              | Analysis-ready CSV    |
| Execution                  | VS Code + Python venv |

The removed records are either:

* Cancellations (retained but flagged), or
* Invalid for customer & revenue analytics

Nothing important is blindly deleted.

---

## 📌 Sample Output (Post-ETL)

| InvoiceNo | Quantity | UnitPrice | CustomerID | Is_Cancelled |
| --------- | -------- | --------- | ---------- | ------------ |
| 536365    | 6        | 2.55      | 17850      | False        |
| C536379   | -1       | 4.25      | 17850      | True         |
| 536370    | 2        | 3.75      | 12583      | False        |

> Cancellation rows are preserved so finance teams can reconcile gross vs net revenue.

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/fahri-dataworks/business-data-cleaning.git
cd business-data-cleaning
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the ETL pipeline

```bash
python scripts/cleaner.py
```

All transformations are logged and fully auditable in the terminal.

---

## 📩 Let’s Talk Business

I am available for **freelance data engineering, ETL automation, and business-critical analytics projects**.

* **Upwork:** [https://www.upwork.com/freelancers/~017c3d7b28f4181c81](https://www.upwork.com/freelancers/~017c3d7b28f4181c81)
* **Email:** [fahriramadhanidris6@gmail.com](mailto:fahriramadhanidris6@gmail.com)
* **GitHub:** [https://github.com/fahri-dataworks](https://github.com/fahri-dataworks)

> *“I don’t just clean data — I prepare it for high-stakes business decisions.”*
