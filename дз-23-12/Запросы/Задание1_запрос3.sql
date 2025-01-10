use bikestore;

SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as customer, customers.email, customers.phone
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
JOIN stores ON stores.store_id = orders.store_id
WHERE stores.store_name = 'Rowlett Bikes'