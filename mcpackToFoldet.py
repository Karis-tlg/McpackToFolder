import glob
import os
import zipfile as zip

root = input("Enter the directory path: ")
ext = (".zip", ".mcpack")

for file in glob.glob(f"{root}/**/*", recursive = True):
    if file.endswith(ext):
        try:
            with zip.ZipFile(file, "r") as zipr:
                zipr.extractall(root)
                print(f"Extracted: {file}")
            os.remove(file)
        except Exception as e:
            print(f"An error occurred while extracting {file}: {e}")
    else:
        print(f"Skipped: {file} (unsupported file type)")

print("Processing complete.")
