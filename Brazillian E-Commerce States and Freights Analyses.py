# -*- coding: utf-8 -*-
"""Brazillian E-Commerce: Overall Analysis and View.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KWhZo2CZUrAfdFvry5r3LHl6H-63Vk-e

# Brazillian E-Commerce: Overall Analysis and View

## Importing Packages & Data

### Packages
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""### Packages Configs"""

# Commented out IPython magic to ensure Python compatibility.
# Matplotlib
# %matplotlib inline
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (10,4)
plt.style.use('fivethirtyeight')
plt.rcParams['axes.grid.axis'] = 'y'

"""### Data"""

# Local
#customers = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_customers_dataset.csv')
#geolocation = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_geolocation_dataset.csv')
#order_items = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_order_items_dataset.csv')
#order_payments = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_order_payments_dataset.csv')
#order_reviews = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_order_reviews_dataset.csv')
#orders = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_orders_dataset.csv')
#products = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_products_dataset.csv')
#sellers = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/olist_sellers_dataset.csv')
#product_category_name_translation = pd.read_csv('C:/Users/josem/Desktop/Olist/Data/product_category_name_translation.csv')


# Google Colab
customers = pd.read_csv('olist_customers_dataset.csv')
geolocation = pd.read_csv('olist_geolocation_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
order_payments = pd.read_csv('olist_order_payments_dataset.csv')
order_reviews = pd.read_csv('olist_order_reviews_dataset.csv')
orders = pd.read_csv('olist_orders_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')
sellers = pd.read_csv('olist_sellers_dataset.csv')
product_category_name_translation = pd.read_csv('product_category_name_translation.csv')

"""# States Analysis

## Customer & Sellers Total Numbers

### Customers per State
"""

# Verifying the number of the missing values in column
customers['customer_state'].isnull().sum()

# Sellers per states
customers_per_state = customers['customer_state'].value_counts() 
customers_per_state_values = np.array(customers_per_state.values)
customers_per_state_alpha2 = np.array(customers_per_state.index)

customers_per_state

"""### Sellers Per State"""

# Verifying the number of the missing values in column
sellers['seller_state'].isnull().sum()

# Sellers per states
sellers_per_state = sellers['seller_state'].value_counts() 
sellers_per_state_values = np.array(sellers_per_state.values)
sellers_per_state_alpha2 = np.array(sellers_per_state.index)

sellers_per_state

"""### Chart & Insights

#### Chart
"""

# Figure
fig = plt.figure(figsize = (12, 9))

# First Axes
fig.add_subplot(211)
plt.bar(customers_per_state_alpha2, customers_per_state, color = 'forestgreen')
plt.title('Customers per State', fontweight = 'bold')
plt.xlabel('States')

# Second Axes
fig.add_subplot(212)
plt.bar(sellers_per_state_alpha2, sellers_per_state, color = 'limegreen')
plt.title('Sellers per State', fontweight = 'bold')
plt.xlabel('States')

# Fine adjust in Axes positions
plt.subplots_adjust(hspace=0.35)

# Showing the final result
plt.show()

# Saving chart
fig.savefig('Customers_&_Sellers_States.jpeg', transparent=False, dpi=80, bbox_inches="tight")

"""#### Insights

From this chart we can get at least two thoughts:

1. The SP (stands for S??o Paulo) is, without doubt, the E-Commerce pole of Brazil.

2. The PR (stands for Paran??) seems to have a large proportion of sellers per customer.

In the next steps, we will explore if the thoughts are true and because. Starting at item 2.

## Sellers per Customer

### Data Frame
"""

# Customer & Sellers per State Data Frame
customers_per_state_df = customers['customer_state'].value_counts().to_frame(name = 'Customers')
sellers_per_state_df = sellers['seller_state'].value_counts().to_frame(name = 'Sellers')

customers_sellers_per_state = customers_per_state_df.join(sellers_per_state_df, how='inner')

customers_sellers_per_state

# Concatening Sellers per Customer in Data Frame
customers_sellers_per_state['Sellers per Customer'] = customers_sellers_per_state['Sellers'].values / customers_sellers_per_state['Customers'].values 
customers_sellers_per_state = customers_sellers_per_state.sort_values(by = 'Sellers per Customer', 
                                                                      axis = 0, ascending = False)

customers_sellers_per_state

"""### Chart & Insights

#### Chart
"""

# Figure
fig, ax = plt.subplots()

# Axes
ax.bar(customers_sellers_per_state.index, 'Sellers per Customer',
       data = customers_sellers_per_state, color = "darkred")
ax.set(xlabel='States', ylabel='Sellers per Customer', 
       title='Sellers per Customer by State')
plt.setp(ax.title, fontweight = 'bold')

# Plotting
plt.show()

# Saving the figure
fig.savefig('Sellers_per_Customer_by_State.jpeg', transparent=False, dpi=80, bbox_inches="tight")

"""#### Insights

So, indeed, PR not only has big sellers per customer proportion as this is the biggest in Brazil. Besides S??o Paulo, Santa Catarina (SC) and Rio Grande do Sul (RS) are on top. Why? Well, a possible explanation can be taxes. All three states compound the south region where the taxes on interstadial transactions are lower than anyone located in the country.
But, that yet doesn't explain the S??o Paulo state numbers, so let's dive into this state.

<br/>

*Taxes Infos Source: The National Confederation of Industry (CNI) and Brazilian Micro and Small Business Support Service (SEBRAE), 2013*

## SP State

### Data Frame's
"""

# Customers Data Frame
customers_sp = customers.query('customer_state == "SP"')
customers_sp_cities = customers_sp.customer_city.value_counts().to_frame('Customers')
customers_sp_cities_top20 = customers_sp_cities.nlargest(20, 'Customers')

customers_sp_cities_top20

# Sellers Data Frame
sellers_sp = sellers.query('seller_state == "SP"')
sellers_sp_cities = sellers_sp.seller_city.value_counts().to_frame('Sellers')
sellers_sp_cities_top20 = sellers_sp_cities.nlargest(20, 'Sellers')

sellers_sp_cities_top20

"""### Chart & Insights

#### Chart
"""

# Figure
fig = plt.figure(figsize = (14, 12))

# First Axes
ax1 = fig.add_subplot(211)
ax1.bar(customers_sp_cities_top20.index, 'Customers', 
        data = customers_sp_cities_top20, color = 'royalblue')
ax1.set(title = "SP: Customers per City")
plt.setp(ax1.get_xticklabels(), rotation = 45, 
         horizontalalignment = 'right', fontsize = 12)
plt.setp(ax1.get_yticklabels(), fontsize = 12)
plt.setp(ax1.title, fontweight = 'bold')

# Second Axes
ax2 = fig.add_subplot(212)
ax2.bar(customers_sp_cities_top20.index, 'Customers', 
        data = customers_sp_cities_top20, color = 'royalblue')
ax2.set(title = "SP: Customers per City")
plt.setp(ax2.get_xticklabels(), rotation = 45, 
         horizontalalignment = 'right', fontsize = 12)
plt.setp(ax2.get_yticklabels(), fontsize = 12)
plt.setp(ax2.title, fontweight = 'bold')

# Adjust in Axes
plt.subplots_adjust(hspace=0.5)

# Plotting
plt.show()

# Saving the figure
fig.savefig('SP_Customers_per_City.jpeg', transparent=False, dpi=80, bbox_inches="tight")

"""#### Insights

Now we can see why S??o Paulo state has more customers and sellers than other states, great most of these people are from the S??o Paulo city.

The city of S??o Paulo is the 4th most populated city in the world and not only an E-Commerce pole but the pole of all technology and business of Brazil and even Latin America.

<br/>

*Population Info Source: World Bank Group*

# Freight

## Data Wrangling
"""

# Wrangling Order Items
order_items_wrangled = order_items.set_index('order_id')
order_items_wrangled = order_items_wrangled.drop(columns = ['order_item_id', 
                                                            'product_id', 
                                                            'seller_id', 
                                                            'shipping_limit_date'])

order_items_wrangled.head()

# Wrangling Customers
customers_wrangled = customers.set_index('customer_id')
customers_wrangled = customers_wrangled.drop(columns = ['customer_unique_id', 
                                                        'customer_zip_code_prefix'])

customers_wrangled.head()

# Wrangling Orders
order_columns = list(orders.columns.values)
del order_columns[0]
del order_columns[0]
orders_wrangled = orders.drop(order_columns, axis = 1)

orders_wrangled.head()

# Merging Order Items & Customers
orders_values = orders_wrangled.join(order_items_wrangled, on = 'order_id')
orders_values = orders_values.join(customers_wrangled, on = 'customer_id')

# Dropping key columns and rows with missing values
orders_values.drop(['order_id', 'customer_id'], axis = 1, inplace = True)
orders_values.dropna(inplace = True)

# Renaming columns
orders_values.rename({'price': 'Price', 'freight_value': 'Freight', 
                      'customer_city': 'Customer City', 
                      'customer_state': 'Customer State'}, 
                     axis = 1, inplace = True)

orders_values.head()

"""## Freight and Price

### Chart & Insights

#### Chart
"""

# A function to format labels
def format_as_real(values):
  formated_values = []
  for value in values:
    formated_values.append('R$ %s.00' % value)

  return formated_values 

# Figure
fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharey = False)
plt.subplots_adjust(hspace=0.8)

