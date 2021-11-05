from dataclasses import dataclass
from typing import Callable

import re

@dataclass
class Command:
    pattern: str
    func: Callable
    help_info: str

    def get_usage_pattern(self):
        p = re.sub(r"\(\?P", '', self.pattern)
        second = re.sub(r"\[\^\'\]\+\)", '', p)
        third = re.sub(r"\.\*", '', second)
        fourh = re.sub(r"\\s\*", '', third)
        res = re.sub(r"\$", '', fourh)
        return res

    def get_usage(self):
        return self.get_usage_pattern() + ': ' + self.help_info 
