import tkinter as tk
from tkinter import filedialog, messagebox
from functions import compress_folders_in_directory, get_file_names_in_folder

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        selected_directory.set(directory)

def run_compression():
    directory = selected_directory.get()
    if directory:
        result = compress_folders_in_directory(directory)
        if result:
            messagebox.showinfo("Compression Complete", "All folders have been compressed.")
        else:
            messagebox.showinfo("No Folders Found", "No folders were found in the selected directory.")
    else:
        messagebox.showwarning("No Directory Selected", "Please select a directory first.")

def run_list_files():
    directory = selected_directory.get()
    if directory:
        file_names = get_file_names_in_folder(directory)
        if file_names:
            # Display the file names in a new window
            file_list_window = tk.Toplevel(root)
            file_list_window.title("File Names")
            text_widget = tk.Text(file_list_window, wrap="none")
            text_widget.pack(expand=True, fill='both')
            # Add scrollbars
            y_scrollbar = tk.Scrollbar(file_list_window, orient='vertical', command=text_widget.yview)
            y_scrollbar.pack(side='right', fill='y')
            text_widget.configure(yscrollcommand=y_scrollbar.set)
            # Insert the file names
            for file_name in file_names:
                text_widget.insert('end', file_name + '\n')
        else:
            messagebox.showinfo("No Files Found", "No files were found in the selected directory.")
    else:
        messagebox.showwarning("No Directory Selected", "Please select a directory first.")

def main():
    global root
    root = tk.Tk()
    root.title("Folder Compressor")
    root.geometry("400x200")
    
    global selected_directory
    selected_directory = tk.StringVar()
    
    select_button = tk.Button(root, text="Select Folder", command=select_directory)
    select_button.pack(pady=10)
    
    directory_label = tk.Label(root, textvariable=selected_directory)
    directory_label.pack()
    
    run_button = tk.Button(root, text="Compress Folders", command=run_compression)
    run_button.pack(pady=10)
    
    list_files_button = tk.Button(root, text="List Files", command=run_list_files)
    list_files_button.pack(pady=10)
    
    root.mainloop()

if __name__ == '__main__':
    main()
