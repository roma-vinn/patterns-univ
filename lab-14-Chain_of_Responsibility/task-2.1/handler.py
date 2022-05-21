from abc import ABC, abstractmethod
import os


class Handler(ABC):
    def __init__(self):
        self._next = None

    @abstractmethod
    def open(self, file_path: str):
        pass

    def set_next(self, handler):
        self._next = handler


class PreviewHandler(Handler):
    _valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf']

    def __init__(self):
        super(PreviewHandler, self).__init__()

    def open(self, file_path: str):
        ext = os.path.splitext(file_path)[-1]  # get file extension
        if ext.lower() in PreviewHandler._valid_extensions:
            print(f'File {file_path} was handled by Preview app.')
        elif self._next is not None:
            self._next.open(file_path)
        else:
            print(f'File {file_path} was not handled.')


class PagesHandler(Handler):
    _valid_extensions = ['.doc', '.docx']

    def __init__(self):
        super(PagesHandler, self).__init__()

    def open(self, file_path: str):
        ext = os.path.splitext(file_path)[-1]  # get file extension
        if ext.lower() in PagesHandler._valid_extensions:
            print(f'File {file_path} was handled by Pages app.')
        elif self._next is not None:
            self._next.open(file_path)
        else:
            print(f'File {file_path} was not handled.')


class NumbersHandler(Handler):
    _valid_extensions = ['.xls', '.xlsx']

    def __init__(self):
        super(NumbersHandler, self).__init__()

    def open(self, file_path: str):
        ext = os.path.splitext(file_path)[-1]  # get file extension
        if ext.lower() in NumbersHandler._valid_extensions:
            print(f'File {file_path} was handled by Numbers app')
        elif self._next is not None:
            self._next.open(file_path)
        else:
            print(f'File {file_path} was not handled.')


class KeynoteHandler(Handler):
    _valid_extensions = ['.ppt', '.pptx']

    def __init__(self):
        super(KeynoteHandler, self).__init__()

    def open(self, file_path: str):
        ext = os.path.splitext(file_path)[-1]  # get file extension
        if ext.lower() in KeynoteHandler._valid_extensions:
            print(f'File {file_path} was handled by Keynote app')
        elif self._next is not None:
            self._next.open(file_path)
        else:
            print(f'File {file_path} was not handled.')
