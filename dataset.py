#!/home/tridimensional/u/dcc/octavo/rim/rim/bin/python3
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class File:
    def __init__(self, filename: str, dir_dataset="datos/peliculas"):
        self.name = filename
        self.load_full_text(dir_dataset)

    def load_full_text(self, dir_data):
        with open(f"{dir_data}/{self.name}", 'r') as f:
            self.full_text = f.read()


class Dataset:
    def __init__(self, dir_dataset: str):
        self.dir_dataset = dir_dataset
        self.data_dic = {}
        # print("Loading files ...")
        self.load_dataset()
        # print("Calculating descriptors ...")
        self.calculate_vectorizer()
        self.calculate_descriptors()
        self.calculate_distances()

    def load_dataset(self):
        files = os.listdir(self.dir_dataset)  # dir_dataset = "datos/peliculas"
        self.data = list(map(lambda x: File(x, self.dir_dataset), files))
        list(map(
            lambda x: self.data_dic.update({x[1].name: x[0]}),
            list(enumerate(self.data))
            ))

    def calculate_vectorizer(self):
        self.vectorizer = TfidfVectorizer(
                lowercase=True,  # por defecto es True
                strip_accents='unicode',  # por defecto es None
                sublinear_tf=True,  # por defecto es False. usar 1+log(freq)
                use_idf=True,  # por defecto es True
                norm='l2',  # por defecto es True
                ngram_range=(1, 1),  # por defecto es (1,1). rango de ngramas
                max_df=1.0,
                min_df=1
                # Si una palabra aparece en menos que min_df documentos,
                # se ignora
                )
        self.vectorizer.fit(list(map(lambda x: x.full_text, self.data)))

    def calculate_descriptors(self):
        self.descriptors = self.vectorizer.transform(
                list(map(lambda x: x.full_text, self.data))
                )

    def calculate_distances(self):
        descriptors_dense = self.descriptors.toarray()
        self.distances = np.matmul(descriptors_dense, descriptors_dense.T)
        np.fill_diagonal(self.distances, 0)

    def get_nns_i(self, i, n):
        nns = list(enumerate(self.distances[i]))
        nns.sort(reverse=True, key=lambda x: x[1])

        print(f"Los {n} vecinos más cercanos de {self.data[i].name} son:")

        for j in range(n):
            nn_name = self.data[nns[j][0]].name
            nn_distance = nns[j][1]
            print(f" {j+1} - {nn_name} {nn_distance}")
        print("")

    def get_nns_name(self, name, n):
        try:
            i = self.data_dic[f"{name} subs.srt"]
        except KeyError:
            return []

        nns = list(enumerate(self.distances[i]))
        nns.sort(reverse=True, key=lambda x: x[1])
        nns = nns[0:n]
        nns = list(map(lambda x: self.data[x[0]].name, nns))
        return nns
