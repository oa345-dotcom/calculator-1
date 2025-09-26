from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def test_calculator_operations():
	assert add(2, 3) == 5
	assert subtract(5, 2) == 3
	assert multiply(4, 3) == 12
	assert divide(10, 2) == 5
	try:
		divide(5, 0)
		assert False, "Division by zero should raise ValueError"
	except ValueError:
		pass

if __name__ == "__main__":
	test_calculator_operations()
	print("All tests passed.")
