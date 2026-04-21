CREATE OR REPLACE TABLE `uk-ecommerce-analytics-493919.uk_ecommerce.sales_by_country` AS
SELECT
  Country,
  COUNT(*) AS total_orders,
  SUM(Quantity) AS total_quantity,
  ROUND(SUM(revenue), 2) AS total_revenue
FROM `uk-ecommerce-analytics-493919.uk_ecommerce.cleaned_retail_data`
GROUP BY Country
ORDER BY total_revenue DESC;
