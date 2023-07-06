import re
string = "Tfsfd243he price of this product is $123.45, and 24 43the di4324scount is 10%."
pattern = r"\d+\.\d+|\d+"
result = re.findall(pattern, string)
print(result)
number_list = []
for r in result:
    number_list.append(float(r))
print(number_list)