# Axes 0
sns.histplot(data = orders_values, ax = axs[0], x = 'Price', binwidth = 25)
axs[0].set_title('Prices Distribution', fontweight = 'bold', fontsize = 25)
axs[0].set_xlabel('')
axs[0].set_xlim((0, 700))
axs[0].set_xticks(np.arange(0, 701, 25))
axs[0].set_xticklabels(format_as_real(np.arange(0, 701, 25)), rotation = 75)
axs[0].set_ylabel(ylabel = '', labelpad = 16)
plt.setp(axs[0].get_yticklabels(), verticalalignment = 'baseline')

# Axes 1
sns.histplot(data = orders_values, ax = axs[1], x = 'Freight', binwidth = 5)
axs[1].set_title('Freight Distribution', fontweight = 'bold', fontsize = 25)
axs[1].set_xlabel('')
axs[1].set_xlim((0, 70))
axs[1].set_xticks(np.arange(0, 71, 5))
axs[1].set_xticklabels(format_as_real(np.arange(0, 71, 5)), rotation = 75)
axs[1].set_ylabel(ylabel = '', labelpad = 20)
plt.setp(axs[1].get_yticklabels(), verticalalignment = 'baseline')

# Show
plt.show()

# Saving the figure
fig.savefig('Prices_&_Freight_Distributions.jpeg', transparethent=False, dpi=80, bbox_inches="tight")

