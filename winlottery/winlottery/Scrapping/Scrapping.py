#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import Funciones

def obtenerResultadosBonoloto():
    urlBonoloto = urllib2.urlopen("https://www.loterias.com/bonoloto/resultados/2017").read()

    fechas = []
    numeros = []
    complementarios = []

    auxNumero = []

    sopaBonoloto = BeautifulSoup(urlBonoloto, "html.parser")
    elementosBonoloto = sopaBonoloto.find_all("table", {"class": "archives"})

    for elemento in elementosBonoloto:
        fechaSopa = elemento.find_all("a", {"class": "smallerHeading"})
        numerosSopa = elemento.find_all("li", {"class": "ball"})
        complementariosSopa = elemento.find_all("li", {"class": "bonus-ball bonus"})
        for fecha in fechaSopa:
            fechas.append(Funciones.procesarFechaBonoloto(fecha.text).strip())
        for numero in numerosSopa:
            auxNumero.append(numero.text)
        for complementario in complementariosSopa:
            complementarios.append(complementario.text)

        for i in range(0, len(auxNumero), 6):
            aux = auxNumero[i:(i + 6)]
            numeros.append(aux)

    fechas.reverse()
    numeros.reverse()
    complementarios.reverse()

    return fechas, numeros, complementarios

def obtenerResultadosPrimitiva():
    urlPrimitiva = urllib2.urlopen("https://www.loterias.com/la-primitiva/resultados/2017").read()

    fechas = []
    numeros = []
    complementarios = []

    auxNumero = []

    sopaPrimitiva = BeautifulSoup(urlPrimitiva, "html.parser")
    elementosPrimitiva = sopaPrimitiva.find_all("table", {"class": "archives"})

    for elemento in elementosPrimitiva:
        fechaSopa = elemento.find_all("a", {"class": "smallerHeading"})
        numerosSopa = elemento.find_all("li", {"class": "ball"})
        complementariosSopa = elemento.find_all("li", {"class": "bonus-ball bonus"})
        for fecha in fechaSopa:
            fechas.append(Funciones.procesarFechaPrimitiva(fecha.text).strip())
        for numero in numerosSopa:
            auxNumero.append(numero.text)
        for complementario in complementariosSopa:
            complementarios.append(complementario.text)

        for i in range(0, len(auxNumero), 6):
            aux = auxNumero[i:(i + 6)]
            numeros.append(aux)

    fechas.reverse()
    numeros.reverse()
    complementarios.reverse()

    return fechas, numeros, complementarios

def obtenerResultadosGordo():
    urlGordo = urllib2.urlopen("https://www.loterias.com/el-gordo-de-la-primitiva/resultados/2017").read()

    fechas = []
    numeros = []
    reintegros = []

    auxNumero = []

    sopaGordo = BeautifulSoup(urlGordo, "html.parser")
    elementosGordo = sopaGordo.find_all("table", {"class": "archives"})

    for elemento in elementosGordo:
        fechaSopa = elemento.find_all("a", {"class": "smallerHeading"})
        numerosSopa = elemento.find_all("li", {"class": "ball"})
        reintegrosSopa = elemento.find_all("li", {"class": "bonus-ball bonus"})
        for fecha in fechaSopa:
            fechas.append(Funciones.procesarFechaGordo(fecha.text).strip())
        for numero in numerosSopa:
            auxNumero.append(numero.text)
        for reintegro in reintegrosSopa:
            reintegros.append(reintegro.text)

        for i in range(0, len(auxNumero), 5):
            aux = auxNumero[i:(i + 5)]
            numeros.append(aux)

    fechas.reverse()
    numeros.reverse()
    reintegros.reverse()

    return fechas, numeros, reintegros

def obtenerResultadosEuromillones():
    urlEuromillones = urllib2.urlopen("https://www.loterias.com/euromillones/resultados/2017").read()

    fechas = []
    numeros = []
    estrellas = []

    auxNumero = []
    auxEstrella = []

    sopaEuromillones = BeautifulSoup(urlEuromillones, "html.parser")
    elementosEuromillones = sopaEuromillones.find_all("table", {"class": "archives"})

    for elemento in elementosEuromillones:
        fechaSopa = elemento.find_all("a", {"class": "smallerHeading"})
        numerosSopa = elemento.find_all("li", {"class": "ball"})
        estrellasSopa = elemento.find_all("li", {"class": "lucky-star bonus"})
        for fecha in fechaSopa:
            fechas.append(Funciones.procesarFechaEuromillones(fecha.text).strip())
        for numero in numerosSopa:
            auxNumero.append(numero.text)
        for estrella in estrellasSopa:
            auxEstrella.append(estrella.text)

    for i in range(0, len(auxNumero), 5):
        aux = auxNumero[i:(i + 5)]
        numeros.append(aux)

    for i in range(0, len(auxEstrella), 2):
        aux = auxEstrella[i:(i + 2)]
        estrellas.append(aux)

    fechas.reverse()
    numeros.reverse()
    estrellas.reverse()

    return fechas, numeros, estrellas