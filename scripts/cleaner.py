import os
import logging
import numpy as np
import pandas as pd

# =============================
# Professional Logging Config
# =============================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class DataRefinery:
    """
    Enterprise-grade ETL Pipeline for Retail Transaction Data
    Focus: financial integrity, traceability, and memory efficiency
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df: pd.DataFrame | None = None

    # -----------------------------
    # 1. Data Ingestion
    # -----------------------------
    def load_source_data(self) -> None:
        """Load Excel or CSV source data with validation."""
        if not os.path.exists(self.file_path):
            logging.error(f"Source file not found: {self.file_path}")
            return

        try:
            ext = os.path.splitext(self.file_path)[1].lower()

            if ext == '.xlsx':
                logging.info("Excel source detected. Loading via openpyxl...")
                self.df = pd.read_excel(self.file_path)
            else:
                logging.info(
                    "CSV source detected. Auto-detecting delimiter...")
                self.df = pd.read_csv(
                    self.file_path,
                    encoding='ISO-8859-1',
                    sep=None,
                    engine='python',
                    on_bad_lines='warn'
                )

            logging.info(f"Ingested {len(self.df):,} raw records")

        except Exception as e:
            logging.exception(f"Data ingestion failed: {e}")

    # -----------------------------
    # 2. Business Logic & Cleaning
    # -----------------------------
    def apply_business_logic(self) -> None:
        """Apply business-grade validation and cleaning rules."""
        if self.df is None or self.df.empty:
            logging.warning("No data available to process")
            return

        initial_rows = len(self.df)

        # ---- Identity Integrity ----
        self.df = self.df.dropna(subset=['CustomerID'])

        # ---- Cancellation Identification ----
        if 'InvoiceNo' in self.df.columns:
            self.df['Is_Cancelled'] = (
                self.df['InvoiceNo']
                .astype(str)
                .str.startswith('C')
            )
        else:
            self.df['Is_Cancelled'] = False

        # ---- Financial Validation ----
        valid_sales = (
            (~self.df['Is_Cancelled']) &
            (self.df['Quantity'] > 0) &
            (self.df['UnitPrice'] > 0)
        )

        # Keep clean sales + all cancellations (for net vs gross analysis)
        self.df = self.df[valid_sales | self.df['Is_Cancelled']]

        # ---- Memory Optimization ----
        before_mem = self.df.memory_usage(deep=True).sum() / 1024**2

        self.df['UnitPrice'] = pd.to_numeric(
            self.df['UnitPrice'], errors='coerce', downcast='float'
        )
        self.df['Quantity'] = pd.to_numeric(
            self.df['Quantity'], errors='coerce', downcast='integer'
        )
        self.df['CustomerID'] = pd.to_numeric(
            self.df['CustomerID'], errors='coerce', downcast='integer'
        )

        after_mem = self.df.memory_usage(deep=True).sum() / 1024**2

        logging.info(
            f"Refinement completed: {initial_rows:,} → {len(self.df):,} rows"
        )
        logging.info(
            f"Memory usage reduced from {before_mem:.2f}MB to {after_mem:.2f}MB"
        )

    # -----------------------------
    # 3. Export Layer
    # -----------------------------
    def export_data(self, output_path: str) -> None:
        """Export refined dataset for BI / analytics consumption."""
        if self.df is None or self.df.empty:
            logging.warning("No data to export")
            return

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path, index=False)
        logging.info(f"Refined dataset exported to: {output_path}")


# =============================
# Execution Entry Point
# =============================
if __name__ == '__main__':
    # -----------------------------
    # Robust path resolution
    # -----------------------------
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))

    INPUT_PATH = os.path.join(PROJECT_ROOT, 'data', 'customer.xlsx')
    OUTPUT_PATH = os.path.join(
        PROJECT_ROOT, 'data', 'refined_online_retail.csv')

    refinery = DataRefinery(INPUT_PATH)
    refinery.load_source_data()
    refinery.apply_business_logic()
    refinery.export_data(OUTPUT_PATH)
