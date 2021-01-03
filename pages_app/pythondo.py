import pandas as pd
from sqlalchemy import create_engine

# follows django database settings format, replace with your own settings
# DATABASES = {
#     'default': {
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '12345678',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     },
# }

DATABASES = {
    'default': {
        'NAME': 'ddnnb11m47ie4m',
        'USER': 'ashraf',
        'PASSWORD': '338e715b16b6097e1c57d18e5f5c582efcc8fa07891b34c9887ef879c1e9b914',
        'HOST': 'postgres://noielsoyjrjlgz:338e715b16b6097e1c57d18e5f5c582efcc8fa07891b34c9887ef879c1e9b914@ec2-100-25-231-126.compute-1.amazonaws.com:5432/ddnnb11m47ie4m',
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
    df_shuffled = df.sample(frac=1).reset_index(drop=True)
    # df['isbn'] = df['isbn'].apply(str)
    return df_shuffled
