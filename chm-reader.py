import os
import chm

def read_chm_file(file_path):
    # Verify that the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return
    
    # Open the CHM file
    try:
        chm_file = chm.CHMFile(file_path)
        
        # List all topics (files) in the CHM file
        print("Listing all topics in the CHM file:")
        for topic in chm_file.files:
            print(topic)
        
        # Read a specific topic (e.g., "/index.html")
        topic_path = "/index.html"  # replace with the actual topic path if known
        if chm_file.file_exists(topic_path):
            data = chm_file.get_file(topic_path)
            print(f"\nContent of {topic_path}:")
            print(data.decode("utf-8"))  # Assuming UTF-8 encoding
        else:
            print(f"The topic '{topic_path}' does not exist in the CHM file.")
    except Exception as e:
        print(f"Error opening the CHM file: {e}")

# Path to your CHM file
file_path = "./achelp.chm"
read_chm_file(file_path)
