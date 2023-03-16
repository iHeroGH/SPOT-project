import os
import xml.etree.ElementTree as ET

# Define the new path string
#new_path = r'C:\Users\jojom\OneDrive\Desktop\School\SPOT_project\fetch\can\images'

#new_path = r'C:\Users\jojom\OneDrive\Desktop\School\SPOT_project\fetch\trashcan\images'


# The type of image
img_dir = 'trashcan'

# The camera mode
cam_mode = 'back_cam'

# The created annotations directory
img_annotation_dir = "../" + img_dir + '/annotations/xml/' + cam_mode

# The path to set all xml files' images to
new_path = r'C:\Users\jojom\OneDrive\Desktop\School\SPOT_project\fetch' + f"\\{img_dir}\\images\\{cam_mode}"

# Loop through all the XML files in the directory
# Loop through all the directories and files within the annotations folder
print(img_annotation_dir, new_path)
for dirpath, dirnames, filenames in os.walk(img_annotation_dir):
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