use bikestore;

SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as Customer,
         sum(order_items.quantity * (order_items.list_price * (1 - order_items.discount))) AS Total_Money_Spent
FROM customers
inner join orders on orders.customer_id = customers.customer_id
inner join order_items on order_items.order_id = orders.order_id
GROUP BY Customer
order by Total_Money_Spent
DESC LIMIT 5;
