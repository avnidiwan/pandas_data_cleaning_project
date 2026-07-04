# ==============================================================================
# This script builds the Product Dimension table (dim_products) by merging product master data with category data.
# It creates a derived category_id from product_key, resolves naming conflicts between product and category attributes,
# adds a surrogate key (S.NO.), and prepares a structured
# star schema-ready dimension table for data warehousing.
# ==============================================================================






import pandas as pd


# accessing the cleaned file
prd_info = pd.read_csv('cleaned_prd_info.csv')
category = pd.read_csv('cleaned_category.csv')


# checking columns
print(prd_info.columns)
print(category.columns)


# creating new col to perform join operation 
prd_info['category_id'] = prd_info['product_key'].str[:5]
print(prd_info['category_id'].head(30))


# testing
print(prd_info.head(10))
print(prd_info.columns)
print(category.columns)


# joining prd_info with category
dim_products = pd.merge(
    prd_info,
    category,
    on = 'category_id',
    how ='left'
)


print(dim_products.head(20))
print(dim_products.columns)


# resolving the column naming
dim_products.rename(
    columns={
        'product_category_x': 'product_line',
        'product_category_y': 'product_category'
    },
    inplace=True
)

# keeping only current products
# dim_products = dim_products[
#     dim_products['end_date'].isna()
# ]


# adding new columns for serial number
dim_products['S.NO.'] = range(1, len(dim_products)+1)


# reorder the columns 
dim_products = dim_products[
    [
        'S.NO.',
        'product_id',
        'product_key',
        'product_name',
        'category_id',
        'product_category',
        'product_subcategory',
        'product_maintenance',
        'product_cost',
        'product_line',
        'start_date',
        'end_date'
    ]
]


print(dim_products.head(30))
print(dim_products.columns)


# storing
dim_products.to_csv('gold_dim_products.csv', index = False)
