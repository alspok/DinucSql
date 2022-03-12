import imp
from ntpath import join
from Classes.InitVars import InitVars as iv
from Classes.GetColumn import GetColumn as gc
from Classes.StringToFloat import StringToFloat
from MatPlot import simplePlot, multiFigurePlot, subPlots
import sqlalchemy as db
from pathlib import Path

def dinucSql() -> None:
    """
    di_diff, mono_shuffle, di_shuffle, tri_shuffle = gc().getColumn()
    subPlots(di_diff, mono_shuffle, di_shuffle, tri_shuffle)
    pass
    """
    di_row = gc().getDinucColumn()

if __name__ == "__main__":
    dinucSql()