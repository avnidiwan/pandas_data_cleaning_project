# ==========================================================================
# Data Cleaning 
# - Column 1: trimmed prefixes, removed duplicates
# - Column 2: converted to datetime, replaced unrealistic values with NaT
# - Column 3: standardized labels, filled missing with 'Unknown'
# Result: Clean, consistent, analysis-ready customer dataset
# ============================================================================





import pandas as pd

cust = pd.read_csv('cust_az12.csv')

print(cust.head(10))


# ----------------Column 1----------------
cid = (cust['CID'])


# checking
print(cid.shape)
print(cid.dtypes)
print(cid.isnull().sum())
print(cid.duplicated().sum())


# correcting
cust['CID'] = cust['CID'].str.strip()
cust['CID'] = cust['CID'].str.lstrip('NASAW000')
cust.drop_duplicates(subset='CID', inplace=True)


# rename
cust.rename( columns = {'CID' : 'customer_id'} , inplace = True)


# testing
print(cust['customer_id'].isnull().sum())
print(cust['customer_id'].duplicated().sum())
print(cust.head(10))
print(cust.describe())








#----------------Column 2------------------
dob = cust['BDATE']


# checking
print(dob.dtypes)
print(dob.isnull().sum())


# correcting
cust['BDATE'] = pd.to_datetime(cust['BDATE'], errors ='coerce')
cust.loc[(cust['BDATE'] < '1900-01-01') | (cust['BDATE'] > pd.to_datetime("today")), 'BDATE'] = pd.NaT


# testing
print(cust['BDATE'].dtypes)
print(cust.head(20))
print(cust['BDATE'].min())
print(cust['BDATE'].max())


# rename
cust.rename( columns = {'BDATE' : 'date_of_birth'} , inplace = True)


print(cust.head(20))









# ------------------Column 3------------------
g = cust['GEN']


# checking
print(g.isnull().sum())
print(g.dtypes)
print(g.unique())


# correcting
cust['GEN'] = cust['GEN'].str.strip()
cust['GEN'] = cust['GEN'].str.title()
cust['GEN'] = cust['GEN'].fillna('Unknown')
print(cust['GEN'].unique())

cust['GEN'] = cust['GEN'].replace(
    {
        'M' : 'Male',
        'F' : 'Female',
        '' : 'Unknown',
        'nan' : 'Unknown'
    }
)


# testing
print(cust['GEN'].unique())


# rename
cust.rename( columns = {'GEN' : 'gender'} , inplace = True)


print(cust.head(50))
print(cust.describe())
