def is_float(str_int):
    try:
        float(str_int)
        return True
    except ValueError:
        return False
