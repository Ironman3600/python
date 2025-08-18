#1
# file1 = open("myfile.txt", "r")
# reading_file = file1.read()
# print(reading_file)
# file1.close()
#if you open file you need to close

#2
# with open("file.txt") as file:

# file1 = open("file.txt", "w")
# writing_file = file1.write("Hello World")
# print(writing_file)
# file1.close()
# file1 = open("file.txt", "r")
# reading_file = file1.read()
# print(reading_file)
# file1.close()
#


try:
    with open("myfile.txt", "w") as file:
        initial_text = input("Enter text to write to the file: ")
        file.write(initial_text)
        print("Data successfully written to file.txt")

    with open("myfile.txt", "a") as file:
        additional_text = input("Enter additional text to append: ")
        file.write("\n" + additional_text)  # Add newline for clarity
        print("Data successfully appended ")

    with open("myfile.txt", "r") as file:
        final_content = file.read()
        print("Final content of output.txt:")
        print(final_content)

except FileNotFoundError:
    print("Error: The file could not be found.")
