
sentence = "Novantas is fun"
string_list = list(sentence)
result_list = []

counter = len(string_list) - 1
while counter >= 0:
    result_list.append(string_list[counter])
    counter -= 1

print("".join(string_list))


for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)







