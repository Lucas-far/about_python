

# --------------------------------------- List comprehension na forma pythônica ---------------------------------------
var = ['A', 'B', 'C']
var2 = [word.lower() for word in var]  #
print(var2)

# -------------------------------------- List comprehension na forma não pythônica--------------------------------------
for index, word in enumerate(var):
    var[index] = word.lower()

print(var)
