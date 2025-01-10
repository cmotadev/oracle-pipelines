import sqlalchemy as sa


class FeatureClassExtractor:
    """
    _summary_
    """
    def __init__(self, engine, schema, table):
        self._engine = engine
        self._schema = schema
        self._schema = table

    @property
    def database_name(self):
        return self._engine.dialect.name

    def sde_database_version(self):
        with self._engine.connect() as conn:
            _table = 'sde.sde_version'

            if conn.dialect.name == 'oracle':
                _table = 'sde.version'        

            major, minor, bugfix = conn.execute(
                sa.text(f"SELECT major, minor, bugfix FROM {_table}"),
                
            ).fetchone()

        return major, minor, bugfix
