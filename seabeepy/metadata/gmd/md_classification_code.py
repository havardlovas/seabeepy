from dataclasses import dataclass
from seabeepy.metadata.gmd.code_list_value_type import CodeListValueType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdClassificationCode(CodeListValueType):
    class Meta:
        name = "MD_ClassificationCode"
        namespace = "http://www.isotc211.org/2005/gmd"
