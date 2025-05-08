def read_file():
    try:
        with open("sample.txt", "w") as file:
            file.write("Line 1: This is a sample text file\n")
            file.write("Line 2: It contains multiple lines.")
        with open("sample.txt", "r") as file:
            print("Reading File Content!!")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File does not exist")

read_file()