import pandas as pd
import numpy as np
import logging
import os

# Professional Logging Configuration for Production Environments
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class DataRefinery:
    """
    Automated ETL Pipeline for Retail Transactional Data.
    Designed to ensure data integrity, financial accuracy, and memory scalability.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_source_data(self):
        """
        Ingests source data with support for both Excel and CSV formats.
        Includes automatic delimiter detection for text-based files.
        """
        try:
            if not os.path.exists(self.file_path):
                logging.error(f"File not found: {self.file_path}")
                return

            file_extension = os.path.splitext(self.file_path)[1].lower()

            if file_extension == '.xlsx':
                logging.info(
                    "Excel format detected. Processing with openpyxl engine...")
                self.df = pd.read_excel(self.file_path)
            else:
                logging.info(
                    "CSV/Text format detected. Auto-detecting delimiter...")
                self.df = pd.read_csv(
                    self.file_path,
                    encoding='ISO-8859-1',
                    sep=None,
                    engine='python',
                    on_bad_lines='warn'
                )

            if self.df is not None:
                logging.info(
                    f"Ingestion successful: {self.df.shape[0]} initial records loaded.")
        except Exception as e:
            logging.error(f"Ingestion failed: {e}")

    def apply_business_logic(self):
        """
        Applies standard retail business rules for data sanitization.
        """
        if self.df is None or self.df.empty:
            logging.warning("No data found to process.")
            return

        # 1. Identity Validation: Ensure CustomerID exists for CRM/LTV attribution
        initial_count = len(self.df)
        self.df = self.df.dropna(subset=['CustomerID'])

        # 2. Revenue Normalization: Categorizing Cancellations/Refunds
        if 'InvoiceNo' in self.df.columns:
            self.df['Is_Cancelled'] = self.df['InvoiceNo'].astype(
                str).str.startswith('C')

        # 3. Transactional Integrity: Filtering non-commercial records (Price/Quantity > 0)
        if 'Quantity' in self.df.columns and 'UnitPrice' in self.df.columns:
            self.df = self.df[(self.df['Quantity'] > 0) &
                              (self.df['UnitPrice'] > 0)]

        # 4. Memory Optimization: Downcasting numerical types for high-performance processing
        if 'UnitPrice' in self.df.columns:
            self.df['UnitPrice'] = pd.to_numeric(
                self.df['UnitPrice'], downcast='float')
        if 'Quantity' in self.df.columns:
            self.df['Quantity'] = pd.to_numeric(
                self.df['Quantity'], downcast='integer')
        if 'InvoiceDate' in self.df.columns:
            self.df['InvoiceDate'] = pd.to_datetime(self.df['InvoiceDate'])

        logging.info(
            f"Sanitization complete: Records refined from {initial_count} to {len(self.df)}.")

    def export_refined_data(self, output_path):
        """
        Exports the validated dataset for BI tool integration (PowerBI/Tableau).
        """
        if self.df is not None:
            self.df.to_csv(output_path, index=False)
            logging.info(f"Success: Refined dataset exported to {output_path}")


if __name__ == "__main__":
    # Path configuration for organized directory structure
    INPUT_FILE = "../data/customer.xlsx"
    OUTPUT_FILE = "../data/refined_online_retail.csv"

    refinery = DataRefinery(INPUT_FILE)
    refinery.load_source_data()
    refinery.apply_business_logic()
    refinery.export_refined_data(OUTPUT_FILE)
