import os
import shutil

# File type mappings
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.jpeg'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Scripts': ['.py', '.js', '.sh'],
    'Archives': ['.zip', '.rar'],
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return 'Others'

def organize_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            category = get_category(file)
            category_path = os.path.join(folder_path, category)

            if not os.path.exists(category_path):
                os.makedirs(category_path)

            shutil.move(file_path, os.path.join(category_path, file))
            print(f"Moved {file} → {category}/")

# Run
if __name__ == "__main__":
    target_folder = input("Enter path to organize: ").strip()
    organize_folder(target_folder)
