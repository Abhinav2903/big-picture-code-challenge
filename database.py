from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
# from app import db
# Database URL
DB_URL = "mysql+pymysql://root:abhi2903@127.0.0.1:3306/flaskdatabase?charset=utf8mb4"

# Create the SQLAlchemy engine
engine = create_engine(DB_URL)

# Create a Session class for interacting with the database
Session = sessionmaker(bind=engine)
create_table_sql = """
CREATE TABLE IF NOT EXISTS books (
    isbn VARCHAR(255) PRIMARY KEY,
    author VARCHAR(255),
    title VARCHAR(255),
    cover VARCHAR(255),
    summary TEXT
);
"""

add_sample_bok ="""INSERT INTO books (isbn, author, title, cover, summary)
VALUES ('1234567890', 'John Doe', 'Sample Book', 'cover_url', 'This is a sample book summary.');
"""
with engine.connect() as conn:
    conn.execute(text(create_table_sql))
    conn.execute(text(add_sample_bok))

    # Execute the SELECT query and fetch the results
    result = conn.execute(text("SELECT * FROM books"))
    rows = result.fetchall()

    # Print the retrieved rows
    for row in rows:
        print(row)






