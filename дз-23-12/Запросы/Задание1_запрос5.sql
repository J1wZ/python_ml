use bikestore;

SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as customer, COUNT(orders.order_id) as count
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
GROUP BY customer;
