# DCS Livery Compression Tool

A powerful graphical tool designed to efficiently compress and manage Digital Combat Simulator (DCS) livery folders while maintaining folder structure integrity.

## Features

- User-friendly graphical interface
- Batch compression of multiple livery folders
- High compression ratio using LZMA algorithm
- Preserves internal folder structure
- Multi-threaded processing for faster compression
- Creates individual zip files for each livery folder
- Progress tracking with status bar
- Detailed compression statistics
- Support for custom output directory selection
- Automatic file size optimization
- Error handling and reporting

## Usage

1. Launch the application
2. Click "Select Input Folder" to choose the directory containing your DCS livery folders
3. Click "Select Output Folder" to choose where compressed files will be saved
4. Click "Run" to begin the compression process
5. Monitor progress through the status bar
6. Review compression results in the statistics panel

## Technical Details

- Uses LZMA compression with maximum compression level (9)
- Automatically processes all folders in the selected directory
- Parallel processing with up to 4 threads for optimal performance
- Creates zip files with the same name as the original folders
- Real-time progress tracking and status updates
- Intelligent error handling and recovery
- Customizable output directory structure

## Use Cases

- Compress livery folders before sharing
- Reduce storage space used by livery collections
- Prepare liveries for distribution or backup
- Maintain organized livery archives
- Batch process multiple livery folders
- Create compressed backups with custom locations

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- Available disk space for compressed files

## Statistics and Reporting

- Compression ratio display
- Processing time tracking
- Space saved calculations
- Success/failure reporting
- Individual file progress tracking
