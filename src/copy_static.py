import os
import shutil

def delete_public(public_path):
    if os.path.exists(public_path):
        return shutil.rmtree(public_path)
    return

def generate_new_public(public_path):
    if os.path.exists(public_path) == False:
        return os.mkdir(public_path)
    return

def copy_static(path_src, path_des):
    file_list = os.listdir(path_src)
    for file in file_list:
        if os.path.isfile(os.path.join(path_src, file)):
            shutil.copy(os.path.join(path_src, file), path_des)
        else:
            try: 
                os.mkdir(os.path.join(path_des, file))
            except:
                continue
            new_src_path = os.path.join(path_src, file)
            new_des_path = os.path.join(path_des, file)
            copy_static(new_src_path,new_des_path)
                