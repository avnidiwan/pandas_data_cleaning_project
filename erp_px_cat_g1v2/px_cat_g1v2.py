# =============================================================================================
# Load category dataset, clean each column:
# - 'ID': fill missing, strip spaces, convert to uppercase, replace underscores with hyphens → renamed 'category_id'
# - 'CAT': fill missing, strip spaces, standardize capitalization → renamed 'product_category'
# - 'SUBCAT': fill missing, strip spaces, standardize capitalization → renamed 'product_subcategory'
# - 'MAINTENANCE': fill missing, strip spaces, normalize Yes/No values → renamed 'product_maintenance'
# Final dataset is consistent, analysis-ready, with descriptive column names.
# =============================================================================================




import pandas as pd

category = pd.read_csv('PX_CAT_G1V2.csv')

print(category.head(10))
print(category.shape)




# -------------Column 1-----------------
i = category['ID']


# checking
print(i.isnull().sum())
print(i.duplicated().sum())
print(i.unique())
print(i.dtypes)


# correcting
category['ID'] = category['ID'].fillna('Unknown')
category['ID'] = category['ID'].str.strip()
category['ID'] = category['ID'].str.upper()
category['ID'] = category['ID'].str.replace('_', '-', regex=False)


# rename
category.rename( columns = {'ID' : 'category_id'}, inplace = True)


print(category.head(10))








# ---------------------Column 2-------------------
c = category['CAT']


# checking
print(c.dtypes)
print(c.isnull().sum())
print(c.unique())


# correcting
category['CAT'] = category['CAT'].fillna('Unknown')
category['CAT'] = category['CAT'].str.strip()
category['CAT'] = category['CAT'].str.title()


# rename
category.rename(columns = { 'CAT' : 'product_category'}, inplace = True)


print(category.head(10))








# ---------------------Column 3-------------------
s = category['SUBCAT']


# checking
print(s.dtypes)
print(s.isnull().sum())
print(s.unique())


# correcting
category['SUBCAT'] = category['SUBCAT'].fillna('Unknown')
category['SUBCAT'] = category['SUBCAT'].str.strip()
category['SUBCAT'] = category['SUBCAT'].str.title()


# rename
category.rename(columns = { 'SUBCAT' : 'product_subcategory'}, inplace = True)


print(category.head(10))









# ---------------------Column 4-------------------
m = category['MAINTENANCE']


# checking
print(m.dtypes)
print(m.isnull().sum())
print(m.unique())


# correcting
category['MAINTENANCE'] = category['MAINTENANCE'].fillna('Unknown')
category['MAINTENANCE'] = category['MAINTENANCE'].str.strip()
category['MAINTENANCE'] = category['MAINTENANCE'].str.title()


# rename
category.rename(columns = { 'MAINTENANCE' : 'product_maintenance'}, inplace = True)


print(category.head(10))


# storing cleaned data in new file
category.to_csv(
  'cleaned_category.csv', 
  index=False
)
