import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'
postfix = [1, 2, 3]
source_object = glob.glob(source_path)
object_path = source_object[0]

object_name = object_path.split('/')[-1].split('\\')[-1].split('.')

prefix = object_name[0]
postfixTwo = object_name[1]

def make_zip(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, format), destination)
try:
    if postfixTwo == "txt":
        package_path = "./package"
        os.mkdir(package_path)
        tmp_data = []
        with open(source_object[0], "r") as file:
            tmp_data = file.readlines()
        for item in range(len(postfix)):
            current_data = ""
            for line in range((item + 1)*10):
                current_data += tmp_data[line]
            with open("./temporary.txt", "w") as file:
                file.write(current_data)
            file_name = prefix+"_"+str(item+1)+"."+postfixTwo
            shutil.copy("./temporary.txt", f"{package_path}/{file_name}")
        os.remove("./temporary.txt")
        make_zip(package_path, f"{destination_path}/ZipPackage.zip")
        shutil.unpack_archive(f"{destination_path}/ZipPackage.zip", destination_path)
        shutil.rmtree(package_path)

    elif postfixTwo== "py":
        try:
            os.system(f"python {object_path}")
        except:
            print("Error 404 not found.")
except:
    print("No file found.")