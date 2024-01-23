import os
import random

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def shuffle_lines(lines):
    random.shuffle(lines)

def quiz(lines):
    for line in lines:
        parts = line.split('/')
        phrases = parts[0].strip()
        plural_form = parts[1].strip().split()[1]

        print(phrases.split()[1])
        
        answer1 = input(f"What is the artikel for: {phrases.split()[1]}? ").strip()
        if answer1 == phrases.split()[0]:
            print("Correct!")
        else:
            print(f"Wrong answer. The correct answer is {phrases.split()[0]}")

        answer2 = input(f"What is the plural form of the word? die ").strip()
        if answer2 == plural_form:
            print("Correct!")
        else:
            print(f"Wrong answer. The correct answer is {plural_form}")

def main():
    folder_path = "words"
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    print("List of available txt files:")
    for i, txt_file in enumerate(txt_files):
        print(f"{i + 1}. {txt_file}")

    try:
        file_index = int(input("Choose a file to quiz (enter the corresponding number): ")) - 1
        selected_file = os.path.join(folder_path, txt_files[file_index])

        lines = read_txt_file(selected_file)
        shuffle_lines(lines)
        quiz(lines)

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid file number.")

if __name__ == "__main__":
    main()
