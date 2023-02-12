import os
import shutil
import zipfile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


current_dir = os.path.dirname(__file__)
zip_file = f'{current_dir}\\data.zip'
cache_folder = f'{current_dir}\\cache'


def clean_cache():
    if (os.path.exists(cache_folder)):
        shutil.rmtree(cache_folder)
    os.mkdir(cache_folder)


def cache_zip(zip_path, cache_path):
    if (zipfile.is_zipfile(zip_path)):
        with zipfile.ZipFile(zip_path) as myzip:
            myzip.extractall(cache_path)


def cached_files():
    file_list = []
    with os.scandir(cache_folder) as cache:
        for text_file in cache:
            file_list.append(text_file.path)
    return file_list


def find_password(file_list):
    for text_file in file_list:
        with open(text_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if (line.find('password') != -1):
                    return (line[line.find(':')+2:]).rstrip()