"""#### Insights

At first, glance seems the freight and prices walk together, at particular in begin, but look again at to chart and you will see how that isn't true. Observe how in freight graph we have a big concentration in just a bin and then suddenly a large crush, so we can deduce that probably just price doesn't explain freight (more of this soon).

## Freight and Price by State

### Data Preprocessing
"""

# Grouping Values by State
orders_values_total = orders_values.groupby('Customer State').sum()
orders_values_avg = orders_values.groupby('Customer State').mean()

# Merging
  # Renaming Columns
orders_values_total = orders_values_total.rename(columns = {'Price': 'Total Price', 
                                                            'Freight': 'Total Freight'})
orders_values_avg = orders_values_avg.rename(columns = {'Price': 'Average Price', 
                                                           'Freight': 'Average Freight'})
orders_values_avg.head()
orders_values_total.head()
  # Join
orders_values_total_avg = orders_values_total.join(orders_values_avg)

# Pivoting
  # Removing Index
orders_values_total_avg = orders_values_total_avg.reset_index()
orders_values_avg = orders_values_avg.reset_index()

  # Melt
orders_values_total_avg = orders_values_total_avg.melt(id_vars = ['Customer State'], 
                                                       value_vars = ['Total Price', 'Total Freight', 
                                                                     'Average Price', 'Average Freight'], 
                                                       var_name = 'Type', value_name = 'Value')

# Text to columns
orders_values_total_avg[['Measure Type','Measure']] = orders_values_total_avg.Type.str.split(expand=True)

"""### Chart & Insights

#### Chart
"""

# Getting first states by Total Price
orders_values_total_avg = orders_values_total_avg.sort_values(['Measure Type', 
                                                               'Measure', 'Value'], 
                                                              ascending = False)
sorted_labels = orders_values_total_avg.head(27)['Customer State']

# Figure level plotting
fig = sns.FacetGrid(orders_values_total_avg, col = 'Measure', row  = 'Measure Type', 
                    hue = 'Measure', sharex = False, sharey = False, height = 7, aspect = 1.4)
fig.map(sns.barplot, 'Customer State', 'Value', order = sorted_labels)

# Saving the figure
fig.savefig('Prices_&_Freight_Total_and_Average.jpeg', transparethent=False, dpi=80, bbox_inches="tight")

"""#### Insights

Before anything let's understand the chart organization:
* Into columns are plots of price and freight.
* In rows we have total and average measures respective.
* All values are grouped by Customer State and all plots sorted by Total Price.

<br/>

Now, first, observe columns and see the prices and freights total across the states, here seems again that in begin both are related, but afterward this relationship disappears.

Second, on rows total are a likely inverse proportionally to average, in other words, how bigger states prices total are, lesser is your order price average. And on columns the states prices and freights averages are at some level equally sorted, which show how large prices are associated with large expensive freights.

# References

**_Data Source:_** Olist

**_Project Link:_**
"""