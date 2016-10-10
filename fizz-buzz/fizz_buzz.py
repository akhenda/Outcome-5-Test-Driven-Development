def print_and_return(input):
    print input
    return input

def fizz_buzz(number):
	if number % 3 == 0 and number % 5 == 0:
		return print_and_return('FizzBuzz')
	elif number % 5 == 0:
		return print_and_return('Buzz')
	elif number % 3 == 0:
		return print_and_return('Fizz')
	else:
		return print_and_return(number)
