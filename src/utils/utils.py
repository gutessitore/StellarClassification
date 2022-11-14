import os


def get_project_root():
    """Returns project root folder."""
    project_folder_name = "StellarClassification"
    return os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    ).split(project_folder_name)[0] + project_folder_name


def get_data_path():
    """Returns data folder path."""
    return os.path.join(get_project_root(), "data")

