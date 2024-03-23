import glob, os, zipfile

while True:
    root = input("Enter the directory path: ")
    if os.path.isdir(root):
        break
    else:
        print("Please enter a valid directory path.")

ext = (".zip", ".mcpack")

for file in glob.glob(f"{root}/*", recursive=True):
    if file.endswith(ext):
        try:
            with zipfile.ZipFile(file, "r") as zip:
                folder = os.path.splitext(file)[0]
                zip.extractall(os.path.join(root, folder))              
                print(f"Extracted: {file}")
            os.remove(file)
        except zipfile.BadZipFile as e:
            print(f"An error occurred while extracting {file}: {e}")
    else:
        print(f"Skipped: {file} (unsupported file type)")
