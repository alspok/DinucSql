import imp
from ntpath import join
from Classes.InitVars import InitVars as iv
from Classes.GetColumn import GetColumn
from Classes.StringToFloat import StringToFloat
from Classes.MatPlot import MatPlot
import sqlalchemy as db
from pathlib import Path

def dinucSql() -> None:
    # di_diff, mono_shuffle, di_shuffle, tri_shuffle = gc().getColumn()
    # subPlots(di_diff, mono_shuffle, di_shuffle, tri_shuffle)
    # pass

    di_dict = GetColumn().getColumn()
    MatPlot().dictPlot(di_dict)
    pass


if __name__ == "__main__":
    dinucSql()