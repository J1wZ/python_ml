use bikestore;

Select  products.product_name , (SUM(order_items.quantity * (order_items.list_price * (1-order_items.discount)))) as total_sales
FROM products
Inner Join order_items on order_items.product_id = products.product_id
Group by products.product_name

