import pandas as pd

# Cargar los archivos CSV en DataFrames de Pandas
customers_df = pd.read_csv('ecommerce_customers_dataset.csv')
orders_df = pd.read_csv('ecommerce_orders_dataset.csv')
order_items_df = pd.read_csv('ecommerce_order_items_dataset.csv')
products_df = pd.read_csv('ecommerce_products_dataset.csv')
payments_df = pd.read_csv('ecommerce_order_payments_dataset.csv')

# Establecer la columna índices de las tablas como la clave primaria en el DataFrame
customers_df.set_index('customer_id', inplace=True)
orders_df.set_index('order_id', inplace=True)
order_items_df.set_index('order_item_id', inplace=True)
products_df.set_index('product_id', inplace=True)
payments_df.set_index('payment_id', inplace=True)

   