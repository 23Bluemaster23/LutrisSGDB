import sqlite3 as sq
from controllers.FileSystem import ConfigController
from pathlib import Path
con = sq.connect(database=Path(ConfigController.get_config('PATHS','db')).expanduser())


class SqliteDbModel:
    @staticmethod
    def get_all_games():
        return con.execute('SELECT name,slug,platform FROM GAMES').fetchall()