from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class DisplayObject(ABC):
    @abstractmethod
    def display(self):
        pass


class ImageFile(DisplayObject):
    def __init__(self, path: str):
        self._img = None
        try:
            self._img = plt.imread(path)  # read img into memory
        except FileNotFoundError:
            print(f'File {path} is not found.')

    def display(self):
        if self._img is not None:
            plt.imshow(self._img)
            plt.show()


class ImageProxy(DisplayObject):
    def __init__(self, path: str):
        self._img_path = path
        self._img_file = None

    def display(self):
        if self._img_file is None:
            self._img_file = ImageFile(self._img_path)  # load img only when display() is called
        self._img_file.display()
