SELECT
  TO_CHAR(trans_date, 'yyyy-mm-dd') AS trans_date,
  member_number,
  qty AS quantity,
  net_price_tot / 1.07 AS net_sales_amt_exc_vat
FROM analysis_cds_rbs.sales_sku_cds_rbs
WHERE
  DATE(trans_date) BETWEEN '{DATE_RANGE[0]}' AND '{DATE_RANGE[1]}'
LIMIT 100
