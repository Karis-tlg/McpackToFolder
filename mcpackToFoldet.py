import glob
import os
import zipfile

root = input("Enter the directory path: ")
ext = (".zip", ".mcpack")

for file in glob.glob(os.path.join(root, "*")):
    if file.endswith(ext):
        print(f"Extracted: {file}")
        try:
            with zipfile.ZipFile(file, "r") as zip_ref:
                zip_ref.extractall(root)
            os.remove(file)
        except Exception as e:
            print(f"An error occurred while extracting {file}: {e}")
    else:
        print(f"Skipped: {file} (unsupported file type)")

print("Processing complete.")
