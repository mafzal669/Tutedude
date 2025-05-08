# Step 1: Take user input and write it to output.txt
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")
 
# Step 2: Take additional input and append it to output.txt
additional_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")
 
# Step 3: Read and display the final content of output.txt
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
 
