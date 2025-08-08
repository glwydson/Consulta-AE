#!bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('C:/Users/glaydson.araujo/OneDrive - AEGEA Saneamento e Participações S.A/Compartilhados/Consulta-AE')

def bibliotecas():
    import pandas as pd
    import polars as pl
    import pathlib as Path
    import os
    import time
    import sys

    return pd, pl, Path, os, time, sys

pd, pl, Path, os, time, sys = bibliotecas()


def var():
    usuario = os.getlogin()  # Obtém o nome do usuário atual
    dir_1 = fr"C:\Users\{usuario}\OneDrive - AEGEA Saneamento e Participações S.A\Compartilhados\Base\Consulta Cliente.xlsx"  # Caminho do arquivo Excel
    data_save = fr"C:\Users\{usuario}\OneDrive - AEGEA Saneamento e Participações S.A\Compartilhados\Consulta-AE\Data\dados.csv"

    return dir_1, data_save
