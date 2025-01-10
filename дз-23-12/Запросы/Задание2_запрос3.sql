use bikestore;

SELECT month(orders.order_date) AS Month,
         count(orders.order_id) AS Total_Number_of_Orders,
		sum(order_items.quantity * (order_items.list_price * (1 - order_items.discount))) AS Total_Sales
FROM orders
inner join order_items on order_items.order_id = orders.order_id
GROUP BY Month
ORDER BY Month;
