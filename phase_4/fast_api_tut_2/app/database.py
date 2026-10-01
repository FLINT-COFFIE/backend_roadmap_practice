# imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# connection
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"  # used my windows host ip

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# making a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# # reference using raw sql to connect to the database

# # establishing connection to database
# while True:
#     try:
#         conn = psycopg2.connect(
#             host="172.26.80.1",
#             database="fastapi",
#             user="postgres",
#             password="*******",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break

#     except Exception as error:
#         print("Connectin to database failed")
#         print("Error: ", error)
#         time.sleep(2)
