from ntpath import join


class InitVars():
    # db_path = "../DinucSql/"
    # db_name = "embryophyta1.sqlite3"

    db_path = "F:/Procaryote/Archaea/"
    db_name = "archaea.sqlite3"
    
    db_file = join(db_path, db_name)
    db_table = "dinuctbl"