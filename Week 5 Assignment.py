def modify_content(content):
    """
    Simple modification function:
    Converts text to uppercase.
    You can change this logic if needed.
    """
    return content.upper()


def main():
    filename = input("Enter the filename to read: ")

    try:
        # Read the original file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You cannot read/write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
