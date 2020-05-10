import pandas
from pprint import pprint
# datos y puntuaciones
autoestima_rossemberg = [
    {
        "items": [7, 8, 10, 12, 13],
        "group": "directos",
        "puntuaciones": {
            "Estoy muy de acuerdo": 4,
            "Estoy de acuerdo": 3,
            "No estoy de acuerdo": 2,
            "Estoy muy en desacuerdo": 1
        }
    },
    {
        "items": [9, 11, 14, 15, 16],
        "group": "indirectos",
        "puntuaciones": {
            "Estoy muy de acuerdo": 1,
            "Estoy de acuerdo": 2,
            "No estoy de acuerdo": 3,
            "Estoy muy en desacuerdo": 4
        }
    }
]


alexitimia_tas20 = [
    {
        "items": [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
        "group": "totales",
        "puntuaciones": {
            "Muy en desacuerdo": 0,
            "En desacuerdo": 1,
            "Ligeramente en desacuerdo": 2,
            "Ligeramente de acuerdo": 3,
            "De acuerdo": 4,
            "Muy de acuerdo": 5,
        }
    },
    {
        "items": [17, 19, 22, 23, 25, 29, 30],
        "group": "a",
        "puntuaciones": {
            "Muy en desacuerdo": 0,
            "En desacuerdo": 1,
            "Ligeramente en desacuerdo": 2,
            "Ligeramente de acuerdo": 3,
            "De acuerdo": 4,
            "Muy de acuerdo": 5,
        }
    },
    {
        "items": [],
        "group": "a_inversa",
        "puntuaciones": {
            "Muy en desacuerdo": 5,
            "En desacuerdo": 4,
            "Ligeramente en desacuerdo": 3,
            "Ligeramente de acuerdo": 2,
            "De acuerdo": 1,
            "Muy de acuerdo": 0,
        }
    },
    {
        "items": [18, 27, 28, 33],
        "group": "b",
        "puntuaciones": {
            "Muy en desacuerdo": 0,
            "En desacuerdo": 1,
            "Ligeramente en desacuerdo": 2,
            "Ligeramente de acuerdo": 3,
            "De acuerdo": 4,
            "Muy de acuerdo": 5,
        }
    },
    {
        "items": [20],
        "group": "b_inversa",
        "puntuaciones": {
            "Muy en desacuerdo": 5,
            "En desacuerdo": 4,
            "Ligeramente en desacuerdo": 3,
            "Ligeramente de acuerdo": 2,
            "De acuerdo": 1,
            "Muy de acuerdo": 0,
        }
    },
    {
        "items": [24, 31, 32, 36],
        "group": "c",
        "puntuaciones": {
            "Muy en desacuerdo": 0,
            "En desacuerdo": 1,
            "Ligeramente en desacuerdo": 2,
            "Ligeramente de acuerdo": 3,
            "De acuerdo": 4,
            "Muy de acuerdo": 5,
        }
    },
    {
        "items": [21, 26, 34, 35],
        "group": "c_inversa",
        "puntuaciones": {
            "Muy en desacuerdo": 5,
            "En desacuerdo": 4,
            "Ligeramente en desacuerdo": 3,
            "Ligeramente de acuerdo": 2,
            "De acuerdo": 1,
            "Muy de acuerdo": 0,
        }
    },
]

bsq_cooper = [
    {
        "items": [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
        "group": "c",
        "puntuaciones": {
            "Nunca": 1,
            "Raramente": 2,
            "Alguna vez": 3,
            "A menudo": 4,
            "Muy a menudo": 5,
            "Siempre": 6,
        }
    },
]

# carga file
cuestionario = pandas.read_csv('../cuestionario.csv')

resultados = {"Edad": [],
              "Género": [],
              "Peso": [],
              "Altura": [],
              "Autoestima Rossemberg": [],
              "Alexitimia TAS-20", [],
              "BSQ Cooper": []
              }


for i in range((cuestionario.shape[0])):      
    row = list(cuestionario.iloc[i, :])

    # test rossemberg
    for test in autoestima_rossemberg:
      resultado=0
      for item in test["items"]:
        # pprint(row[item+4])
        resultado = resultado + test["puntuaciones"][row[item+4].replace(".","")]
      print("%s %s" % (test["group"], resultado))
    break
    # break
    # row_list.append(list(cuestionario.iloc[i, :])) 

