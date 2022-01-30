from Classes.InitVars import InitVars as iv
import sqlalchemy as sq
from sqlalchemy import or_, and_

class GetColumn():
    def __init__(self) -> None:
        self.db = iv.db_file
        self.tbl = iv.db_table
        pass
    
    def getColumn(self) -> list:
        engine = sq.create_engine("sqlite:///" + self.db)
        meta_data = sq.MetaData(bind=engine)
        sq.MetaData.reflect(meta_data)
        Dinuctbl = meta_data.tables[self.tbl]
        
        # query = db.select(Dinuctbl).filter(Dinuctbl.c.id.in_(100, 120))
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.id.between(15,51))
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.notlike('%mito%'))
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.like('%plasm%'))
        # query = sq.select(Dinuctbl).filter((Dinuctbl.c.description.like('%mito%') | Dinuctbl.c.seq_length > 9000))
        query = sq.select(Dinuctbl)
        query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.notlike('%mito%'))
        query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.like('%mito%'))
        query = sq.select(Dinuctbl).filter((Dinuctbl.c.id) &
                                           (Dinuctbl.c.description.notlike('%mito%')) & 
                                           (Dinuctbl.c.di_diff) &
                                           (Dinuctbl.c.di_shuffle_diff))
        query = sq.select(Dinuctbl).order_by(Dinuctbl.c.di_diff)
        
        di_diff = [row.di_diff for row in engine.execute(query)]
        di_shuffle_diff = [row.di_shuffle_diff for row in engine.execute(query)]
        
        return di_diff, di_shuffle_diff