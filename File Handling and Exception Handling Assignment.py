# File Read & Write Challenge with Error Handling

def main():
    try:
        # Ask the user for the filename to read
        input_file = input("Enter the name of the file to read: ")

        # Open and read the original file
        with open(input_file, "r") as file:
            content = file.read()

        # Modify content (example: convert all text to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read/write the file. Please check permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
