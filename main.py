import os
import shutil

directory = os.path.join(os.path.expanduser('~'), 'Downloads') # Change this to the folder you want to organize

# Add a key = file extension and a value = target folder.
# Example: '.pdf': 'Documents'

extensions = {
    '.pdf': 'Documents',
    '.mp3': 'Music',
    '.mp4': 'Videos',
    '.jpeg': 'Images',
    '.jpg': 'Images'
}

# Iterate over all files in the selected directory
 
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()


        # If extension is recognized, move the file
        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            location_path = os.path.join(folder_path, filename)

            #Move the file to target folder
            shutil.move(file_path, location_path)

            print(f'Moved {filename} to {folder_name} folder.')

        else:
            print(f'{filename}, unknown file extension.')
    else:
        print(f'{filename} is a directory')


print('Completed')

