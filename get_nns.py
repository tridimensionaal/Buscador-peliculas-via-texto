#!/home/tridimensional/u/dcc/octavo/rim/rim/bin/python3
import pickle
import dataset
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} number-nns")
        sys.exit(1)

    with open("dataset.obj", 'rb') as f:
        data = pickle.load(f)

    n = int(sys.argv[1])
    for i in range(len(data.data)):
        data.get_nns_i(i, n)


if __name__ == "__main__":
    main()
