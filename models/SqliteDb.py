import sqlite3 as sq
from controllers.FileSystem import ConfigController

con = sq.connect(database=ConfigController.get_config('PATHS','db'))


class SqliteDbModel:
    @staticmethod
    def get_all_games():
        return con.execute('SELECT name,slug,platform FROM GAMES').fetchall()