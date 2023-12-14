PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as file_name:
    names = file_name.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()


    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/completed_letter_for_{stripped_name}.txt", "w") as completed:
            completed.write(new_letter)



