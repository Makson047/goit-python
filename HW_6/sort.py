import os
import pathlib
import re
import shutil
import sys


def folder_processing(path, protected_folders):
    """Create list with all files"""
    fileCollections = []

    def __handler(path, protected_folders):
        p = pathlib.Path(path)
        if p not in protected_folders:
            fileCollections.append(p)
            for item in p.iterdir():
                if item.is_file():
                    fileCollections.append(item)
                else:
                    __handler(item, protected_folders)

    __handler(path, protected_folders)
    return fileCollections


def to_latin(name):
    """Convert all symbols to latin"""
    symbols = (u"іїєабвгдеёжзийклмнопрстуфхцчшщъыьэюяІЇЄАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
               u"iieabvgdeejzijklmnoprstufhzcss_y_euaIIEABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

    tr = {ord(a): ord(b) for a, b in zip(*symbols)}
    translated_name = name.translate(tr)
    translated_name = re.sub("[^A-Za-z0-9]", "_", translated_name)
    return translated_name


def normalize(element):
    """Change file name"""
    element_name = element.name
    path = str(element)[:-len(element_name)]
    if element.is_file():
        element_suffix = element.suffix
        element_name = element_name.rsplit(element_suffix)
        translated_name = to_latin(element_name[0])
        name = f'{translated_name}{element_suffix}'
    else:
        name = to_latin(element_name)
    normalized_name = path + name
    # print(normalized_name)
    return normalized_name


def remove_empty_folders(path_abs, protected_folders):
    """Delete empty folders"""
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if pathlib.Path(path) not in protected_folders:
            if len(os.listdir(path)) == 0:
                os.rmdir(path)


def sorting(folder_path):
    """Sort all files in folder"""

    # Creating empty storages
    file_types = {}
    key_types = ['images', 'document', 'audio', 'video', 'archives', 'unknown_file']
    protected_folders = []
    for key in key_types:
        file_types[key] = []
    known_extensions = set()
    unknown_extensions = set()

    for new_fold in key_types:
        # Filling the list with folders that are protected
        protected_path = f'{str(folder_path)}\\{new_fold}'
        protected_folders.append(pathlib.Path(protected_path))
        # Create folders to main type of elements
        if not os.path.exists(f'{str(folder_path)}\\{new_fold}'):
            os.makedirs(f'{str(folder_path)}\\{new_fold}')

    collections = folder_processing(folder_path, protected_folders)

    # Checking if the source folder is empty
    if len(collections) <= 1:
        return print("Your folder is empty!!!")

    # Loop through all files and folders
    for element in collections:
        normalized_name = normalize(element)

        # Renaming the file
        try:
            os.rename(element, normalized_name)
        except FileExistsError:
            print(f'File with name {normalized_name} already exists, please try enter another name')

        normalized_name = pathlib.Path(normalized_name)

        # Sort all files
        if not normalized_name.is_dir():

            if normalized_name.suffix in ['.jpeg', '.png', '.jpg', '.svg']:
                path_for_images = f"{str(folder_path)}\\images\\{normalized_name.name}"
                try:
                    # Move files to folder by appropriate type
                    os.replace(normalized_name, path_for_images)
                except FileExistsError:
                    print(f'File with name {path_for_images} already exists, please try enter another name')

                file_types['images'].append(path_for_images)  # Filling dict with sorted files
                path_for_images = pathlib.Path(path_for_images)
                known_extensions.add(path_for_images.suffix)  # Filling list with known file types

            elif normalized_name.suffix in ['.avi', '.mp4', '.mov', '.mkv']:
                path_for_video = f"{str(folder_path)}\\video\\{normalized_name.name}"
                try:
                    os.replace(normalized_name, path_for_video)
                except FileExistsError:
                    print(f'File with name {path_for_video} already exists, please try enter another name')

                file_types['video'].append(path_for_video)
                path_for_video = pathlib.Path(path_for_video)
                known_extensions.add(path_for_video.suffix)

            elif normalized_name.suffix in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                path_for_document = f"{str(folder_path)}\\document\\{normalized_name.name}"
                try:
                    os.replace(normalized_name, path_for_document)
                except FileExistsError:
                    print(f'File with name {path_for_document} already exists, please try enter another name')

                file_types['document'].append(path_for_document)
                path_for_document = pathlib.Path(path_for_document)
                known_extensions.add(path_for_document.suffix)

            elif normalized_name.suffix in ['.mp3', '.ogg', '.wav', '.amr']:
                path_for_audio = f"{str(folder_path)}\\audio\\{normalized_name.name}"
                try:
                    os.replace(normalized_name, path_for_audio)
                except FileExistsError:
                    print(f'File with name {path_for_audio} already exists, please try enter another name')

                file_types['audio'].append(path_for_audio)
                path_for_audio = pathlib.Path(path_for_audio)
                known_extensions.add(path_for_audio.suffix)

            elif normalized_name.suffix in ['.zip', '.gz', '.tar']:
                archive_name = str(normalized_name.name)[:-len(normalized_name.suffix)]
                archives_folder = f"{str(folder_path)}\\archives\\{archive_name}"
                path_for_archives = f"{archives_folder}\\{normalized_name.name}"
                # Creating folders with archive name
                if not os.path.exists(archives_folder):
                    os.makedirs(archives_folder)
                try:
                    # Unpacking archive
                    shutil.unpack_archive(normalized_name, archives_folder)
                    # Delete unzipped file
                    os.remove(normalized_name)
                except:
                    try:
                        # If we have are problems with unpacking,
                        # than we replace archive to folder by appropriate type
                        os.replace(normalized_name, path_for_archives)
                    except FileExistsError:
                        print(f'File with name {path_for_archives} already exists, please try enter another name')

                file_types['archives'].append(path_for_archives)
                path_for_archives = pathlib.Path(path_for_archives)
                known_extensions.add(path_for_archives.suffix)

            else:
                path_for_unknown = f"{str(folder_path)}\\unknown_file\\{normalized_name.name}"
                try:
                    os.replace(normalized_name, path_for_unknown)
                except FileExistsError:
                    print(f'File with name {path_for_unknown} already exists, please try enter another name')

                file_types['unknown_file'].append(path_for_unknown)
                path_for_unknown = pathlib.Path(path_for_unknown)
                unknown_extensions.add(path_for_unknown.suffix)
    try:
        # Delete empty folders
        remove_empty_folders(folder_path, protected_folders)
    except Exception as error:
        print(f'You have are problems:\n{error}')

    return file_types, known_extensions, unknown_extensions


if __name__ == '__main__':
    # Running a script with a command
    try:
        folder_name = sys.argv[1]
    except:
        print('Incorrect folder path!')
        folder_name = input('Please enter correct folder path:\n')

    # folder_name = 'M:\\Max\\xiaomi redmi3\\Download\\to_rename'
    folder_path = pathlib.Path(folder_name)
    try:
        file_types, known_extensions, unknown_extensions = sorting(folder_path)
    except Exception as error:
        print(f'You have are problems:\n{error}')
