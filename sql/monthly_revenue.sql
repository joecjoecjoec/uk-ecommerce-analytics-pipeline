CREATE OR REPLACE TABLE `uk-ecommerce-analytics-493919.uk_ecommerce.monthly_revenue` AS
SELECT
  FORMAT_DATE('%Y-%m', DATE(InvoiceDate)) AS invoice_month,
  Country,
  ROUND(SUM(revenue), 2) AS monthly_revenue
FROM `uk-ecommerce-analytics-493919.uk_ecommerce.cleaned_retail_data`
GROUP BY invoice_month, Country
ORDER BY invoice_month, monthly_revenue DESC;
