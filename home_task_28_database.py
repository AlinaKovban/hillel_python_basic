import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    # db_path = os.path.join(os.getcwd(), 'chinook.db')
    db_path = os.path.join(os.path.dirname(__file__), 'chinook.db')
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)




def get_orders_amount() -> int:
    '''
    сумма заказов по таблице invoice_items
    '''
    query_sql = f'''
        SELECT sum(UnitPrice*Quantity)
          FROM invoice_items;
    '''
    orders = execute_query(query_sql)
    return orders

print(get_orders_amount())



def repeated_names() -> None:
    '''
    повторяющееся имена FirstName из таблицы customers
    '''
    query_sql = f'''
        SELECT FirstName, COUNT(FirstName)
          FROM customers
          GROUP BY FirstName
          HAVING COUNT(FirstName) > 1
    '''
    result = execute_query(query_sql)
    return result

print(repeated_names())



