# CHM File Backup with App

This project provides a Python-based application for reading and displaying the contents of CHM (Compiled HTML Help) files. It includes a web interface for easy navigation and viewing of the CHM file contents.

## Features

- Read and parse CHM files
- Web interface for displaying CHM contents
- Easy navigation through CHM file structure

## Requirements

- Python 3.7+
- Flask
- pychm

## Installation and Usage

1. Clone this repository:
   ```
   git clone https://github.com/Sum1Solutions/chm-file-backup-with-app.git
   cd chm-file-backup-with-app
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Place your CHM file in the project directory (by default, the app looks for `achelp.chm`).

5. Run the CHM reader script:
   ```
   python chm-reader.py
   ```

6. Then run:
   ```
   python app.py
   ```

7. And then open the generated index.html file in a browswer to see help files and a start to a web app.

## File Structure

- `app.py`: Main Flask application
- `chm-reader.py`: CHM file parsing functionality
- `achelp.chm`: Sample CHM file (replace with your own)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
