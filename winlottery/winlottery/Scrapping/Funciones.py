#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

def generarMes(mesAbr):
    res = ""
    if mesAbr == "ene":
        res = "enero"
    elif mesAbr == "feb":
        res = "febrero"
    elif mesAbr== "mar":
        res = "marzo"
    elif mesAbr == "abr":
        res = "abril"
    elif mesAbr == "mayo":
        res = "mayo"
    elif mesAbr == "jun":
        res = "junio"
    elif mesAbr == "jul":
        res = "julio"
    elif mesAbr == "ago":
        res = "agosto"
    elif mesAbr == "sep":
        res = "septiembre"
    elif mesAbr == "oct":
        res = "octubre"
    elif mesAbr == "nov":
        res = "noviembre"
    elif mesAbr == "dic":
        res = "diciembre"

    return res

def procesarNumeros(numeros):
    return numeros.split("-")

def procesarFechaBonoloto(fecha):
    res = ""
    dia = ""
    aux = fecha.split(" ")
    if "es" in fecha:
        dia = aux[0].split("es")[1]
    elif "bado" in fecha:
        dia = aux[0].split("bado")[1]

    mes = generarMes(str(aux[1]))

    res = str(dia) + " de " + mes + " de " + str(aux[2])
    return res



def procesarFechaPrimitiva(fecha):
    res = ""
    dia = ""
    aux = fecha.split(" ")
    if "jueves" in fecha:
        dia = aux[0].split("jueves")[1]
    elif "bado" in fecha:
        dia = aux[0].split("bado")[1]

    mes = generarMes(str(aux[1]))

    res = str(dia) + " de " + mes + " de " + str(aux[2])
    return res

def procesarFechaGordo(fecha):
    res = ""
    aux = fecha.split(" ")
    dia = aux[0].split("domingo")[1]

    mes = generarMes(str(aux[1]))

    res = str(dia) + " de " + mes + " de " + str(aux[2])
    return res

def procesarFechaEuromillones(fecha):
    res = ""
    aux = fecha.split(" ")
    dia = aux[0].split("s")[1]

    mes = generarMes(str(aux[1]))

    res = str(dia) + " de " + mes + " de " + str(aux[2])
    return res

def crearListaNumeros(numeros, complementarios):
    res = []
    for n in numeros:
        for n2 in n:
            res.append(n2)
    for c in complementarios:
        res.append(c)
    return res

def crearDiccionarioBonolotoPrimitiva(numeros, complementarios):
    listaNumeros = crearListaNumeros(numeros, complementarios)
    res = {}
    for numero in listaNumeros:
        if numero not in res:
            res[numero] = 1
        else:
            res[numero] += 1

    return res

def crearDiccionarioGordo(numeros, reintegros):
    resNumeros = {}
    resReintegros = {}
    for numero in numeros:
        for n in numero:
            if n not in resNumeros:
                resNumeros[n] = 1
            else:
                resNumeros[n] += 1

    for reintegro in reintegros:
        if reintegro not in resReintegros:
            resReintegros[reintegro] = 1
        else:
            resReintegros[reintegro] += 1

    return resNumeros, resReintegros


def crearDiccionarioEuromillones(numeros, estrellas):
    resNumeros = {}
    resEstrellas = {}
    for numero in numeros:
        for n in numero:
            if n not in resNumeros:
                resNumeros[n] = 1
            else:
                resNumeros[n] += 1

    for estrella in estrellas:
        for es in estrella:
            if es not in resEstrellas:
                resEstrellas[es] = 1
            else:
                resEstrellas[es] += 1


    return resNumeros, resEstrellas

def obtenerNumerosGanadores(diccionario):
    res = []
    valores = diccionario.items()
    valores.sort(key=lambda x:x[1])
    valores.reverse()
    if len(diccionario.keys()) == 49:
        for i in range(0, 14):
            res.append(valores[i][0])
    else:
        for i in range(0, 10):
            res.append(valores[i][0])

    res.sort()

    return res

def obtenerReintegrosEstrellasGanadores(diccionario):
    res = []
    valores = diccionario.items()
    valores.sort(key=lambda x:x[1])
    valores.reverse()
    if len(diccionario.keys()) == 10:
        for i in range(0, 5):
            res.append(valores[i][0])
    else:
        for i in range(0, 6):
            res.append(valores[i][0])

    res.sort()

    return res

def recomendacionNumeros(numeros):
    recomendacion = []
    aux = []
    if len(numeros) == 14:
        while len(recomendacion) < 6:
            posicion = randint(0, 13)
            if posicion in aux:
                posicion = randint(0, 13)
            else:
                recomendacion.append(numeros[posicion])
                aux.append(posicion)
    elif len(numeros) == 10:
        while len(recomendacion) < 5:
            posicion = randint(0, 9)
            if posicion in aux:
                posicion = randint(0, 9)
            else:
                recomendacion.append(numeros[posicion])
                aux.append(posicion)

    recomendacion.sort()

    return recomendacion

def recomendacionReintegroEstrellas(numeros):
    recomendacion = []
    aux = []
    if len(numeros) == 5:
        posicion = randint(0, 4)
        recomendacion.append(numeros[posicion])
    elif len(numeros) == 6:
        while len(recomendacion) < 2:
            posicion = randint(0, 5)
            if posicion in aux:
                posicion = randint(0, 5)
            else:
                recomendacion.append(numeros[posicion])
                aux.append(posicion)

    recomendacion.sort()

    return recomendacion

def leerDatosBonolotoPrimitiva(ruta):
    fileobj = open(ruta, "r")
    fileobj.readline()
    numeros = fileobj.readline().strip()
    complementario = fileobj.readline().strip()
    fileobj.close()

    numerosRes = procesarNumeros(numeros)

    return numerosRes, complementario

def leerDatosGordo(ruta):
    fileobj = open(ruta, "r")
    fileobj.readline()
    numeros = fileobj.readline().strip()
    reintegro = fileobj.readline().strip()
    fileobj.close()

    numerosRes = procesarNumeros(numeros)

    return numerosRes, reintegro

def leerDatosEuromillones(ruta):
    fileobj = open(ruta, "r")
    fileobj.readline()
    numeros = fileobj.readline().strip()
    estrellas = fileobj.readline().strip()
    fileobj.close()

    numerosRes = procesarNumeros(numeros)
    estrellasRes = procesarNumeros(estrellas)

    return numerosRes, estrellasRes
