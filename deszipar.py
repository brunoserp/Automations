import zipfile
import os
import shutil


def unzip_zip_file(zip_file_path, extraction_dir):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_dir)

def process_folder(input_folder, output_folder):
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if os.path.isdir(item_path):
            # If it's a directory, create a corresponding directory in the output folder
            os.makedirs(os.path.join(output_folder, item), exist_ok=True)
            # Recursively process the subfolder
            process_folder(item_path, os.path.join(output_folder, item))
        elif item.endswith('.zip'):
            # If it's a ZIP file, unzip it to the output folder

            unzip_zip_file(item_path, output_folder)
        else:
            # If it's not a ZIP file, copy it to the output folder
            shutil.copy(item_path, output_folder)

# Specify the input folder containing files and possibly nested ZIPs
input_folder = input("Insira o caminho da pasta (apenas clique com o botão direito pra colar)\n").replace('\\','/')

# Specify the output folder where you want to copy files and unzip ZIPs
output_folder = input("Insira o caminho pasta onde vc queira deszipar:\n").replace('\\','/')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Start processing the input folder
process_folder(input_folder, output_folder)

while any(item.endswith('.zip') for item in os.listdir(output_folder)):
    # Find and process any remaining ZIP files
    for item in os.listdir(output_folder):
        item_path = os.path.join(output_folder, item)
        if item.endswith('.zip'):
            unzip_zip_file(item_path, output_folder)
            os.remove(item_path)