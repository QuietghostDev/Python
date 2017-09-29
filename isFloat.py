def isFloat(number):
    try:
        float(number)
        return True
    except (ValueError, TypeError):
        return False
