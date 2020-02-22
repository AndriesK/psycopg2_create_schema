from create_schema import create_schema

connection_string = "postgresql://postgres:postgres@/myappdb"

tables = {
    'property': {
        'columns': {
            'link': 'citext',
            'price': 'integer',
            'title': 'citext',
            'description': 'citext',
            'suburb': 'citext',
            'pet': 'boolean',
            'bedrooms': 'integer',
            'bathrooms': 'integer',
            'garages': 'integer',
            'score': 'integer'
        },
        'constraints': {
            'link': 'PRIMARY KEY NOT NULL',
            'title': 'NOT NULL',
            'price': 'NOT NULL',
            'suburb': 'NOT NULL'
        }
    },
    'users': {
        'columns': {
            'id': 'serial',
            'username': 'citext',
            'password': 'citext',
            'registered': 'timestamp'
        },
        'constraints': {
            'id': 'PRIMARY KEY NOT NULL',
            'username': 'UNIQUE NOT NULL',
        }
    }
}


def main():
    create_schema(tables, connection_string)


if __name__ == "__main__":
    main()
