from library import Library, Catalogue


def main():
    """
    Runs the program
    """
    flag = True
    catalogue = Catalogue()
    library = Library(catalogue)
    while flag:
        library.run()


if __name__ == '__main__':
    main()
