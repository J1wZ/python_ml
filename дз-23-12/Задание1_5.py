from sqlalchemy import create_engine, text
 
user = 'root'
password = 'NoMorFort19#'
host = '127.0.0.1'
port = 3306
database = 'bikestore'

def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    )


if __name__ == '__main__':
    try:
        engine = get_connection()
        print(f"Успешно подключено.")
        with engine.connect() as connection:
            query="""
            SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as customer, COUNT(orders.order_id) as count
            FROM customers
            JOIN orders ON orders.customer_id = customers.customer_id
            GROUP BY customers.customer_id;"""
            my_data=list(connection.execute(text(query)))

        for el in my_data:
            print(el)
    except Exception as ex:
        print("Не получилось подключиться: \n", ex)