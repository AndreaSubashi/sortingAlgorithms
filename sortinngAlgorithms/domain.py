import secrets

def generate_random_array(size, lower_bound, upper_bound):
   #(upper_bound - lower_bound + 1) calculates the size of the range, adding 1 to include the upper bound
   # +lower_bound to adjust it to start from the lower bound
    return [secrets.randbelow(upper_bound - lower_bound + 1) + lower_bound for _ in range(size)]

# Example usage:
lower_bound = 1
upper_bound = 2**31
size1 = 100
size100_1 = generate_random_array(size1, lower_bound, upper_bound)

size2 = 200
size200_1 = generate_random_array(size2, lower_bound, upper_bound)

size3 = 500
size300_1 = generate_random_array(size3, lower_bound, upper_bound)

size4 = 1000
size400_1 = generate_random_array(size4, lower_bound, upper_bound)

size5 = 10000
size500_1 = generate_random_array(size5, lower_bound, upper_bound)

