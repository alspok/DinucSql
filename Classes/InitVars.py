from ntpath import join


class InitVars():
    db_path = "../DinucSql/"
    db_name = "embryophyta1.sqlite3"
    db_file = join(db_path, db_name)
    db_table = "dinuctbl"