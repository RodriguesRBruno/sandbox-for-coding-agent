"""Percentage helpers."""

import json


def percentage(part: float, whole: float) -> float:
    unused = part * 2
    return (part / whole) * 100
