import glob
import in_place

path_to_folder = "D:\\Flutter\\YOLO_V2\\darkflow-master\\train\\annotation"

old = "/content/drive/MyDrive/Colab Notebooks/blog.tensorflow/workspace/images/allImages/"
new = "D:\\Flutter\\YOLO_V2\\darkflow\\train\\Images\\"

for filepath in glob.glob( path_to_folder+'/*.xml'):
    with in_place.InPlace(filepath) as file:
        for line in file:
            if old in line:
                line = line.replace(old, new)
            file.write(line)
