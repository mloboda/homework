import os
import shutil
import datetime


def copy_text_files(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            if file_name.endswith('.txt'):
                source_file = os.path.join(root, file_name)
                destination_file = os.path.join(destination_dir, file_name)
                shutil.copy(source_file, destination_file)

                print(f'<{datetime.datetime.now()}>: <{source_file}>: <{destination_file}>')


source_directory = 'D:\ma_python\homework\homework_module_6\\text_files'
destination_directory = 'D:\ma_python\homework\homework_module_6\my\\files'

copy_text_files(source_directory, destination_directory)
