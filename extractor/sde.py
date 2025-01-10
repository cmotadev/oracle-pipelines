import sqlalchemy as sa


class FeatureClassExtractor:
    """
    _summary_
    """
    def __init__(self, engine, schema, table):
        self._engine = engine
        self._schema = schema
        self._schema = table