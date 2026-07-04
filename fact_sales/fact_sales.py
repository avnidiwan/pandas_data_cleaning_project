# =============================================================

# Build final fact_sales table by joining sales with customer and product dimensions, 
# renaming surrogate keys, selecting required columns, and saving as gold_fact_sales.csv

# ==============================================================





import pandas as pd


# accessing the files
sales = pd.read_csv('cleaned_sales.csv')
dim_cust = pd.read_csv('gold_dim_customers.csv')
dim_prd = pd.read_csv('gold_dim_products.csv')


# join only customer dimension
fact_sales = pd.merge(
    sales,
    dim_cust,
    left_on='sales_customer_id',
    right_on='customer_id',
    how='left'
)

# rename surrogate key
fact_sales.rename(
    columns={'S.NO.': 'customer_S.NO.'},
    inplace=True
)


print(fact_sales.columns)


# new column common on both sales and dim_prd table
dim_prd['sales_product_key'] = dim_prd['product_key'].str[6:]
print(dim_prd['sales_product_key'].unique())


# joining
fact_sales = pd.merge(
    fact_sales,
    dim_prd,
    on = 'sales_product_key',
    how = 'left'
)


# renaming
fact_sales.rename(
    columns={'S.NO.': 'product_S.NO.'},
    inplace=True
)

# keep only required fact columns
fact_sales = fact_sales[
    [
        'sales_ship_number',
        'customer_S.NO.',
        'product_S.NO.',
        'sales_order_date',
        'sales_ship_date',
        'sales_due_date',
        'sales',
        'quantity',
        'sales_price'
    ]
]


print(fact_sales.columns)
print(fact_sales.head(20))


# save final fact table
fact_sales.to_csv('gold_fact_sales.csv', index=False)
