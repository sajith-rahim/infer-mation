from infermation.infer import infer
from utils import Logger

import pandas as pd
from prettytable import PrettyTable


def run():
    Logger.set_logger()
    logger = Logger.get_logger()
    logger.info("Starting..")
    df = pd.read_csv("./data/RL1.csv")
    print(df.head(3))

    db_type_map = infer(df)

    table = PrettyTable(["Attribute Name", "Data Type"])
    for attr in db_type_map:
        table.add_row([attr['colname'], attr['type']])

    print(table)

    # gen_ddl(db_type_map)
