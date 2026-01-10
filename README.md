# Data Refinery: Cleaning 500k+ Online Retail Transactions

**Developed by Fahri-Dataworks**

## Project Logic

Most "data cleaning" tutorials just show how to fill NaNs. In a real-world business context, it’s much messier. This project is my personal workflow for handling a high-volume retail dataset. I didn't just strip out bad data; I structured it so that a CFO could actually trust the final revenue numbers.

## Engineering Decisions (The "Why")

During the development, I made several specific technical choices to ensure data integrity:

- **Handling the 'C' Prefix:** I noticed that thousands of transactions had a 'C' prefix in the `InvoiceNo`. Many beginners just delete these. I chose to isolate them into a "Returns" category to allow for accurate Gross vs. Net revenue calculation.
- **The CustomerID Dilemma:** Roughly 25% of the data had missing `CustomerID`. Instead of guessing or using a mean, I dropped these for the "Loyalty Analysis" version of the data, as ghost-customers skew retention KPIs.
- **Memory Management:** I manually downcast `float64` to `float32` and `int64` to `int32`. It’s a small step that cut RAM usage by over 60%, which is critical if you're deploying this on a small cloud instance.

## Key Metrics Post-Refinery

- **Input Rows:** 541,909
- **Valid Business Records:** 406,829 (After stripping noise, tests, and non-customer logs)
- **Memory Footprint:** Reduced from ~98MB to ~30MB.
- **Integrity:** Verified 0% duplicates and 100% timestamp consistency.

## How to Run This

I've kept the setup simple. No complex Docker needed for now, just standard Python.

1.  Clone: `git clone https://github.com/fahri-dataworks/business-data-cleaning.git`
2.  Install: `pip install pandas`
3.  Run: `python cleaner.py`

## Portfolio Context

I built this to solve a common problem: E-commerce data that looks good on the surface but is financially inaccurate. This pipeline ensures that when you run a "Top 10 Products" report, you aren't seeing "Postage" or "Bank Fees" at the top of your list.

---

---

## 📩 Let's Talk Business

I am available for freelance data engineering and automation projects.

- **Upwork:** [View My Freelancer Profile]https://www.upwork.com/freelancers/~017c3d7b28f4181c81

- **Email:** fahriramadhanidris6@gmail.com

> "I don't just clean data; I prepare it for high-stakes business decisions."
