# %%
from typing import runtime_checkable
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# %%
ruta_base_DCL = "/home/jesusmendoza/Clasificadores/Recortes_aleatorios/DCL/"
ruta_base_Control = "/home/jesusmendoza/Clasificadores/Recortes_aleatorios/Control/"

# %%
nombresDCL = ["AEF", "CLM", "FGV", "JGM", "LIV", "PCM", "RLM", "RRM"]
nombresControl = ["EMV", "GH2", "GUR", "JAL", "JAN", "MGN", "MJN", "MMA", "RAN", "VCN"]
nodos = [
    "C3",
    "C4",
    "CZ",
    "F3",
    "F4",
    "F7",
    "F8",
    "FP1",
    "FP2",
    "FZ",
    "LOG",
    "O1",
    "O2",
    "P3",
    "P4",
    "PZ",
    "ROG",
    "T3",
    "T4",
    "T5",
    "T6",
]
minutos = [i for i in range(1, 51)]


# %%
class Persona:
    def __init__(self, ruta_base, nombre, nodos, status):
        """
        Create an array with the people and all their files and signals
        Args:
            ruta_base: the directory where are your subjects
        """
        # self.ruta = f\"{ruta_base}{nombre}/{nodo}/recorte_{minuto}.txt\"\n",
        # self.data = pd.read_table(self.ruta, header = None)\n",
        self.ruta_base = ruta_base
        self.data = {}
        self.nombre = nombre
        self.nodos = nodos
        self.recortes = [str(i) for i in range(1, 51)]
        self.status = status
        # self.archivos = {}\n",

    def read_file(self, archivo):
        return pd.read_table(archivo, header=None)

    def all_files(self):
        for nodo in self.nodos:
            self.data[nodo] = {}
            for recorte in self.recortes:
                ruta = f"{self.ruta_base}{self.nombre}/{nodo}/recorte_{recorte}.txt"
                self.data[nodo][recorte] = self.read_file(ruta)
        return self.data

    def data_frame(self, nodo, recorte):
        return self.data[nodo][recorte]
        # En estatus 0 si no tiene DCL y 1 si lo tiene\n",


# %%
personasDCL = []
for nombre in nombresDCL:
    personasDCL.append(Persona(ruta_base_DCL, nombre, nodos, 1))

for persona in personasDCL:
    persona.all_files()

# %%
personasControl = []
for nombre in nombresControl:
    personasControl.append(Persona(ruta_base_Control, nombre, nodos, 0))

for persona in personasControl:
    persona.all_files()

# %%
# Block de pruebas
personasDCL[7].data_frame("O2", "30")
personasControl[7].data_frame("O2", "30")
