import glob
import os
import zipfile

root = input("Enter the directory path: ")
ext = (".zip", ".mcpack")

if not os.path.exists(root):
    print(f"Error: The specified directory path does not exist")
    exit()

for file in glob.glob(f"{root}/*", recursive=True):
    if file.endswith(ext):
        try:
            with zipfile.ZipFile(file, "r") as zip:
                folder = os.path.splitext(os.path.basename(file))[0]
                zip.extractall(os.path.join(root, folder))              
                print(f"Extracted: {file}")
            os.remove(file)
        except Exception as e:
            print(f"An error occurred while extracting {file}: {e}")
    else:
        print(f"Skipped: {file} (unsupported file type)")

print("Processing complete.")
