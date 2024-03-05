#!/usr/bin/python3


"""
module to create instance of 'Filestorage'

creates storage (an instance of FileStorage) and
calls reload() method
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
