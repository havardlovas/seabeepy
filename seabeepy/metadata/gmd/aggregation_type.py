from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class AggregationType(Enum):
    SET = "set"
    BAG = "bag"
    SEQUENCE = "sequence"
    ARRAY = "array"
    RECORD = "record"
    TABLE = "table"
