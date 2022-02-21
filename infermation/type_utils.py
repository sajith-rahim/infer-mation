def is_nan_numeric(value) -> bool:
    """
    Check for nan and inf
    """

    try:
        value = str(value)
        value = float(value)
    except Exception:
        return False

    try:
        if isinstance(value, float):
            a = int(value)  # noqa
        isnan = False
    except Exception:
        isnan = True

    return isnan


def cleanse(val):
    val = str(val).strip(' ')
    val = val.replace(',', '.')
    val = val.rstrip('"').lstrip('"')

    if val == '' or val == 'None' or val == 'nan':
        return None

    return -1
