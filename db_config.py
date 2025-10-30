# db_config.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# --- Connect to existing MySQL database ---
DATABASE_URL = "mysql+pymysql://root:root1337434@localhost/DiaryProgram"

# --- Create Engine and MetaData ---
engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

# --- Bind MetaData to the engine ---
metadata.reflect(bind=engine)

# --- Session factory ---
db_execute = sessionmaker(bind=engine)()
