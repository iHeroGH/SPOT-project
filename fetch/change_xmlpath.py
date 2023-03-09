import os
import xml.etree.ElementTree as ET

# Define the new path string
new_path = r'C:\Users\jojom\OneDrive\Desktop\School\SPOT_project\fetch\can\images'

# Loop through all the XML files in the directory
# Make sure in directory that contains annotations folder
# Loop through all the directories and files within the annotations folder
print(new_path)

for dirpath, dirnames, filenames in os.walk('can/annotations/test'):
    for filename in filenames:
        if not filename.endswith('.xml'):
            continue

        # Load the XML file and find the path element
        tree = ET.parse(os.path.join(dirpath, filename))
        path_elem = tree.find('path')

        # Get the filename without extension
        filename_without_extension = os.path.splitext(filename)[0]

        # Create the new path string
        new_path_to_image = os.path.join(new_path, filename_without_extension + '.jpg')

        # Replace the path with the new value
        path_elem.text = new_path_to_image

        # Save the modified XML file
        tree.write(os.path.join(dirpath, filename))