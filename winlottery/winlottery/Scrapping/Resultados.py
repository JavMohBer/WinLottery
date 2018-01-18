#!/usr/bin/python
# -*- coding: utf-8 -*-

from Scrapping import Funciones
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def mostrarBonoloto():
    res = []
    auxNumeros = []
    auxComplementarios = []
    for i in range(0, 312):
        auxNumeros.append(Funciones.leerDatosBonolotoPrimitiva(BASE_DIR+"\Resultados\Bonoloto\Bonoloto" + str(i) + ".txt")[0])
        auxComplementarios.append(Funciones.leerDatosBonolotoPrimitiva(BASE_DIR+"\Resultados/Bonoloto/Bonoloto" + str(i) + ".txt")[1])

    diccionario = Funciones.crearDiccionarioBonolotoPrimitiva(auxNumeros, auxComplementarios)
    numeros = Funciones.obtenerNumerosGanadores(diccionario)
    aux = Funciones.recomendacionNumeros(numeros)
    for r in aux:
        res.append(int(r))
    res.sort()
    return res

def mostrarPrimitiva():
    res = []
    auxNumeros = []
    auxComplementarios = []
    for i in range(0, 104):
        auxNumeros.append(Funciones.leerDatosBonolotoPrimitiva("Resultados/Primitiva/Primitiva" + str(i) + ".txt")[0])
        auxComplementarios.append(Funciones.leerDatosBonolotoPrimitiva("Resultados/Primitiva/Primitiva" + str(i) + ".txt")[1])

    diccionario = Funciones.crearDiccionarioBonolotoPrimitiva(auxNumeros, auxComplementarios)
    numeros = Funciones.obtenerNumerosGanadores(diccionario)
    aux = Funciones.recomendacionNumeros(numeros)
    for r in aux:
        res.append(int(r))
    res.sort()
    return res

def mostrarGordo():
    numerosRes = []
    auxNumeros = []
    auxReintegros = []
    for i in range(0, 53):
        auxNumeros.append(Funciones.leerDatosGordo("Resultados/Gordo/Gordo" + str(i) + ".txt")[0])
        auxReintegros.append(Funciones.leerDatosGordo("Resultados/Gordo/Gordo" + str(i) + ".txt")[1])

    diccionario = Funciones.crearDiccionarioGordo(auxNumeros, auxReintegros)
    numeros = Funciones.obtenerNumerosGanadores(diccionario[0])
    reintegros = Funciones.obtenerReintegrosEstrellasGanadores(diccionario[1])
    aux = Funciones.recomendacionNumeros(numeros)
    reintegroRes = Funciones.recomendacionReintegroEstrellas(reintegros)
    for r in aux:
        numerosRes.append(int(r))
    numerosRes.sort()
    return numerosRes, reintegroRes

def mostrarEuromillones():
    numerosRes = []
    estrellasRes = []
    auxNumeros = []
    auxEstrellas = []
    for i in range(0, 104):
        auxNumeros.append(Funciones.leerDatosEuromillones("Resultados/Euromillones/Euromillones" + str(i) + ".txt")[0])
        auxEstrellas.append(Funciones.leerDatosEuromillones("Resultados/Euromillones/Euromillones" + str(i) + ".txt")[1])

    diccionario = Funciones.crearDiccionarioEuromillones(auxNumeros, auxEstrellas)
    numeros = Funciones.obtenerNumerosGanadores(diccionario[0])
    estrellas = Funciones.obtenerReintegrosEstrellasGanadores(diccionario[1])
    aux = Funciones.recomendacionNumeros(numeros)
    aux2 = Funciones.recomendacionReintegroEstrellas(estrellas)
    for r in aux:
        numerosRes.append(int(r))
    for r2 in aux2:
        estrellasRes.append(int(r2))
    numerosRes.sort()
    estrellasRes.sort()
    return numerosRes, estrellasRes