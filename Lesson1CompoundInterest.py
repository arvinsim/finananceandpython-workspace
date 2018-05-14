# Let's say you get 5% interest from your bank every year, what is it worth after 5 years?
# We could use a loop to print the value at each point

principal = 100
interest = 0.05
accumulated = principal

for t in range(5):
    accumulated = accumulated*(1+interest)
    print(accumulated)

# We might also wonder how much it increases by each period
# Notice how the amount of interest we get each period goes up. It grows with our investment
print('-----')
principal = 100
interest = .05
accumulated = principal

for t in range(5):
    last = accumulated
    accumulated = accumulated*(1+interest)
    print(accumulated-last)


# Run a loop, like before, but use the present value equation for each time.
print('-----')
principal = 100
interest = .05
years = 5

def value_of_investment(principal, interest, years):
    return principal * (1 + interest)**years

# print(value_of_investment(principal, interest, years))
# print(value_of_investment(100000, 0.07, 10))
t = list(range(26))
accumulated = [value_of_investment(principal, interest, x) for x in t]

import matplotlib.pyplot as plt
plt.plot(t, accumulated)
plt.xlabel("t")
plt.ylabel("Value")
plt.title("Compound Interest")
plt.show()