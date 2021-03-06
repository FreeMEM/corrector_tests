import pandas
# from pprint import pprint
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
    # {
    #     "items": [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
    #     "group": "totales",
    #     "puntuaciones": {
    #         "Muy en desacuerdo": 0,
    #         "En desacuerdo": 1,
    #         "Ligeramente en desacuerdo": 2,
    #         "Ligeramente de acuerdo": 3,
    #         "De acuerdo": 4,
    #         "Muy de acuerdo": 5,
    #     }
    # },
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
              "Grupo edad": [],
              "Género": [],
              "Peso": [],
              "Altura": [],
              "IMC": [],
              "Clasificación IMC": [],
              "Autoestima Rossemberg": [],
            #   "Valoración Rossemberg": [],
              "Alexitimia TAS-20": [],
              "Valoración Alexitimia TAS-20": [],
              "Alexitimia TAS-20 grupo A": [],
              "Alexitimia TAS-20 grupo B": [],
              "Alexitimia TAS-20 grupo C": [],
              "BSQ Cooper": [],
              "Valoración BSQ Cooper": []
              }


def parse_to_numeric(cadena):
    convertido = ""
    for n in cadena:
        if n.isdigit():
            convertido = convertido + n
        else:
            if n == "/":
                partes = cadena.split("/")
                total = ((float(partes[1]) - float(partes[0])) / 2) + float(partes[0])
                convertido = str(total)
                break
            if n == ",":
                convertido = convertido + n.replace(",", ".")
            if n == "'":
                convertido = convertido + n.replace("'", ".")
            if n == ".":
                convertido = convertido + n
    return convertido


for i in range((cuestionario.shape[0])):
    row = list(cuestionario.iloc[i, :])
    # resultados["Id"].append(row[0])
    # print(row[0])
    edad = int(parse_to_numeric(row[7]))
    if not edad or (18 > edad and edad > 55):
        continue
    resultados["Edad"].append(edad)
    if 18 <= edad and edad <= 30:
        resultados["Grupo edad"].append("18-30")
    if 31 <= edad and edad <= 43:
        resultados["Grupo edad"].append("31-43")
    if 44 <= edad and edad <= 55:
        resultados["Grupo edad"].append("44-55")
    # print("%s %s %s" % (row[0], edad, resultados["Grupo edad"].pop()))
    resultados["Género"].append(row[8])
    peso = float(parse_to_numeric(row[9]))
    # print("peso: %s %s" % (row[9],peso))
    raw_altura = parse_to_numeric(row[10])
    if raw_altura.find(".") != -1:
        num = float(raw_altura) * 100
        raw_altura = f'{num:.2f}'
    altura = float(raw_altura)
    # print("altura: %s %s " % (row[10],altura))
    resultados["Peso"].append(int(peso))
    resultados["Altura"].append(int(altura))
    imc = peso / (pow(altura / 100, 2))
    resultados["IMC"].append(f'{imc:.2f}')
    # clasificacion IMC
    if imc < 18.5:
        resultados["Clasificación IMC"].append("Bajo peso")
    if 18.5 <= imc and imc < 25:
        resultados["Clasificación IMC"].append("Normopeso")
    if 25 <= imc and imc < 30:
        resultados["Clasificación IMC"].append("Sobrepeso")
    if imc >= 30:
        resultados["Clasificación IMC"].append("Obesidad")
    # if 30 < imc and imc < 35:
    #     resultados["Clasificación IMC"].append("Obesidad tipo I")
    # if 35 < imc and imc < 40:
    #     resultados["Clasificación IMC"].append("Obesidad tipo II")
    # if 40 <= imc:
    #     resultados["Clasificación IMC"].append("Mórbida")

    # test Rossemberg
    score = 0
    for test in autoestima_rossemberg:
        for item in test["items"]:
            # pprint(row[item+4])
            score = score + test["puntuaciones"][row[item + 4].replace(".", "")]
        # print("%s %s" % (test["group"], score))
    resultados["Autoestima Rossemberg"].append(score)

    # valoración Rossemberg
    # if score < 25:
    #     resultados["Valoración Rossemberg"].append("Baja autoestima")
    # if 25 <= score and score <= 35:
    #     resultados["Valoración Rossemberg"].append("Valores normales")
    # if score > 35:
    #     resultados["Valoración Rossemberg"].append("Autoestima elevada")

    # test TAS-20 completo
    score = 0
    for test in alexitimia_tas20:
        for item in test["items"]:
            # print("%s %s" % (row[item+4], test["puntuaciones"][row[item+4].replace(".","")]))
            score = score + test["puntuaciones"][row[item + 4].replace(".", "")]
    resultados["Alexitimia TAS-20"].append(score)
    # valoración TAS-20 completo
    if score <= 51:
        resultados["Valoración Alexitimia TAS-20"].append("Ausencia de alexitimia")
    if 51 < score and score <= 60:
        resultados["Valoración Alexitimia TAS-20"].append("Posible alexitimia")
    if score > 60:
        resultados["Valoración Alexitimia TAS-20"].append("Alexitimia")

    # test TAS-20 grupo a
    score = 0
    for test in alexitimia_tas20:
        if test["group"] == "a" or test["group"] == "a_inversa":
            for item in test["items"]:
                # print("%s %s" % (row[item+4], test["puntuaciones"][row[item+4].replace(".","")]))
                score = score + test["puntuaciones"][row[item + 4].replace(".", "")]
    resultados["Alexitimia TAS-20 grupo A"].append(score)

    # test TAS-20 grupo b
    score = 0
    for test in alexitimia_tas20:
        if test["group"] == "b" or test["group"] == "b_inversa":
            for item in test["items"]:
                # print("%s %s" % (row[item+4], test["puntuaciones"][row[item+4].replace(".","")]))
                score = score + test["puntuaciones"][row[item + 4].replace(".", "")]
    resultados["Alexitimia TAS-20 grupo B"].append(score)

    # test TAS-20 grupo c
    score = 0
    for test in alexitimia_tas20:
        if test["group"] == "c" or test["group"] == "c_inversa":
            for item in test["items"]:
                # print("%s %s" % (row[item+4], test["puntuaciones"][row[item+4].replace(".","")]))
                score = score + test["puntuaciones"][row[item + 4].replace(".", "")]
    resultados["Alexitimia TAS-20 grupo C"].append(score)

    # test BSQ Cooper
    score = 0
    for test in bsq_cooper:
        for item in test["items"]:
            # print("%s %s" % (row[item+4], test["puntuaciones"][row[item+4].replace(".","")]))
            score = score + test["puntuaciones"][row[item + 4].replace(".", "")]
    resultados["BSQ Cooper"].append(score)

    # valoración BSQ
    if score >= 105:
        resultados["Valoración BSQ Cooper"].append("Patología")
    else:
        resultados["Valoración BSQ Cooper"].append("Ausencia patología")

# for key,value in resultados.items():
#     print(len(value))


df = pandas.DataFrame(resultados)

df.to_csv("resultados.csv", mode = 'w', index=False)
