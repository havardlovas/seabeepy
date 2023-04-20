from dataclasses import dataclass
from seabeepy.metadata.gmd.code_list_value_type import CodeListValueType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeometricObjectTypeCode(CodeListValueType):
    class Meta:
        name = "MD_GeometricObjectTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"
