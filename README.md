# DCS Livery Compression Tool

A simple graphical tool designed to efficiently compress Digital Combat Simulator (DCS) livery folders while maintaining folder structure integrity.

## Features

- User-friendly graphical interface
- Batch compression of multiple livery folders
- High compression ratio using LZMA algorithm
- Preserves internal folder structure
- Multi-threaded processing for faster compression
- Creates individual zip files for each livery folder

## Usage

1. Launch the application
2. Click "Select Folder" to choose the directory containing your DCS livery folders
3. Click "Run" to begin the compression process
4. Each livery folder will be compressed into a separate .zip file in the same location

## Technical Details

- Uses LZMA compression with maximum compression level (9)
- Automatically processes all folders in the selected directory
- Parallel processing with up to 4 threads for optimal performance
- Creates zip files with the same name as the original folders

## Use Cases

- Compress livery folders before sharing
- Reduce storage space used by livery collections
- Prepare liveries for distribution or backup
- Maintain organized livery archives

## Requirements

- Python 3.x
- tkinter (usually included with Python)
