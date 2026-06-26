# ------------------------------------------------------------
# Summary:
# In this script, I am using Pandas to read the CRM dataset (cust_info.csv) and clean it step by step. 
# Each column is checked for data quality (missing values, duplicates, wrong formats) and then corrected. 
# For IDs, I remove nulls and duplicates, change datatype to integer, and rename the column.
# For text columns like first_name and last_name, I fill missing values, strip spaces, standardize capitalization, and rename
# For categorical columns like marital_status and gender,I replace codes (M, S) with full words (Married, Single) and (M, F) by(Male, Female). 
# For dates, I convert strings into proper datetime objects. 
# The overall approach is to make the dataset clean, consistent, and ready for analysis while practicing Pandas data wrangling skills.
# ------------------------------------------------------------







import pandas as pd

# accessing the crm -> cust_info csv file
cust_info = pd.read_csv('cust_info.csv')

print(cust_info.head())


# ==========cleaning and transforming data========
# ----------column 1-----------

customer_id = cust_info['cst_id']

# checking the data quality of the column
print(customer_id.shape)
print(customer_id.isnull().sum())
print(customer_id.duplicated().sum())


#removing the invalid ids
cust_info = cust_info.dropna(subset=['cst_id'])        
cust_info = cust_info.drop_duplicates(subset=['cst_id'])


# testing
print(cust_info['cst_id'].shape)
print(cust_info['cst_id'].isnull().sum())
print(cust_info['cst_id'].duplicated().sum())


#change datatype to int and rename 
cust_info['cst_id'] = cust_info['cst_id'].astype('int64')
cust_info = cust_info.rename(columns={'cst_id': 'customer_id'}) 

print(cust_info.head())








#------------Column 2----------------
customer_key = cust_info['cst_key']


# checking data quality
print(customer_key.describe())
print(customer_key.isnull().sum())
print(customer_key.duplicated().sum())
print(customer_key.dtypes)


# renaming
cust_info = cust_info.rename(columns={'cst_key': 'customer_key'})


print(cust_info.head())







#----------------Column 3-----------------
name = cust_info['cst_firstname']


# checking data quality
print(name.describe())
print(name.shape)
print(name.info())
print(name.isnull().sum())
print(name.duplicated().sum())
print(name.dtypes)


#removing
cust_info['cst_firstname'] = cust_info['cst_firstname'].fillna('Unknown')
cust_info['cst_firstname'] = cust_info['cst_firstname'].str.strip()
cust_info['cst_firstname'] = cust_info['cst_firstname'].str.title()
cust_info = cust_info[cust_info['cst_firstname'] != ""]


#rename
cust_info= cust_info.rename(columns={'cst_firstname':'first_name'})


#testing
print(cust_info)









#----------------Column 4-----------------
lst_name = cust_info['cst_lastname']


# checking data quality
print(lst_name.describe())
print(lst_name.shape)
print(lst_name.info())
print(lst_name.isnull().sum())
print(lst_name.duplicated().sum())
print(lst_name.dtypes)


#removing
cust_info['cst_lastname'] = cust_info['cst_lastname'].fillna('Unknown')
cust_info['cst_lastname'] = cust_info['cst_lastname'].str.strip()
cust_info['cst_lastname'] = cust_info['cst_lastname'].str.title()
cust_info = cust_info[cust_info['cst_lastname'] != ""]


#rename
cust_info= cust_info.rename(columns={'cst_lastname':'last_name'})


#testing
print(cust_info)








# -----------------Column 5-----------------
marital = cust_info['cst_marital_status']


# checking data quality
print(marital.describe())
print(marital.shape)
print(marital.info())
print(marital.isnull().sum())
print(marital.unique())


# rename
cust_info = cust_info.rename(columns = {'cst_marital_status':'marital_status'})


#correcting the values
cust_info['marital_status'] = cust_info['marital_status'].fillna('Unknown')
cust_info['marital_status'] = cust_info['marital_status'].str.strip()
cust_info['marital_status'] = cust_info['marital_status'].str.title()
cust_info['marital_status'] = cust_info['marital_status'].replace(
    {
        'M':'Married',
        'S':'Single',
        'Nan':'Unknown'
    }
)


# testing
print(marital.isnull().sum())
print(marital.unique())
print(cust_info)







#----------------Column 6-----------------
gender = cust_info['cst_gndr']


# checking data quality
print(gender.describe())
print(gender.shape)
print(gender.info())
print(gender.isnull().sum())
print(gender.unique())


#rename
cust_info = cust_info.rename(columns = {'cst_gndr':'gender'})


# correcting the values
cust_info['gender'] = cust_info['gender'].fillna('Unknown')
cust_info['gender'] = cust_info['gender'].str.strip()
cust_info['gender'] = cust_info['gender'].str.title()
cust_info['gender'] = cust_info['gender'].replace(
    {
        'M':'Male',
        'F':'Female',
        'Nan':'Unknown'
    }
)


# testing
print(cust_info['gender'].isnull().sum())
print(cust_info['gender'].unique())
print(cust_info)






# -----------------Column 7-----------------
creation_date = cust_info['cst_create_date']


# checking data quality
print(creation_date.describe())
print(creation_date.shape)
print(creation_date.info())
print(creation_date.isnull().sum())
print(creation_date.dtypes)


#rename
cust_info = cust_info.rename(columns = {'cst_create_date': 'creation_date'})


# converting to datetime    
cust_info['creation_date'] = pd.to_datetime(cust_info['creation_date'])


# testing 
print(cust_info['creation_date'].isnull().sum())
print(cust_info['creation_date'].dtypes)
print(cust_info)
