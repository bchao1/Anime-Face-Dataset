"""Remove empty jpg files"""
import os

# Specify your own image directory here
target_folder = "/cropped"

with os.scandir(target_folder) as it:
    for entry in it:
        file_dir = os.path.join(target_folder, entry.name)
        if os.stat(file_dir).st_size == 0:
            try:
                os.remove(file_dir)
                print("Empty file %s is removed" % entry.name)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
