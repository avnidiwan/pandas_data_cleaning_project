# Data Cleaning Pipeline:
# - Loaded product info CSV and inspected each column.
# - Column 1 (prd_id): checked for nulls/duplicates, renamed to product_id.
# - Column 2 (prd_key): stripped spaces, standardized to uppercase, renamed to product_key.
# - Column 3 (prd_nm): trimmed/uppercased names, renamed to product_name.
# - Column 4 (prd_cost): rounded to 2 decimals, removed negative values, renamed to product_cost.
# - Column 5 (prd_line): cleaned spaces/case, filled nulls with 'Unknown', mapped codes (S/M/R/T) to labels, renamed to product_category.
# - Column 6 (prd_start_dt): converted to datetime, renamed to start_date.
# - Column 7 (prd_end_dt): converted to datetime, renamed to end_date.
# Overall: ensured consistent formatting, handled missing/invalid values, and standardized column names for analysis.











import pandas as pd

prd_info = pd.read_csv('prd_info.csv')
print(prd_info.head())


# ===========cleaning and tranforming the data=========
# -----------Colummn 1------------------
prd_id = prd_info['prd_id']


# checking data quality
print(prd_id.shape)
print(prd_id.info())
print(prd_id.describe())
print(prd_id.isnull().sum())
print(prd_id.duplicated().sum())

# => NO NULL AND DUPLICATES


# rename
prd_info = prd_info.rename( columns = {'prd_id' : 'product_id'})









# --------------Column 2------------------
prd_key = prd_info['prd_key']


# checking data quality
print(prd_key.shape)
print(prd_key.info())
print(prd_key.describe())
print(prd_key.isnull().sum())
print(prd_key.duplicated().sum())
print(prd_key.unique())
print(prd_key.dtypes)


# correcting
prd_info['prd_key'] = prd_info['prd_key'].str.strip()
prd_info['prd_key'] = prd_info['prd_key'].str.upper()


# rename
prd_info = prd_info.rename( columns = {'prd_key' : 'product_key'})


# testing
print(prd_info.head())












# ---------------Column 3------------------
name = prd_info['prd_nm']


# checking data quality
print(name.shape)
print(name.dtypes)
print(name.info())
print(name.isnull().sum())
print(name.duplicated().sum())
print(name.unique())


# correcting
prd_info['prd_nm'] = prd_info['prd_nm'].str.strip()
prd_info['prd_nm'] = prd_info['prd_nm'].str.upper()


# rename
prd_info = prd_info.rename( columns = {'prd_nm' : 'product_name'})


# testing
print(prd_info['product_name'].head())















#-----------------Column 4------------------
prd_cost = prd_info['prd_cost']


# checking data quality
print(prd_cost.shape)
print(prd_cost.dtypes)
print(prd_cost.info())
print(prd_cost.describe())
print(prd_cost.isnull().sum())
print(prd_cost.duplicated().sum())


# correcting
prd_info['prd_cost'] = prd_info['prd_cost'].round(2)   
prd_info = prd_info[prd_info['prd_cost'] >= 0]


# rename
prd_info = prd_info.rename( columns = {'prd_cost' : 'product_cost'})


# testing
print(prd_info['product_cost'].head(50))













# ----------------Column 5------------------
prd_line = prd_info['prd_line']


# checking data quality
print(prd_line.shape)
print(prd_line.dtypes)
print(prd_line.info())
print(prd_line.describe())
print(prd_line.isnull().sum())
print(prd_line.unique())


# correcting
prd_info['prd_line'] = prd_info['prd_line'].str.strip()
prd_info['prd_line'] = prd_info['prd_line'].str.upper()
prd_info['prd_line'] = prd_info['prd_line'].fillna('Unknown')
prd_info['prd_line'] = prd_info['prd_line'].replace({
    'S' : 'Sports',
    'M' : 'Mountain',
    'R' : 'Roadways',
    'T' : 'Touring'
})


# testing
print(prd_info['prd_line'] .isnull().sum())
print(prd_info['prd_line'] .unique())


# rename
prd_info = prd_info.rename( columns = {'prd_line' : 'product_category'})


print(prd_info)












# -------------------Column 6-----------------
start_date = prd_info['prd_start_dt']


print(start_date.shape)
print(start_date.dtypes)
print(start_date.info())
print(start_date.min())
print(start_date.max())
print(start_date.isnull().sum())


# converting datatype
prd_info['prd_start_dt'] = pd.to_datetime(prd_info['prd_start_dt'], errors='coerce')


# rename
prd_info = prd_info.rename( columns = { 'prd_start_dt' : 'start_date'})












# -------------------Column 7-----------------
end_date = prd_info['prd_end_dt']


print(end_date.shape)
print(end_date.dtypes)
print(end_date.info())
print(end_date.min())
print(end_date.max())
print(end_date.isnull().sum())


# converting datatype
prd_info['prd_end_dt'] = pd.to_datetime(prd_info['prd_end_dt'], errors='coerce')


# rename
prd_info = prd_info.rename( columns = { 'prd_end_dt' : 'end_date'})





print(prd_info)
