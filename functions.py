import os
import zipfile
from concurrent.futures import ThreadPoolExecutor

def compress_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    zip_filename = os.path.join(os.path.dirname(folder_path), f"{folder_name}.zip")
    with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Preserve the folder structure inside the zip file
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname=arcname)

def compress_folders_in_directory(directory):
    folder_list = [
        os.path.join(directory, item)
        for item in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, item))
    ]
    if not folder_list:
        return False  # No folders found
    # Use ThreadPoolExecutor to compress folders in parallel
    max_workers = min(4, len(folder_list))  # Adjust the number of threads as needed
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(compress_folder, folder_path) for folder_path in folder_list]
        for future in futures:
            future.result()  # Wait for all tasks to complete
    return True  # Compression complete

def get_file_names_in_folder(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == '.zip':
                file_names.append(name)  # Append the file name without '.zip'
            else:
                file_names.append(file)  # Append the full file name
    return file_names
