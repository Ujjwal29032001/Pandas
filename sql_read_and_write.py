import pandas as pd
from sqlalchemy import create_engine
connection_string = 'mysql+pymysql://root:@localhost/hr_db'
engine = create_engine(connection_string)

query = "Select * from department"
df = pd.read_sql(query,engine)
print(df)

