from .BioSeq import BioSeq, ReprSeq
from .SeqAnalyzer import SeqAnalyzer
from .BioCode import BioCode
from ._Weight_ import Weight
from .__version__ import __version__

__author__ = "RC Fofanahy"

__all__ = [
    "BioSeq", "ReprSeq",
    "SeqAnalyzer",
    "BioCode",
    "Weight"
]

SeqCode = BioCode
BioAnalyzer = SeqAnalyzer
Bios = SeqNavig = BioSeq
Repr = ReprSeq