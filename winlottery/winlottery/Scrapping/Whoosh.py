#!/usr/bin/python
# -*- coding: utf-8 -*-

import Scrapping
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, NUMERIC
from whoosh.qparser import QueryParser
import os

def getSchemaBonolotoPrimitiva():
    return Schema(fecha=TEXT(stored=True), numeros=TEXT(stored=True), complementario=NUMERIC(stored=True))

def getSchemaGordo():
    return Schema(fecha=TEXT(stored=True), numeros=TEXT(stored=True), reintegro=NUMERIC(stored=True))

def getSchemaEuromillones():
    return Schema(fecha=TEXT(stored=True), numeros=TEXT(stored=True), estrellas=TEXT(stored=True))

def indiceFicheroBonolotoPrimitiva(writer, enlace, nombreDoc):
    fileobj = open(enlace + '\\' + nombreDoc, "rb")
    f = unicode(fileobj.readline().strip())
    n = unicode(fileobj.readline().strip())
    c = unicode(fileobj.readline().strip())
    fileobj.close()

    writer.add_document(fecha=f, numeros=n, complementario=c)

def indiceFicheroGordo(writer, enlace, nombreDoc):
    fileobj = open(enlace + '\\' + nombreDoc, "rb")
    f = unicode(fileobj.readline().strip())
    n = unicode(fileobj.readline().strip())
    r = unicode(fileobj.readline().strip())
    fileobj.close()

    writer.add_document(fecha=f, numeros=n, reintegro=r)

def indiceFicheroEuromillones(writer, enlace, nombreDoc):
    fileobj = open(enlace + '\\' + nombreDoc, "rb")
    f = unicode(fileobj.readline().strip())
    n = unicode(fileobj.readline().strip())
    e = unicode(fileobj.readline().strip())
    fileobj.close()

    writer.add_document(fecha=f, numeros=n, estrellas=e)


def crearFicherosBonoloto():
    if not os.path.exists("Resultados/Bonoloto"):
        os.mkdir("Resultados/Bonoloto")
        fechas, numeros, complementarios = Scrapping.obtenerResultadosBonoloto()
        for i in range(0, 312):
            f = open("Resultados/Bonoloto/Bonoloto" + str(i) + ".txt", "w")
            f.write(fechas[i].encode('ascii', 'ignore') + "\n")
            for e in range(0, 6):
                if e is not 5:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "-")
                else:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "\n")

            f.write(complementarios[i].encode('ascii', 'ignore'))

        if not os.path.exists("Indices/Bonoloto"):
            os.mkdir("Indices/Bonoloto")

        ix = create_in("Indices/Bonoloto", schema=getSchemaBonolotoPrimitiva())
        writer = ix.writer()

        for docname in os.listdir("Resultados/Bonoloto"):
            if not os.path.isdir("Resultados/Bonoloto/" + docname):
                indiceFicheroBonolotoPrimitiva(writer, "Resultados/Bonoloto/", docname)

        writer.commit()

def crearFicherosPrimitiva():
    if not os.path.exists("Resultados/Primitiva"):
        os.mkdir("Resultados/Primitiva")
        fechas, numeros, complementarios = Scrapping.obtenerResultadosPrimitiva()
        for i in range(0, 104):
            f = open("Resultados/Primitiva/Primitiva" + str(i) + ".txt", "w")
            f.write(fechas[i].encode('ascii', 'ignore') + "\n")
            for e in range(0, 6):
                if e is not 5:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "-")
                else:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "\n")

            f.write(complementarios[i].encode('ascii', 'ignore'))

        if not os.path.exists("Indices/Primitiva"):
            os.mkdir("Indices/Primitiva")

        ix = create_in("Indices/Primitiva", schema=getSchemaBonolotoPrimitiva())
        writer = ix.writer()

        for docname in os.listdir("Resultados/Primitiva"):
            if not os.path.isdir("Resultados/Primitiva/" + docname):
                indiceFicheroBonolotoPrimitiva(writer, "Resultados/Primitiva/", docname)

        writer.commit()


def crearFicherosGordo():
    if not os.path.exists("Resultados/Gordo"):
        os.mkdir("Resultados/Gordo")
        fechas, numeros, reintegros = Scrapping.obtenerResultadosGordo()
        for i in range(0, 53):
            f = open("Resultados/Gordo/Gordo" + str(i) + ".txt", "w")
            f.write(fechas[i].encode('ascii', 'ignore') + "\n")
            for e in range(0, 5):
                if e is not 4:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "-")
                else:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "\n")

            f.write(reintegros[i].encode('ascii', 'ignore'))

    if not os.path.exists("Indices/Gordo"):
        os.mkdir("Indices/Gordo")

    ix = create_in("Indices/Gordo", schema=getSchemaGordo())
    writer = ix.writer()

    for docname in os.listdir("Resultados/Gordo"):
        if not os.path.isdir("Resultados/Gordo/" + docname):
            indiceFicheroGordo(writer, "Resultados/Gordo/", docname)

    writer.commit()

def crearFicherosEuromillones():
    if not os.path.exists("Resultados/Euromillones"):
        os.mkdir("Resultados/Euromillones")
        fechas, numeros, estrellas = Scrapping.obtenerResultadosEuromillones()
        for i in range(0, 104):
            f = open("Resultados/Euromillones/Euromillones" + str(i) + ".txt", "w")
            f.write(fechas[i].encode('ascii', 'ignore') + "\n")
            for e in range(0, 5):
                if e is not 4:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "-")
                else:
                    f.write(numeros[i][e].encode('ascii', 'ignore') + "\n")

            for es in range(0, 2):
                if es is not 1:
                    f.write(estrellas[i][es].encode('ascii', 'ignore') + "-")
                else:
                    f.write(estrellas[i][es].encode('ascii', 'ignore'))

    if not os.path.exists("Indices/Euromillones"):
        os.mkdir("Indices/Euromillones")

    ix = create_in("Indices/Euromillones", schema=getSchemaEuromillones())
    writer = ix.writer()

    for docname in os.listdir("Resultados/Euromillones"):
        if not os.path.isdir("Resultados/Euromillones/" + docname):
            indiceFicheroEuromillones(writer, "Resultados/Euromillones/", docname)

    writer.commit()



# def buscarNumerosBonoloto(numero):
#     ix = open_dir("Indice/Bonoloto")
#     with ix.searcher() as searcher:
#         query = QueryParser("numeros", ix.schema).parse(unicode(en.get()))
#         results = searcher.search(query)
#         for r in results:
#             lb.insert(END, r['destinatarios'])
#             lb.insert(END, r['asunto'])
#             lb.insert(END, '')