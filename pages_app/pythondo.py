import pandas as pd
from sqlalchemy import create_engine

# follows django database settings format, replace with your own settings
DATABASES = {
    'default': {
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': 5432,
    },
}

# choose the database to use
db = DATABASES['default']

# construct an engine connection string
engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user=db['USER'],
    password=db['PASSWORD'],
    host=db['HOST'],
    port=db['PORT'],
    database=db['NAME'],
)
# create sqlalchemy engine
engine = create_engine(engine_string)




def get_df():
    df = pd.read_sql_table('pages_app_bookclass', engine)
    # l = len(df)
    # for i in range(l):
    #     print(i)
    #     print(df.values[i])
    #     print()

    return df
