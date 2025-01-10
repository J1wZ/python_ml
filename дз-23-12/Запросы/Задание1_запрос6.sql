use bikestore;

SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as customer, COUNT(orders.order_id) as order_count
FROM customers
INNER JOIN orders ON orders.customer_id = customers.customer_id
GROUP BY customer;
