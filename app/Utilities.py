
def compareFloatNumbers(a : float, b : float):

    retval = False

    try:
        a_float = float(a)
        b_float = float(b)
        retval = (abs(a_float - b_float) < 1e-9)
    except:
        retval = False
    # finally:
    #     retval = False

    return retval


