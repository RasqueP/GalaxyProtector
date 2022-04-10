import os


def new_file_path(prefix, path):
    basename = os.path.basename(path)
    fileName = basename[:basename.rfind('.')]

    return f"{path[:len(basename)]}{prefix}_{fileName}.pyw"
