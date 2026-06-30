# ========================================================================
# Import dataset, clean 'CID' by stripping spaces/prefix and converting to int,
# then rename it to 'customer_id'. 
# Clean 'CNTRY' by trimming spaces, fixing capitalization, filling missing values,
# standardizing country names, and rename it to 'country_name'.
# ========================================================================






import pandas as pd

loc = pd.read_csv('LOC_A101.csv')

print(loc.head(10))





#----------------Column 1-------------------
id = loc['CID']


# checking
print(id.shape)
print(id.dtypes)
print(id.isnull().sum())
print(id.duplicated().sum())


# correcting
loc['CID'] = loc['CID'].str.strip()
loc['CID'] = loc['CID'].str.lstrip('AW-000')
loc['CID'] = loc['CID'].astype('int64')


# testing
print(loc['CID'].isnull().sum())
print(loc['CID'].duplicated().sum())
print(loc['CID'].describe())
print(loc['CID'].dtypes)


# rename
loc.rename( columns = {'CID' : 'customer_id'} , inplace = True)


print(loc.head(10))









# ----------------Column 2------------------------
c = loc['CNTRY']


# checking
print(c.shape)
print(c.dtypes)
print(c.isnull().sum())
print(c.unique())


# correcting
loc['CNTRY'] = loc['CNTRY'].str.strip()
loc['CNTRY'] = loc['CNTRY'].str.title()
loc['CNTRY'] = loc['CNTRY'].fillna('Unknown')
print(loc['CNTRY'].unique())

loc['CNTRY'] = loc['CNTRY'].replace({
    'Us' :'USA',
    'Usa' : 'USA',
    'United States' : 'USA',
    'De' : 'Germany',
    '' : 'Unknown'
})


# testing
print(loc['CNTRY'].unique())
print(loc['CNTRY'].isnull().sum())


# rename
loc.rename( columns = {'CNTRY' : 'country_name'} , inplace = True)


print(loc.head(50))
