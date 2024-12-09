###
# Functions to read any data type from the keyboard
#
def input_string(message):
    output = input(message)
    return output

def input_integer(message):
    output = int(input(message))
    return output

def input_real(message):
    output = float(input(message))
    return output

def input_boolean(message):
    output = input(message)
    if output in ['t', 'T', 'true', 'True', 'y', 'Y']:
        return True
    elif output in ['f', 'F', 'false', 'False', 'n', 'N']:
        return False