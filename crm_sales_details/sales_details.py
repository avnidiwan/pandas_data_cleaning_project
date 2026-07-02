# ================= Data Cleaning Summary =================
# Column 1 (Order Number): Removed duplicates, trimmed spaces, converted to uppercase, kept only valid SO-prefixed IDs, renamed to 'sales_ship_number'.
# Column 2 (Product Key): Filled nulls with 'Unknown', trimmed spaces, converted to uppercase, ensured alphanumeric, renamed to 'sales_product_key'.
# Column 3 (Customer ID): Filtered valid numeric range (11000–29483), renamed to 'sales_customer_id'.
# Column 4 (Order Date): Converted YYYYMMDD to datetime, handled invalids with NaT, renamed to 'sales_order_date'.
# Column 5 (Ship Date): Converted YYYYMMDD to datetime, handled invalids with NaT, renamed to 'sales_ship_date'.
# Column 6 (Due Date): Converted YYYYMMDD to datetime, handled invalids with NaT, renamed to 'sales_due_date'.
# Column 7 (Sales): Filled nulls with 0, ensured numeric type, renamed to 'sales'.
# Column 8 (Quantity): Confirmed int64, no nulls, min ≥ 1, renamed to 'quantity'.
# Column 9 (Price): Filled nulls with 0, replaced negatives with NaN, ensured float64, renamed to 'sales_price'.
# =========================================================









import pandas as pd

# fetching the sales_details csv file
sales_details = pd.read_csv('sales_details.csv')

print(sales_details.head())
print(sales_details.shape)
print(sales_details.info())
print(sales_details.describe())







# ================Cleaning and Transforming Data==============
# ----------------Column 1-------------------
ord_no= sales_details['sls_ord_num']


# checking data quality
print(ord_no.dtypes)
print(ord_no.isnull().sum())
print(ord_no.duplicated().sum())
print(ord_no.count())


# correcting
sales_details = sales_details.drop_duplicates(subset=['sls_ord_num'])
sales_details['sls_ord_num'] = sales_details['sls_ord_num'].str.strip()
sales_details['sls_ord_num'] = sales_details['sls_ord_num'].str.upper()
sales_details['sls_ord_num'].str.isalnum().all()
sales_details = sales_details[sales_details['sls_ord_num'].str.startswith('SO')]


# testing
print(sales_details.count())
print(sales_details['sls_ord_num'].duplicated().sum())
print(sales_details.head(20))


# rename
sales_details = sales_details.rename( columns = { 'sls_ord_num' : 'sales_ship_number'})












# -------------------Column 2-------------------------
prd_key = sales_details['sls_prd_key']


# checking data 
print(prd_key.dtypes)
print(prd_key.isnull().sum())
print(prd_key.duplicated().sum())


# correcting
sales_details['sls_prd_key'] = sales_details['sls_prd_key'].fillna('Unknown')
sales_details['sls_prd_key'] = sales_details['sls_prd_key'].str.strip()
sales_details['sls_prd_key'] = sales_details['sls_prd_key'].str.upper()
sales_details['sls_prd_key'].str.isalnum().all()


# rename
sales_details = sales_details.rename( columns = {'sls_prd_key' : 'sales_product_key'})


print(sales_details.head(20))












# ----------------------Column 3------------------
cust_id = sales_details['sls_cust_id']


# checking data quality
print(cust_id.dtypes)
print(cust_id.isnull().sum())
print(cust_id.duplicated().sum())


# correcting
sales_details = sales_details[
    (sales_details['sls_cust_id'] >= 11000) & 
    (sales_details['sls_cust_id'] <= 29483)
]


# rename
sales_details = sales_details.rename( columns = {'sls_cust_id' : 'sales_customer_id'})












# -----------------------Column 4--------------------
order_date = sales_details['sls_order_dt']


# checking
print(order_date.dtypes)
print(order_date.isnull().sum())


# correcting
sales_details['sls_order_dt'] = pd.to_datetime(
    sales_details['sls_order_dt'],
    format='%Y%m%d',
    errors='coerce'
)


# rename
sales_details.rename(columns={'sls_order_dt': 'sales_order_date'}, inplace=True)


# testing
print(sales_details['sales_order_date'].head(20))
print(sales_details['sales_order_date'].dtypes)
print(sales_details['sales_order_date'].min())
print(sales_details['sales_order_date'].max())











# -----------------Column 5-----------------------
ship_date = sales_details['sls_ship_dt']


# checking
print(ship_date.dtypes)
print(ship_date.isnull().sum())


# correcting
sales_details['sls_ship_dt'] = pd.to_datetime(
    sales_details['sls_ship_dt'],
    format='%Y%m%d',
    errors='coerce'
)


sales_details.rename(columns={'sls_ship_dt': 'sales_ship_date'}, inplace=True)


print(sales_details['sales_ship_date'].head(20))
print(sales_details['sales_ship_date'].dtypes)
print(sales_details['sales_ship_date'].min())
print(sales_details['sales_ship_date'].max())















# ------------------------Column 6---------------------
due_date = sales_details['sls_due_dt']


# checking
print(due_date.dtypes)
print(due_date.isnull().sum())


# correcting
sales_details['sls_due_dt'] = pd.to_datetime(
    sales_details['sls_due_dt'],
    format='%Y%m%d',
    errors='coerce'
)


# rename
sales_details.rename(columns={'sls_due_dt': 'sales_due_date'}, inplace=True)


# testing
print(sales_details['sales_due_date'].head(20))
print(sales_details['sales_due_date'].dtypes)
print(sales_details['sales_due_date'].min())
print(sales_details['sales_due_date'].max())


















#  -------------------------Column 7-------------------------
sales = sales_details['sls_sales']


# Checking
print(sales.dtypes)
print(sales.isnull().sum())
print(sales.min())


# correcting
sales_details['sls_sales'] = sales_details['sls_sales'].fillna(0)


# rename
sales_details.rename( columns = {'sls_sales' : 'sales'}, inplace = True)














# ------------------------Column 8---------------------
quantity = sales_details['sls_quantity']


# checking
print(quantity.dtypes)
print(quantity.isnull().sum())
print(quantity.min())


# rename
sales_details.rename( columns = {'sls_quantity' : 'quantity'}, inplace=True)












# -------------------------Column 9------------------------------
price = sales_details['sls_price']


# checkiing
print(price.dtypes)
print(price.isnull().sum())
print(price.min())


#correcting
sales_details['sls_price'] = sales_details['sls_price'].fillna(0)
sales_details.loc[sales_details['sls_price'] < 0, 'sls_price'] = pd.NA


# rename 
sales_details.rename(columns={'sls_price': 'sales_price'}, inplace=True)


# testing 
print(sales_details['sales_price'].head(20))
print(sales_details['sales_price'].dtypes)
print(sales_details['sales_price'].isnull().sum())
print(sales_details['sales_price'].min())
print(sales_details['sales_price'].max())


print(sales_details)


# storing cleaned data in new file
sales_details.to_csv('cleaned_sales.csv', index=False)
