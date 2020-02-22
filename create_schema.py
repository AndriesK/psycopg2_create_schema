import psycopg2
import sys


def create_schema(tables, connection_string):
    conn = psycopg2.connect(connection_string)

    cur = conn.cursor()

    for table_name in tables:

        cur.execute(f"CREATE TABLE {table_name} ()")

        for columnKey, columnValue in tables[table_name]['columns'].items():
            if columnKey in tables[table_name]['constraints']:
                cur.execute(
                    f'alter table {table_name} add column {columnKey} {columnValue} {tables[table_name]["constraints"][columnKey]}')
            else:
                cur.execute(
                    f'alter table {table_name} add column {columnKey} {columnValue}')
        conn.commit()

    conn.close()
    cur.close()
