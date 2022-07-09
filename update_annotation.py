import glob
import in_place

path_to_folder = r"/content/Train-Your-Own-Custom-Object-Detection-Model-for-Flutter-with-Tiny-Yolov2/train/annotation/"

old = "D:\\yolo\\labelthis\\"
new = "/content/Train-Your-Own-Custom-Object-Detection-Model-for-Flutter-with-Tiny-Yolov2/train/Images/"

for filepath in glob.glob( path_to_folder+'/*.xml'):
    with in_place.InPlace(filepath) as file:
        for line in file:
            if old in line:
                line = line.replace(old, new)
            file.write(line)
