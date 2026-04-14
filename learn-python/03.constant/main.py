# Naming Convention: https://peps.python.org/pep-0008/
from typing import Final

# Implicit Constant Declaration
PI: Final = 3.1415926
print(PI)

# Explicit Constant Declaration
TOTAL_SCORE: Final[int] = 100
print(TOTAL_SCORE)
