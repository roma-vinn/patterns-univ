from display import ImageProxy


class ImageGallery:
    def __init__(self):
        self._images = [
            ImageProxy('resources/image1.jpeg'),
            ImageProxy('resources/image2.jpeg'),
            ImageProxy('resources/image3.jpeg'),
            ImageProxy('resources/image4.jpeg'),
            ImageProxy('resources/image5.jpeg'),
            ImageProxy('resources/image6.jpeg'),
            ImageProxy('resources/image7.jpeg'),
            ImageProxy('resources/image8.jpeg'),
            ImageProxy('resources/image9.jpeg'),
            ImageProxy('resources/image10.jpeg'),
        ]

    def show(self):
        for image in self._images:
            image.display()
