import imp
from ntpath import join
from Classes.InitVars import InitVars as iv
from Classes.GetColumn import GetColumn as gc
from Classes.StringToFloat import StringToFloat
from MatPlot import simplePlot, multiFigurePlot, subPlots
import sqlalchemy as db
from pathlib import Path

def dinucSql() -> None:
    di_diff, mono_shuffle, di_shuffle, tri_shuffle = gc().getColumn()
    # di_diff_float = [float(di) for di in di_diff]
    # di_shuffle_diff = StringToFloat().stringToFloat(di_shuffle_diff)

    # simplePlot(di_diff)
    #multiFigurePlot(di_diff, mono_shuffle, di_shuffle, tri_shuffle)
    subPlots(di_diff, mono_shuffle, di_shuffle, tri_shuffle)
    pass


if __name__ == "__main__":
    dinucSql()