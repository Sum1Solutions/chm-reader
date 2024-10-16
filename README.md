# CHM File Backup with App

This project provides a Python-based application for reading and displaying the contents of CHM (Compiled HTML Help) files. Plenty to do to make this a better solution, starting with the Search.

## Features

- Read and parse CHM files
- Web interface for displaying CHM contents

## Requirements

- Python 3.7+
- Flask
- pychm

## Installation and Usage

1. Clone this repository:
   ```
   git clone https://github.com/Sum1Solutions/chm-reader.git
   cd chm-reader
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

6. Then run the app to see the help:
   ```
   python app.py
   ```

7. Or open the generated index.html file in a browswer to see help files from within.

## File Structure

- `app.py`: Main Flask application
- `chm-reader.py`: CHM file parsing functionality
- `achelp.chm`: Sample CHM file (replace with your own)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
