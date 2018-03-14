name = "Michaela"

subjects = ["English", "Latin", "Math", "History", "Science"]

print("My name is " + name)

for i in subjects:
    print("I take " + i + " as one of my classes.")


characters = ["Harry James Potter", "Ron Billius Weasley", "Hermione Jean Granger",]

for i in characters:
    if i == "Harry James Potter":
        print("Harry Potter is thought to be the main charater in Harry Potter, but, in my opinion, it is not in fact him, but the Weasley family. Yes, he can be considered the main person, but I could also argue it could be Lord Voldemort. It really depends on your perspective on the book")
    elif i == "Ron Billius Weasley":
        print("Ron has six sibilings")
    else:
        print(i + " is apart of the golden trio in Harry Potter.")


characters = []

while True:
    print("what are YOUR favorite Harry Potter characters? Type 'end' to stop program")
    answer = input()
    if answer == "end":
        break
    else:
        characters.append(answer)
    
    

