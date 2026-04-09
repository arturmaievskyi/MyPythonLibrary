from .calc import __init__ as calc_init
from .console import __init__ as console_init
from .converters import __init__ as converters_init
from .physics import __init__ as physics_init
from .systemoperationsystem import __init__ as system_ops_init

__init__ = {
    "calc": calc_init,
    "console": console_init,
    "converters": converters_init,
    "physics": physics_init,
    "systemoperationsystem": system_ops_init
}