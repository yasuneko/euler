curr = 1
prev = 1

even_sum = 0

while curr < 4000000:
	if curr%2 == 0:
		even_sum += curr
	next = curr + prev
	prev = curr
	curr = next

print even_sum
