from SmurfParade import SmurfParade


def main():
    # create list
    smurfs = SmurfParade('Bob', 'Sam')

    smurfs.append('Ken')

    print(smurfs)

    print(smurfs.__len__())

    # print(smurfs.__contains__('Bob'))

    # print(smurfs.__getitem__(0))

    # smurfs_iterator = smurfs.__iter__()
    # for i in smurfs_iterator:
    #     print(i)


if __name__ == '__main__':
    main()
