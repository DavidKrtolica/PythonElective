import sys

def main(name):

    if name == 'Alice' or name == 'Jens':
        print('Hello ' + name)
    else:
        print('You are not a real human!')

main(sys.argv[1])