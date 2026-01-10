import pandas as pd
import numpy as np
import logging
import os

# Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class DataRefinery:
    """
    Enterprise-grade ETL Pipeline for Retail Data.
    Focuses on financial integrity, memory optimization, and scalability.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_source_data(self):
        """Robust data ingestion handling both Excel and CSV formats."""
        try:
            if not os.path.exists(self.file_path):
                logging.error(f"File not found: {self.file_path}")
                return

            file_ext = os.path.splitext(self.file_path)[1].lower()

            if file_ext == '.xlsx':
                logging.info("Excel detected. Parsing with openpyxl...")
                self.df = pd.read_excel(self.file_path)
            else:
                logging.info("CSV detected. Auto-detecting delimiter...")
                self.df = pd.read_csv(
                    self.file_path, encoding='ISO-8859-1', sep=None, engine='python', on_bad_lines='warn')

            logging.info(f"Ingested {len(self.df)} initial records.")
        except Exception as e:
            logging.error(f"Ingestion Failed: {e}")

    def apply_business_logic(self):
        """Sanitization engine applying high-stakes retail business rules."""
        if self.df is None or self.df.empty:
            return

        initial_count = len(self.df)

        # 1. Identity Integrity: Drop missing CustomerIDs for accurate loyalty KPIs
        self.df = self.df.dropna(subset=['CustomerID'])

        # 2. Financial Logic: Isolate cancellations (Invoice starts with 'C')
        if 'InvoiceNo' in self.df.columns:
            self.df['Is_Cancelled'] = self.df['InvoiceNo'].astype(
                str).str.startswith('C')

        # 3. Value Validation: Remove zero/negative quantities and prices
        if 'Quantity' in self.df.columns and 'UnitPrice' in self.df.columns:
            self.df = self.df[(self.df['Quantity'] > 0) &
                              (self.df['UnitPrice'] > 0)]

        # 4. Memory Optimization: Numerical Downcasting
        if 'UnitPrice' in self.df.columns:
            self.df['UnitPrice'] = pd.to_numeric(
                self.df['UnitPrice'], downcast='float')
        if 'Quantity' in self.df.columns:
            self.df['Quantity'] = pd.to_numeric(
                self.df['Quantity'], downcast='integer')

        logging.info(
            f"Refinement complete. Records optimized from {initial_count} to {len(self.df)}.")

    def export_data(self, output_path):
        """Exports sanitized data for BI tool integration."""
        if self.df is not None:
            self.df.to_csv(output_path, index=False)
            logging.info(f"Refined dataset saved to: {output_path}")


if __name__ == "__main__":
    # Path configuration for professional directory structure
    INPUT = "../data/customer.xlsx"
    OUTPUT = "../data/refined_online_retail.csv"

    refinery = DataRefinery(INPUT)
    refinery.load_source_data()
    refinery.apply_business_logic()
    refinery.export_data(OUTPUT)
