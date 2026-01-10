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
    Enterprise-grade ETL Pipeline.
    Handles data ingestion, sanitization, and memory optimization 
    for large-scale retail datasets.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_source_data(self):
        """
        Robust data ingestion engine. 
        Supports both Excel (.xlsx) and CSV with automatic delimiter detection.
        """
        try:
            if not os.path.exists(self.file_path):
                logging.error(f"File not found: {self.file_path}")
                return

            # Determine file type
            file_extension = os.path.splitext(self.file_path)[1].lower()

            if file_extension == '.xlsx':
                logging.info("Excel format detected. Parsing with openpyxl...")
                self.df = pd.read_excel(self.file_path)
            else:
                logging.info(
                    "Text-based format detected. Attempting auto-detection of delimiter...")
                # sep=None with engine='python' lets pandas guess if it's comma, semicolon, or tab
                self.df = pd.read_csv(
                    self.file_path,
                    encoding='ISO-8859-1',
                    sep=None,
                    engine='python',
                    on_bad_lines='warn'  # Skip problematic lines but warn the user
                )

            if self.df is not None:
                logging.info(
                    f"Successfully ingested {self.df.shape[0]} records.")
        except Exception as e:
            logging.error(f"Ingestion Failed: {e}")

    def apply_business_logic(self):
        """
        Main sanitization engine applying retail business rules.
        """
        if self.df is None or self.df.empty:
            logging.warning("No data available to clean.")
            return

        # 1. Integrity: Ensure CustomerID exists for attribution
        initial_count = len(self.df)
        self.df = self.df.dropna(subset=['CustomerID'])

        # 2. Accounting: Identify Cancellations
        # Standard retail format: Invoice numbers starting with 'C' are returns
        if 'InvoiceNo' in self.df.columns:
            self.df['Is_Cancelled'] = self.df['InvoiceNo'].astype(
                str).str.startswith('C')

        # 3. Quality: Remove non-commercial records (Price/Quantity <= 0)
        if 'Quantity' in self.df.columns and 'UnitPrice' in self.df.columns:
            self.df = self.df[(self.df['Quantity'] > 0) &
                              (self.df['UnitPrice'] > 0)]

        # 4. Performance: Memory Optimization (Type Casting)
        # Reduces RAM footprint significantly for large datasets
        if 'UnitPrice' in self.df.columns:
            self.df['UnitPrice'] = pd.to_numeric(
                self.df['UnitPrice'], downcast='float')
        if 'Quantity' in self.df.columns:
            self.df['Quantity'] = pd.to_numeric(
                self.df['Quantity'], downcast='integer')
        if 'InvoiceDate' in self.df.columns:
            self.df['InvoiceDate'] = pd.to_datetime(self.df['InvoiceDate'])

        logging.info(
            f"Sanitization complete. Records refined from {initial_count} to {len(self.df)}.")

    def export_data(self, output_path):
        """Exports the cleaned dataset to a standard CSV for BI tools."""
        if self.df is not None:
            self.df.to_csv(output_path, index=False)
            logging.info(f"Refined dataset exported to: {output_path}")


if __name__ == "__main__":
    # Settings
    INPUT = "customer.xlsx"
    OUTPUT = "refined_online_retail.csv"

    refinery = DataRefinery(INPUT)
    refinery.load_source_data()
    refinery.apply_business_logic()
    refinery.export_data(OUTPUT)
