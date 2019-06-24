#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
"""Test escaping on writing VCF records
"""

from vcfpy2 import writer
from vcfpy2 import header

# vcfpy.writer.format_atomic() ------------------------------------------------


def test_format_atomic_with_escape():
    EXPECTED = "%3A%3B%3D%25%2C%0D%0A%09"
    RESULT = writer.format_atomic(":;=%,\r\n\t")
    assert EXPECTED == RESULT


def test_format_atomic_without_escape():
    EXPECTED = "This is a legal string"
    RESULT = writer.format_atomic("This is a legal string")
    assert EXPECTED == RESULT


# vcfpy.writer.format_value() -------------------------------------------------


def test_format_value_with_escape():
    EXPECTED = "%3A%3B%3D%25%2C%0D%0A%09,%25"
    RESULT = writer.format_value(header.FieldInfo("String", 2), (":;=%,\r\n\t", "%"), "INFO")
    assert EXPECTED == RESULT


def test_format_value_without_escape():
    EXPECTED = "This is a legal string,me too"
    RESULT = writer.format_value(
        header.FieldInfo("String", 2), ("This is a legal string", "me too"), "INFO"
    )
    assert EXPECTED == RESULT
