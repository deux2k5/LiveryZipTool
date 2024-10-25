import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
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
    folder_list = [os.path.join(directory, item) for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]
    if not folder_list:
        messagebox.showinfo("No Folders Found", "No folders were found in the selected directory.")
        return
    # Use ThreadPoolExecutor to compress folders in parallel
    max_workers = min(4, len(folder_list))  # Adjust the number of threads as needed
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(compress_folder, folder_path) for folder_path in folder_list]
        for future in futures:
            future.result()  # Wait for all tasks to complete
    messagebox.showinfo("Compression Complete", "All folders have been compressed.")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        selected_directory.set(directory)

def run_compression():
    directory = selected_directory.get()
    if directory:
        compress_folders_in_directory(directory)
    else:
        messagebox.showwarning("No Directory Selected", "Please select a directory first.")

def main():
    global selected_directory
    root = tk.Tk()
    root.title("Folder Compressor")
    root.geometry("400x150")
    
    selected_directory = tk.StringVar()
    
    select_button = tk.Button(root, text="Select Folder", command=select_directory)
    select_button.pack(pady=10)
    
    directory_label = tk.Label(root, textvariable=selected_directory)
    directory_label.pack()
    
    run_button = tk.Button(root, text="Run", command=run_compression)
    run_button.pack(pady=10)
    
    root.mainloop()

if __name__ == '__main__':
    main()
