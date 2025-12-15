from enum import Enum


class PathPattern(str, Enum):
    GRID = "GRID"
    ZIGZAG = "ZIGZAG"
    CIRCULAR = "CIRCULAR"
    CUSTOM = "CUSTOM"
