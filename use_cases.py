import json
import functools
from lib import *

# var 1
# json.dumps(
#     need("buy butter").at("16:30").done(), indent=4,
#         )

# json.dumps(
#     at("16:30").need("buy butter").done(), indent=4
#         )

# var 2
need("buy butter", at(["16:30", "15:20"]))

at("16:30", need("buy butter"))
