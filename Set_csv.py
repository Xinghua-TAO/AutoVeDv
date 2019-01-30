import os


def csv_path(video):
    current_path = os.path.abspath(video)
    csv_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + 'temp_file.csv')

    return csv_path
