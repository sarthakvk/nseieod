from sqlalchemy import engine, text, create_engine


class StockDB:
    def __init__(self):
        # creating engine for sqlalchemy postgresql
        self.DBUri = "postgresql+psycopg2://postgres:@localhost:5432/nseieod"
        self.engine = create_engine(
            self.DBUri,
            executemany_mode="values_plus_batch",
        )

        # coloums in stock tables
        self.cols = [
            "time",
            "price",
            "volume",
        ]

    # function to create database if not exist
    def create_db(self):
        engine = create_engine(self.DBUri.replace("/nseieod", "/postgres"))
        conn = engine.connect()
        conn.connection.connection.set_isolation_level(0)
        conn.execute("create database nseieod")
        conn.close()
        engine.dispose()

    # function to create a table for stock in database
    def create_table(self, stock_code):
        with self.engine.begin() as conn:
            conn.execute(
                text(
                    "CREATE TABLE IF NOT EXISTS ieod_{} ({})".format(
                        stock_code,
                        ", ".join(["{} decimal".format(col) for col in self.cols]),
                    )
                )
            )

    # function to check table exist in database
    def check_table_exist(self, stock_code):
        with self.engine.begin() as conn:
            result = conn.execute(
                text(
                    "Select exists(Select * from information_schema.tables where table_name=:table_name)",
                    table_name="ieod_%s" % stock_code,
                )
            )
            return result.fetchone()[0]

    # function to insert data into table
    def insert(self, stock_code, data):
        with self.engine.begin() as conn:
            conn.execute(
                text(
                    "INSERT INTO ieod_{} ({}) VALUES ({})".format(
                        stock_code,
                        ", ".join([col for col in data.keys()]),
                        ", ".join([str(data[val]) for val in data.keys()]),
                    )
                )
            )
