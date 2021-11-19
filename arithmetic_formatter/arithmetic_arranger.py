#defined all the errors
class Error(Exception):
	"""Base class for all other exceptions"""
	pass
class TooManyProblemsError(Error):
	"""Raised when the problems are more than 5"""
	pass
class InvalidOperatorError(Error):
	"""Raised when the inputed operator isn't '+' or '-'"""
	pass
class InvalidOperandError(Error):
	"""
	Raised when an operand contains a value that isn't a digit
	"""
	pass
class TooManyDigitsError(Error):
	"""Raised when either operand has more than 4 digits"""
	pass


# the errors are not automatic because they are not in bulit

def error_check(problems):
	"""Function for that performs the error check"""
	try:
		if len(problems) > 5:
			raise TooManyProblemsError
		for problem in problems:
			words = problem.split()
			#print(words)
			if not ((words[1] == '+') or (words[1] == '-')):
				#print(words[1])
				#print(word)
				raise InvalidOperatorError
			if not (linear_search(words[0]) and linear_search(words[2])):
				raise InvalidOperandError
			if (len(words[0]) > 4 and len(words[2]) > 4):
				print(len(words[0]))
				print(len(words[2]))
				raise TooManyDigitsError
	except TooManyProblemsError:
		print("Error: Too many problems.")
	except InvalidOperatorError:
		print("Error: Operator must be '+' or '-'.")
	except InvalidOperandError:
		print("Error: Numbers must only contain digits.")
	except TooManyDigitsError:
		print("Error: Numbers cannot be more than four digits.")

def linear_search(string): 
	for char in string:
		if char.isdigit():
			
			continue
		else:
			return False
	return True

def arithmetic_arranger(problems, answer=False):
	error_check(problems)
	for problem in problems:
		words = problem.split()
		#print("\n",words, sep="")
		firstOperand = words[0]
		secondOperand = words[2]
		operatorused= words[1]
		largerOperand = get_operand_size(words, True)
		smallerOperand = get_operand_size(words)
		txt= """{:>1}{:<1}{:>1}"""
		print(txt.format(firstOperand,operatorused,secondOperand), sep="    ",end="")
		#print("large:",largerOperand," small: ",smallerOperand)

def get_operand_size(string, large=False):
	"""Gets the larger operand or the smaller operand"""
	#This logic works even if the numbers are the same
	if large:
		if int(string[0]) > int(string[2]):
			return string[0]
		else:
			return string[2]
	else:
		if int(string[0]) < int(string[2]):
			return string[0]
		else:
			return string[2]



arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

