from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.dq_absolute_external_positional_accuracy import DqAbsoluteExternalPositionalAccuracy
from seabeepy.metadata.gmd.dq_gridded_data_positional_accuracy import DqGriddedDataPositionalAccuracy
from seabeepy.metadata.gmd.dq_relative_internal_positional_accuracy import DqRelativeInternalPositionalAccuracy
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqPositionalAccuracyPropertyType:
    class Meta:
        name = "DQ_PositionalAccuracy_PropertyType"

    dq_absolute_external_positional_accuracy: Optional[DqAbsoluteExternalPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_AbsoluteExternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_gridded_data_positional_accuracy: Optional[DqGriddedDataPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_GriddedDataPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_relative_internal_positional_accuracy: Optional[DqRelativeInternalPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_RelativeInternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
