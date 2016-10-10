
def print_and_return(input):
  print input
  return input

def data_type(anything=None):
  if anything is None:
    return print_and_return('no value')
  elif type(anything) == bool:
    return print_and_return(anything)
  elif type(anything) == int:
    if anything < 100:
      return print_and_return('less than 100')
    elif anything is 100:
      return print_and_return('equal to 100')
    elif anything > 100:
      return print_and_return('more than 100')
  elif type(anything) == list:
    if len(anything) >= 3:
      return print_and_return(anything[2])
    else:
      return print_and_return(None)
  elif anything.isalpha() is True:
    return print_and_return(len(anything))
