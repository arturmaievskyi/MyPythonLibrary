from .Calc import __init__ as calc_init
from .Console import __init__ as console_init
from .Converters import __init__ as converters_init
from .Physics import __init__ as physics_init
from .Systemoperationsystem import __init__ as system_ops_init
from .file_helper import FileHelper
__init__ = {
    "calc": calc_init,
    "console": console_init,
    "converters": converters_init,
    "physics": physics_init,
    "systemoperationsystem": system_ops_init
}