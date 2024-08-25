def parse(code):
    """
    The parameter "code" should be given as a list of integers from 0 to 255.
    This function will return the parsed code.
    """
    # Loop syntax is Æ(loop type)(code)Æ (131)
    # String syntax is È(string)È (133)
    # Base 128 numeric syntax is É(number)É (Extremely confusing I know) (134)
    