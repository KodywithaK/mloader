"""Domain enums used across loader and exporters."""

from enum import Enum


class Language(Enum):
    """Represent supported manga languages."""

    DUMMY = -1
    ENG = 0 # ENGLISH
    SPA = 1 # SPANISH
    FRA = 2 # FRENCH
    IND = 3 # INDONESIAN
    POR = 4 # PORTUGUESE
    RUS = 5 # RUSSIAN
    THA = 6 # THAI
    DEU = 7 # GERMAN
    VIE = 9 # VIETNAMESE


class ChapterType(Enum):
    """Represent chapter ordering categories returned by the API."""

    LATEST = 0
    SEQUENCE = 1
    NO_SEQUENCE = 2


class PageType(Enum):
    """Represent page layout types in manga viewer responses."""

    SINGLE = 0
    LEFT = 1
    RIGHT = 2
    DOUBLE = 3
