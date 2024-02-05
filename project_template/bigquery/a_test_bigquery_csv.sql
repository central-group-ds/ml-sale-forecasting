SELECT
  FORMAT_DATE('%Y%m%d', sale_date) AS sale_date,
  brand_group,
  net_sales_quantity,
  gross_sales_exc_vat,
  net_sales_amt_exc_vat
FROM `cdgshared.DL_OBI_CORE.VW_INCREMENTAL_HISTORICAL_DATA_COMBINE`
WHERE
  sale_date BETWEEN '{DATE_RANGE[0]}' AND '{DATE_RANGE[1]}'
  {WHERE_DEPARTMENT}
LIMIT 100
