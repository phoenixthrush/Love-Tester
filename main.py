from collections import Counter

print("Love Tester\n")

foo = input("First Name: ")
bar = input("Second Name: ")

conc = sorted((foo + bar).lower())
char_count = list(Counter(conc).values())

while len(char_count) > 2 or int("".join(map(str, char_count))) > 100:
    new_list = []

    while len(char_count) > 1:
        new_list.append(char_count.pop(0) + char_count.pop(-1))

    if char_count:
        new_list.append(char_count.pop(0))

    char_count = [int(d) for d in "".join(map(str, new_list))]

result = "".join(map(str, char_count))

print(f"\n{foo.title()} & {bar.title()}:")
print(f"=> {result}%")
