from handler import PreviewHandler, PagesHandler, NumbersHandler, KeynoteHandler


def get_handler():
    preview = PreviewHandler()
    pages = PagesHandler()
    numbers = NumbersHandler()
    keynote = KeynoteHandler()

    preview.set_next(pages)
    pages.set_next(numbers)
    numbers.set_next(keynote)

    return preview


def main():
    handler = get_handler()

    files = [
        "image.jpg",
        "image.png",
        "document.docx",
        "document.doc",
        "table.xls",
        "table.xlsx",
        "presentation.pptx",
        "document.pdf",
    ]
    for file in files:
        handler.open(file)


if __name__ == '__main__':
    main()
    # File image.jpg was handled by Preview app.
    # File image.png was handled by Preview app.
    # File document.docx was handled by Pages app.
    # File document.doc was handled by Pages app.
    # File table.xls was handled by Numbers app
    # File table.xlsx was handled by Numbers app
    # File presentation.pptx was handled by Keynote app
    # File document.pdf was handled by Preview app.
