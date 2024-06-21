import pandas as pd
import sqlite3

# Cargar los archivos CSV
customers_df = pd.read_csv('ecommerce_customers_dataset.csv')
orders_df = pd.read_csv('ecommerce_orders_dataset.csv')
order_items_df = pd.read_csv('ecommerce_order_items_dataset.csv')
products_df = pd.read_csv('ecommerce_products_dataset.csv')
payments_df = pd.read_csv('ecommerce_order_payments_dataset.csv')

# Establecer la columna 'order_id' como índice en el DataFrame payments_df
payments_df.set_index('order_id', inplace=True)

# Imprimir las primeras filas del DataFrame payments_df para confirmar el cambio
print(payments_df.head())

# Análisis de datos

# 1. Obtener el número total de clientes únicos
num_customers = customers_df.index.nunique()
print(f"Total de clientes únicos: {num_customers}")

# 2. Calcular el promedio de valor de pago por pedido
avg_payment_per_order = payments_df['payment_value'].mean()
print(f"Promedio de valor de pago por pedido: {avg_payment_per_order}")

# 3. Determinar la categoría de producto más vendida
order_items_products = order_items_df.merge(products_df, on='product_id')
most_sold_category = order_items_products['product_category_name'].value_counts().idxmax()
print(f"Categoría de producto más vendida: {most_sold_category}")

# 4. Calcular el número total de pedidos realizados
total_orders = orders_df.index.nunique()
print(f"Número total de pedidos realizados: {total_orders}")

# Guardar los resultados en una base de datos SQLite

# Crear una base de datos SQLite
conn = sqlite3.connect('ecommerce.db')

# Guardar los DataFrames en la base de datos
customers_df.to_sql('customers', conn, if_exists='replace', index=True)
orders_df.to_sql('orders', conn, if_exists='replace', index=True)
order_items_df.to_sql('order_items', conn, if_exists='replace', index=True)
products_df.to_sql('products', conn, if_exists='replace', index=True)
payments_df.to_sql('payments', conn, if_exists='replace', index=True)

conn.close()
