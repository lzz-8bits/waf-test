import os,shutil

def copy_file(source_dir,target_dir):

    file_dir = os.path.dirname(__file__)
    #source_dir = os.path.join(file_dir,source_dirname)
    #target_dir = os.path.join(file_dir,target_dirname)
    print(source_dir)
    print(target_dir)

    if os.path.exists(target_dir):
        print("节点已存在，即将覆盖")
        shutil.rmtree(target_dir)
    shutil.copytree(source_dir,target_dir)