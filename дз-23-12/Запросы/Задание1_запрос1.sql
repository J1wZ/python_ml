use bikestore;

SELECT products.product_name, brands.brand_name
FROM products
JOIN brands ON brands.brand_id = products.brand_id