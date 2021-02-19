import pkg_resources

from .fact_utils import dict_to_facts
from .programs import definitions
from .run import is_satisfiable, run_clingo
from .schema import schema_from_dataframe

__version__ = pkg_resources.get_distribution("draco").version

__all__ = [
    "dict_to_facts",
    "definitions",
    "run_clingo",
    "is_satisfiable",
    "schema_from_dataframe",
]
