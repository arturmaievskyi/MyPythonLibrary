from .base_calculator import BaseCalculator
from .advanced_calculator import AdvancedCalculator
from .expression import Expression
from .analitics import __init__ as analitics_init
from .topology import __init__ as topology_init
from .figures import __init__ as figures_init


__init__={
    "base_calculator": BaseCalculator,
    "advanced_calculator": AdvancedCalculator,
    "expression": Expression,
    "analitics": analitics_init,
    "topology": topology_init,
    "figures": figures_init
}