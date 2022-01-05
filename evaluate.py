#!/home/tridimensional/u/dcc/octavo/rim/rim/bin/python3
import pickle
import dataset
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} file-name")
        sys.exit(1)

    with open("dataset.obj", 'rb') as f:
        data = pickle.load(f)

    file_name = sys.argv[1]
    try:
        with open(file_name, 'r') as f:
            ground_truth = f.readlines()
    except FileNotFoundError:
        print(f"El archivo {file_name} no existe")
        sys.exit(1)

    ground_truth = list(map(lambda x: x.split(sep=','), ground_truth))
    for i, lst in enumerate(ground_truth):
        large = len(lst) - 1
        lst[large] = lst[large].replace("\n", "")
        n = large - 1

        name = ground_truth[i][1]
        category = ground_truth[i][0]

        nns = data.get_nns_name(ground_truth[i][1], n)
        nns_gt = lst[2:len(lst)]

        text1 = f"Agrupando los vecinos más cercanos de {name} según"
        text2 = f"la categoría {category} (según el ground truth) se tiene:"
        print(text1)
        print(text2)

        count = 0
        for nn in nns_gt:
            print(f" - {nn}")
            nn = f"{nn} subs.srt"
            if nn in nns:
                count += 1

        text1 = f"Ahora, los vecinos más cercanos de {name}"
        text2 = "obtenidos según td-idf son los siguientes:"
        print(text1)
        print(text2)

        for nn in nns:
            print(f" - {nn}")

        recall = count/n
        print(f"Se obtuvo un recall de {recall}")
        print("")


if __name__ == "__main__":
    main()
