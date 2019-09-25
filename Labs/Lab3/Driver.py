from SmurfParade import SmurfParade


def main():
    smurfs = SmurfParade('Bob', 'Sam', 'Ken')

    # smurfs.append('Ken')

    # print(smurfs)

    # print(smurfs.__len__())

    # print(smurfs.__contains__('Bob'))

    # print(smurfs.__getitem__(0))

    # smurfs_iterator = smurfs.__iter__()
    # for i in smurfs_iterator:
    #     print(i)

    # print(smurfs.count('Bob'))

    # print(smurfs.index('Sam'))

    print(smurfs.__reversed__())


if __name__ == '__main__':
    main()
