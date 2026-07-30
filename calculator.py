"""Tiny calculator module used as fixture code for PR-review pipeline tests."""
import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def average(a,b):
    unused = 42
    return (a+b)/2
