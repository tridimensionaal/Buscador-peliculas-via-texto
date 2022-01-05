#!/home/tridimensional/u/dcc/octavo/rim/rim/bin/python3
import dataset
import pickle


def main():
    data = dataset.Dataset("datos/peliculas")

    with open("dataset.obj", 'wb') as f:
        pickle.dump(data, f)


if __name__ == "__main__":
    main()
