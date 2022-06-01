import sqlalchemy as sq
from collections import defaultdict
from Classes.InitVars import InitVars as iv
from sqlalchemy import MetaData, or_, and_
from sqlalchemy.orm import Load, load_only, defer

class GetColumn():
    def __init__(self) -> None:
        self.db = iv.db_file
        self.tbl = iv.db_table
        self.engine = sq.create_engine(f"sqlite:///{self.db}")
        self.meta_data = sq.MetaData(bind=self.engine)
        MetaData.reflect(self.meta_data)
        self.Dinuctbl = self.meta_data.tables[self.tbl]
        pass
    
    def getColumn(self) -> list:
        engine = sq.create_engine(f"sqlite:///{self.db}")
        meta_data = sq.MetaData(bind=engine)
        sq.MetaData.reflect(meta_data)
        Dinuctbl = meta_data.tables[self.tbl]
        
        query = sq.select([Dinuctbl.c.di_diff_mean,
                          Dinuctbl.c.di_diff_stdev,
                          Dinuctbl.c.mono_shuffle_di_diff_mean,
                          Dinuctbl.c.mono_shuffle_di_diff_stdev,
                          Dinuctbl.c.di_shuffle_di_diff_mean,
                          Dinuctbl.c.di_shuffle_di_diff_stdev,
                          Dinuctbl.c.tri_shuffle_di_diff_mean,
                          Dinuctbl.c.tri_shuffle_di_diff_stdev])
        result = self.engine.execute(query)
        
        i = 1
        for record in result:
            print(f"{i} {record[0]:.9f}\t{record[1]:.9f} \
                        \t{record[2]:.9f}\t{record[3]:.9f} \
                        \t{record[4]:.9f}\t{record[5]:.9f} \
                        \t{record[6]:.9f}\t{record[7]:.9f}")
            i += 1
        
        # query = db.select(Dinuctbl).get(84) # select row by id
        # query = db.select(Dinuctbl).filter(Dinuctbl.c.id.in_(100, 120))
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.id.between(15,51))
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.notlike('%mito%'))
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.like('%plasm%'))
        # query = sq.select(Dinuctbl).filter((Dinuctbl.c.description.like('%mito%') | Dinuctbl.c.seq_length > 9000))
        # query = sq.select(Dinuctbl)
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.notlike('%mito%'))
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.like('%mito%'))
        # query = sq.select(Dinuctbl).filter((Dinuctbl.c.id) &
        #                                    (Dinuctbl.c.description.notlike('%mito%')) & 
        #                                    (Dinuctbl.c.di_diff) &
        #                                    (Dinuctbl.c.di_shuffle_diff))
        # query = sq.select(Dinuctbl).filter((Dinuctbl.c.description.notlike('%mito%')) &
        #                                    (Dinuctbl.c.description.notlike('%chlorop%')) &
        #                                    (Dinuctbl.c.description.notlike('NW_%')))
    
        # query = sq.select(Dinuctbl).filter(Dinuctbl.c.description.notlike('%mito%'))
        
        # query = sq.select(self.Dinuctbl)
        
        # di_diff = [row.di_diff for row in self.engine.execute(query)]
        # mono_shuffle = [row.mono_shuffle_diff for row in self.engine.execute(query)]
        # di_shuffle = [row.di_shuffle_diff for row in self.engine.execute(query)]
        # tri_shuffle = [row.tri_shuffle_diff for row in self.engine.execute(query)]
        
        
        return record[0], record[1]
    
    def getDinucColumn(self):
        query = sq.select(self.Dinuctbl).where(self.Dinuctbl.c.id == 84)
        
        dinuc_dict = {}
        for item in self.engine.execute(query):
            item = dict(item)
            for key, value in item.items():
                if key in iv.dinuc_list:
                    print(key, [float(itm) for itm in value.split(',')])
                    dinuc_dict[key] = [float(itm) for itm in value.split(',')]
                    
        return dinuc_dict