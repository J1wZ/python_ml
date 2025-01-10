use bikestore;

Select orders.order_status, count(orders.order_id) as order_count
from orders
group by orders.order_status
order by orders.order_status;
