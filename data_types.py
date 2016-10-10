import unittest


def data_type(anything=None):
  if anything is None:
	  return'no value'
  elif type(anything) == bool:
    return anything
  elif type(anything) == int:
    if anything < 100:
      return 'less than 100'
    elif anything is 100:
      return 'equal to 100'
    elif anything > 100:
      return 'more than 100'
  elif type(anything) == list:
    if len(anything)>=3:
		  return anything[2]
    else:
		  return None
  elif anything.isalpha() is True:
		return len(anything)


class DataTypeTestCase(unittest.TestCase):

  def test_none_type(self):
    self.assertEqual('no value', data_type(None))

  def test_array_type(self):
    self.assertEqual(3, data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', data_type(200))
  
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))


def main():
  unittest.main()

if __name__ == "__main__":
  main()