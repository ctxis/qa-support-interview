import os

from django.core.files.storage import default_storage


def handle_uploaded_file(f):
    save_path = os.path.join('uploads', f.name)
    path = default_storage.save(save_path, f)

    return default_storage.path(path)