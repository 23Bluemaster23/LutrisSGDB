from models.SqliteDb import SqliteDbModel

class SqliteDbController:
    @staticmethod
    def get_all_games():
        res = SqliteDbModel.get_all_games()
        keys = ['name','slug','platform']

        formated = list(map(lambda item:dict(zip(keys,item)),res))
        return formated