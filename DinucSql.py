import imp
from ntpath import join
from Classes.InitVars import InitVars as iv
from Classes.GetColumn import GetColumn as gc
from Classes.StringToFloat import StringToFloat
from MatPlot import matPlot
import sqlalchemy as db
from pathlib import Path

def dinucSql() -> None:
    di_diff, di_shuffle_diff = gc().getColumn()
    # di_diff_float = [float(di) for di in di_diff]
    di_diff_float = StringToFloat().stringToFloat(di_diff)
    di_shuffle_diff_float = StringToFloat().stringToFloat(di_shuffle_diff)
    
    matPlot(di_diff_float)
        
    pass




if __name__ == "__main__":
    dinucSql()