use bikestore;

SELECT CONCAT_WS(' ',staffs.first_name, staffs.last_name) as staff, stores.store_name
FROM staffs
JOIN stores ON stores.store_id = staffs.store_id
WHERE staffs.active = 1
order by staff