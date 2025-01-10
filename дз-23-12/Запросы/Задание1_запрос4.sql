use bikestore;

SELECT categories.category_name, COUNT(products.product_id) as count
FROM products
JOIN categories ON categories.category_id = products.category_id
GROUP BY categories.category_name;
