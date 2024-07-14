import os

def replace_in_file(filename):
    """Replace 'Riiverse' with 'Riiverse' in the specified file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace occurrences in the content
        new_content = content.replace('Riiverse', 'Riiverse')
        
        # Write the modified content back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated file: {filename}")
        
    except Exception as e:
        print(f"Error processing file {filename}: {e}")

def rename_file(old_name):
    """Rename the file if it contains 'Riiverse'."""
    new_name = old_name.replace('Riiverse', 'Riiverse')
    if old_name != new_name:
        try:
            os.rename(old_name, new_name)
            print(f"Renamed: {old_name} to {new_name}")
        except Exception as e:
            print(f"Error renaming file {old_name}: {e}")

def process_directory(directory):
    """Walk through the directory and process all files."""
    for root, _, files in os.walk(directory):
        for file in files:
            # Full file path
            file_path = os.path.join(root, file)
            
            # Rename file if necessary
            rename_file(file_path)
            
            # Replace content in the file
            replace_in_file(file_path)

if __name__ == "__main__":
    # Specify the directory you want to process
    directory_to_search = input("Enter the directory to search: ")
    process_directory(directory_to_search)
