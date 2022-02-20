import enum

class dtypes(enum.Enum):
    # Numerical type data
    integer = "integer"
    float = "float"

    # Dates and Times (time-series)
    date = "date"
    datetime = "datetime"

    empty = "empty"
    invalid = "invalid"
