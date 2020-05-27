user_text = raw_input("Enter filename: ")
file = open(user_text, "w+")
user_values = raw_input("Enter file text: ")
file.write(user_values)


number_of_lines = 0
number_of_words = 0
number_of_characters = 0

with open(user_text) as file:
    for line in file:
        line = line.strip("\n")
        words = line.split()
        number_of_lines += 1
        number_of_words += len(words)
        number_of_characters += len(line)


print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)