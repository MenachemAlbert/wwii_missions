# wwii_missions

A Python project for analyzing World War II missions data.

## Installation

Use the package manager [pip] to install the required dependencies:

```bash
pip install dictalchemy3 flask toolz returns psycopg2-binary sqlalchemy
```

## Usage

To run the application:


   1.Set up your database and configure the connection in config.py.

   2.Run the Flask application:

```python
app = Flask(__name__)
app.register_blueprint(target_blueprint, url_prefix="/api/mission")

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.