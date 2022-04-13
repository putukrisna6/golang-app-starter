import argparse
import os

from dbus import Interface

hasInterface = {'service', 'controller', 'repository'}
structExport = {'entity'}

def makeDirIfNotExist(path):
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)

def decision(kind, name):
    # Prepare
    makeDirIfNotExist(kind)
    filename = name + '-' + kind + '.go'
    f = open(kind + '/' + filename, 'w')

    # Package
    content = 'package ' + kind + '\n\n'

    # Struct
    struct = 'type ' + (name.capitalize() if (kind in structExport) else name)
    struct += kind.capitalize() if (kind in hasInterface) else ''
    struct += ' struct {\n\n}\n\n'
    content += struct

    # Interface
    if kind in hasInterface:
        fullname = name.capitalize() + kind.capitalize()

        interf = 'type ' + fullname + ' interface {\n\n}\n\n'
        content += interf

        # Bind Interface with Struct
        bind = 'func New' +  fullname + '() ' + fullname + ' {\n\treturn &' + name + kind.capitalize() + '{}\n}\n'
        content += bind

    f.write(content)
    f.close()

if __name__ == '__main__':
    choices = {'entity', 'service', 'controller', 'repository'}
    parser = argparse.ArgumentParser(description='create some .go files')
    parser.add_argument('name', help='name of the file')
    parser.add_argument('-t', metavar='TYPE', choices=choices, help='which file to create')
    parser.add_argument('-a', metavar='ALL', type=bool, default=False, help='create all file type')


    args = parser.parse_args()

    if args.a:
        for c in choices:
            decision(c, args.name)
        exit(0)
    elif not args.t:
        print("Please specify which file type you want to create")
        exit(1)

    decision(args.t, args.name)