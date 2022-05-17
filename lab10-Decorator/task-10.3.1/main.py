from decorators import (PrintableString, PostEndlDecorator, PostWordDecorator,
                        PostExclaimDecorator, PreWordDecorator, PostComaDecorator)


def main():
    word = PrintableString('')
    word = PreWordDecorator(word, 'Hello')
    word = PostComaDecorator(word)
    word = PostWordDecorator(word, ' World')
    word = PostExclaimDecorator(word)
    word = PostEndlDecorator(word)

    word.show()


if __name__ == '__main__':
    main()
    # Hello, World!
    #
