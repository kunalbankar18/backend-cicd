def get_data():

    with open('info.txt') as f:
        names=f.read()

        names=names.split()

        return names