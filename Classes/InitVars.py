from ntpath import join

class InitVars():
    # db_path = "../DinucSql/"
    # db_name = "embryophyta1.sqlite3"
    
    dinuc_list = [
        'aa', 'ac', 'ag', 'at',
        'ca', 'cc', 'cg', 'ct',
        'ga', 'gc', 'gg', 'gt',
        'ta', 'tc', 'tg', 'tt'
    ]

    db_path = "C:\\Users\\hp\\source\\repos\\DinucFrames\\DBResults\\"
    db_name = "archaea_dinuc.sqlite3"
    out_name = db_name.split('.')[0].upper()
    
    db_file = join(db_path, db_name)
    db_table = "dinuc"