# 🚀 Data Refinery: Cleaning 500k+ Online Retail Transactions

**Developed by Fahri-Dataworks**

## 💡 Project Logic

Most "data cleaning" tutorials just show how to fill NaNs. In a real-world business context, it’s much messier. This project is a professional workflow for handling high-volume retail datasets. I didn't just strip out bad data; I structured it so that a CFO could actually trust the final revenue numbers.

## 🛠️ Engineering Decisions (The "Why")

- **Handling the 'C' Prefix:** Isolated transactions with a 'C' prefix (Cancellations) to allow for accurate Gross vs. Net revenue calculation instead of simply deleting them.
- **The CustomerID Dilemma:** Removed records with missing CustomerIDs to prevent ghost-customer bias in Loyalty Analysis and Retention KPIs.
- **Numerical Downcasting:** Converted data types (e.g., float64 to float32). This optimization cut RAM usage by over 60%, critical for deployment on cost-effective cloud instances.

## 📂 Project Architecture

- `scripts/`: Contains `cleaner.py` (Core ETL logic).
- `data/`: Local storage for raw inputs and refined outputs (Excluded from Git for security).
- `requirements.txt`: Project dependency manifest.

## 📊 Real-World Processing Results

- **Initial Records Ingested:** 541,909
- **Final Refined Records:** 397,884
- **Data Noise Removed:** ~144,025 records
- **Optimization:** Memory-efficient processing via numerical downcasting.

## 🚀 How to Run

1. **Clone**: `git clone https://github.com/fahri-dataworks/business-data-cleaning.git`
2. **Install**: `pip install -r requirements.txt`
3. **Run**: `python scripts/cleaner.py`

## 📩 Let's Talk Business

I am available for freelance data engineering and automation projects.

- **Upwork:** [View My Freelancer Profile](https://www.upwork.com/freelancers/~017c3d7b28f4181c81)
- **Email:** fahriramadhanidris6@gmail.com

> "I don't just clean data; I prepare it for high-stakes business decisions."
