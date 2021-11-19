# Multiply two polynomials
def multiply(poly1, poly2):
	len_poly1 = len(poly1)
	len_poly2 = len(poly2)
	result = []
	result_len = len_poly1 + len_poly2 - 1

	for i in range(result_len):
		result.append(0)

	for i in range(len_poly1):
		for j in range(len_poly2):
			result[i+j] += poly1[i] * poly2[j]

	return result


answer = multiply( [0, 1, 2, 3], [5, 4, 3, 2])
print(answer)


