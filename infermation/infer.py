import pandas as pd

import dateutil
from collections import Counter

from infermation.dtypes import dtypes, teradata_dtypes_map
from infermation.type_utils import cleanse, is_nan_numeric
from utils import Logger

from prettytable import PrettyTable


def infer_by_casting(val_in_string):
    r"""
    Infer data type by casting into types

    :param val_in_string: col. value in string type
    :return: inferred data type by casting {int, float, str, None}
    """
    if val_in_string is None or val_in_string == '':
        return None

    if val_in_string.isnumeric():

        try:
            return int(val_in_string)
        except Exception:
            return None

    try:
        if isinstance(val_in_string, (int, float)):
            return float(val_in_string)

        if isinstance(val_in_string, float):
            return val_in_string

        return None if cleanse(val_in_string) is None else float(val_in_string)
    except Exception:
        return val_in_string


def check_numeric_type(element) -> str:
    r"""

    :param element:
    :return: type
    """
    # try casting
    numeric_type = infer_by_casting(str(element))

    try:
        if numeric_type == int(numeric_type):
            numeric_type = int(numeric_type)
    except Exception:
        pass

    if isinstance(numeric_type, float):
        return dtypes.float
    elif isinstance(numeric_type, int):
        return dtypes.integer
    else:
        try:
            if is_nan_numeric(element):
                return dtypes.integer
            else:
                return None
        except Exception:
            return None


def check_date_type(element: object) -> str:
    try:
        dt = dateutil.parser.parse(str(element))

        if dt.hour == 0 and dt.minute == 0 and dt.second == 0 and len(str(element)) <= 16:
            return dtypes.date
        else:
            return dtypes.datetime

    except ValueError:
        return None


def count_dtypes_in_column(data):
    dtype_counts = Counter()

    type_checkers_functions = [check_numeric_type,
                               check_date_type]

    for element in data:
        for type_checker_fn in type_checkers_functions:
            try:
                dtype_guess = type_checker_fn(element)
            except Exception:
                dtype_guess = None
            if dtype_guess is not None:
                dtype_counts[dtype_guess] += 1
                break
        else:
            dtype_counts[dtypes.invalid] += 1

    return dtype_counts


def infer_column_type(sample, df, col_name):
    Logger.get_logger().info(f"Processing column: {col_name}")

    is_categorical = False
    n_distinct = len(set([str(x) for x in df]))
    sample = sample.dropna(axis=0)

    dtype_counts = count_dtypes_in_column(sample)

    known_dtype_dist = {k: v for k, v in dtype_counts.items()}
    majority_dtype = max(known_dtype_dist.items(), key=lambda kv: kv[1])

    if majority_dtype not in (dtypes.date, dtypes.datetime):
        if majority_dtype in (dtypes.integer, dtypes.float):
            is_categorical = n_distinct < 10
        else:
            is_categorical = n_distinct < min(max((sample.shape[0] / 100), 10), 3000)

    return dtype_counts, majority_dtype, is_categorical


def to_db_type(dtype):
    return teradata_dtypes_map.get(dtype)



def infer(df):
    n_rows, n_cols = df.shape

    if n_rows == 0 or n_cols == 0:
        raise RuntimeError("!")

    # TODO: Compute sample size statistically.
    sample = df.sample(frac=0.3, replace=True, random_state=1) if n_rows > 31 else df
    print(dtypes)
    sample_size, _ = sample.shape

    inferred_types = []
    for col in sample.columns.values:
        inferred_types.append(infer_column_type(sample[col], df[col], col))

    db_type_map = []
    for idx, dtype in enumerate(inferred_types):
        print(f"Column: {sample.columns.values[idx]}")
        print(f"Type: {dtype[1][0]}")
        print(f"Categorical: {dtype[2]}")

        db_type_map.append({
            'colname':sample.columns.values[idx],
            'type': to_db_type(dtype[1][0]),
              })

        for k, v in dict(dtype[0]).items():
            print(k, v)
        print(f"_________________________")

    return db_type_map


if __name__ == "__main__":
    Logger.set_logger()
    logger = Logger.get_logger()
    logger.info("Starting..")
    df = pd.read_csv("../data/RL1.csv")
    print(df.head(3))

    db_type_map = infer(df)



    # Specify the Column Names while initializing the Table
    table = PrettyTable(["Attribute Name", "Data Type"])
    for attr in db_type_map:

        table.add_row([attr['colname'],attr['type']])

    print(table)
