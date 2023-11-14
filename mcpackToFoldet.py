import pathlib
import zipfile

# Nhập đường dẫn thư mục chứa các tệp .mcpack và .zip từ người dùng
path = pathlib.Path(input("Enter the directory path: "))

# Định nghĩa hàm để giải nén và xóa tệp .mcpack hoặc .zip
def extract_archive(archive):
    # Xác định loại tệp (mcpack hoặc zip) dựa trên đuôi (extension)
    file_extension = archive.suffix

    if file_extension.lower() in ('.mcpack', '.zip'):
        # Giải nén tệp .mcpack hoặc .zip
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            # Xác định thư mục đích cho việc giải nén
            target_folder = archive.parent.joinpath(archive.stem)
            zip_ref.extractall(target_folder)

        # Xóa tệp .mcpack hoặc .zip sau khi giải nén
        archive.unlink()

        # In thông báo về việc giải nén tệp lên console
        print(f"Extracted: {archive}")
    else:
        print(f"Skipped: {archive} (unsupported file type)")

try:
    # Lấy danh sách tất cả các tệp trong thư mục
    files = list(path.glob("*.mcpack")) + list(path.glob("*.zip"))

    # Giải nén từng tệp trong danh sách
    for file in files:
        extract_archive(file)

    # Thông báo khi xử lý hoàn thành
    print("Processing complete.")
except Exception as e:
    # Thông báo lỗi nếu có lỗi xảy ra
    print(f"An error occurred: {e}")
