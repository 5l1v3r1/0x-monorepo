from distutils.dist import Distribution
from typing import Any, List

def setup(**attrs: Any) -> Distribution: ...

class Command: ...

def find_packages(where: str) -> List[str]: ...