# UK E-Commerce Analytics Pipeline

## Project Description

This project builds an end-to-end batch data pipeline for retail sales analytics using an e-commerce transaction dataset from a UK-based online retailer.

The goal is to ingest raw transaction data, clean and prepare it for analysis, move it into a cloud data warehouse, transform it into analytics-ready tables, and build a dashboard for business monitoring.

The dashboard focuses on two key business questions:
1. How does revenue change over time?
2. Which countries contribute the most to total sales?

This project simulates a practical retail reporting workflow in which raw transaction records are transformed into structured metrics for financial reporting, sales monitoring, and business decision-making.

## Dataset

The dataset contains transaction-level e-commerce sales records from a UK-based online retailer.

Main fields used in this project:
- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

## Data Cleaning

The raw dataset was cleaned using a Python script before being used in the pipeline.

Cleaning steps:
- converted `InvoiceDate` to datetime format
- removed rows with non-positive `Quantity`
- removed rows with non-positive `UnitPrice`
- removed rows with missing `CustomerID`
- excluded cancelled transactions where `InvoiceNo` starts with `C`
- created a new `revenue` column as `Quantity * UnitPrice`

The cleaned dataset was saved as:

`data/processed/cleaned_retail_data.csv`

## Pipeline Overview

This project follows a batch pipeline design:

raw CSV  
→ Python cleaning script  
→ cleaned CSV  
→ cloud storage  
→ BigQuery  
→ dbt transformations  
→ dashboard

## Dashboard

The dashboard will contain at least two visualizations:
- Monthly Revenue Trend
- Top Countries by Revenue

## Tech Stack

- Python
- Pandas
- Google Cloud Storage
- BigQuery
- dbt
- Terraform
- Streamlit or Looker Studio