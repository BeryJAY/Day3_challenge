def whats_missing(given_list):
      first_list = [x for x in range(given_list[0], given_list[-1] + 1)]
      given_list = set(given_list)
      return (list(given_list ^ set(first_list)))

print(whats_missing([1,2,3,4,6,7,10]))
print(whats_missing([10,11,12,14,17]))
