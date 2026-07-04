#=============================================================================================
# This script builds the Customer Dimension table (dim_customers) by merging cleaned customer, demographic, and location datasets.
# It resolves duplicate gender values, standardizes customer attributes, adds a surrogate key (S.NO.), and prepares a final
# analysis-ready dimension table in a star schema format for data warehousing.
#=============================================================================================





import pandas as pd


# read cleaned csv files
cust_info = pd.read_csv('cleaned_cust_info.csv')
cust = pd.read_csv('cleaned_cust_az.csv')
loc = pd.read_csv('cleaned_loc_a101.csv')


# checking column
print(cust_info.columns)
print(cust.columns)
print(loc.columns)


# joining (left) cust_info with cust 
dim_customers = pd.merge (
    cust_info,
    cust,
    on = 'customer_id',
    how = 'left'
)

print(dim_customers.head(10))
print(dim_customers.columns)


# resolving the gender problem as we thave 2 gender column each from different table
print(dim_customers['gender_x'].unique())
print(dim_customers['gender_y'].unique())

# creating the new gender col and assigning values og gender_x fro cust_info col
dim_customers['gender'] = dim_customers['gender_x']
# finding 'Unknown' values from gender_x
# dataframe.loc[ rows , columns ]
dim_customers.loc[dim_customers['gender'] == 'Unknown', 'gender'] = dim_customers['gender_y']
# droping the gender_x and gender_y cols
dim_customers.drop(
    columns=['gender_x','gender_y'],
    inplace=True
)


# testing
print(dim_customers.head(10))
print(dim_customers.columns)
print(dim_customers['gender'].unique())


# again joining it with loc
dim_customers = pd.merge(
    dim_customers,
    loc,
    on = 'customer_id',
    how = 'left'
)


print(dim_customers.head(10))
print(dim_customers.columns)


# add new column for s.no.
dim_customers['S.NO.'] = range(1, len(dim_customers)+1)


# rearrange the columns sequence
dim_customers = dim_customers[
    [
        'S.NO.',
        'customer_id',
        'customer_key',
        'first_name',
        'last_name',
        'gender',
        'date_of_birth',
        'country_name',
        'marital_status',
        'creation_date'
    ]
]


print(dim_customers.head(10))
print(dim_customers.columns)


# storing this 
dim_customers.to_csv(
    'gold_dim_customers.csv',
    index=False
)
