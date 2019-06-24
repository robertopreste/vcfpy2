#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
"""Test Call class
"""

import vcfpy2 as vcfpy
from vcfpy2 import record

__author__ = "Manuel Holtgrewe <manuel.holtgrewe@bihealth.de>"


def build_rec(calls=None, format_extras=None):
    calls = calls or []
    format_extras = format_extras or []
    alt1 = record.Substitution(vcfpy.SNV, "T")
    alt2 = record.Substitution(vcfpy.SNV, "A")
    return record.Record(
        "2",
        100,
        [],
        "C",
        [alt1, alt2],
        None,
        [],
        vcfpy.OrderedDict(),
        ["GT"] + format_extras,
        calls,
    )


# Call.is_phased() ------------------------------------------------------------


def test_is_phased_true():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|1")]))
    assert call.is_phased is True


def test_is_phased_mixed():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0/1|2")]))
    assert call.is_phased is True


def test_is_phased_false():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0/1")]))
    assert call.is_phased is False


# Call.gt_phase_char() --------------------------------------------------------


def test_gt_phase_char_pipe():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|1")]))
    assert call.gt_phase_char == "|"


def test_gt_phase_char_slash():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0/1")]))
    assert call.gt_phase_char == "/"


# Call.gt_bases() -------------------------------------------------------------


def test_gt_bases_0_0():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|0")]))
    build_rec([call])
    assert call.gt_bases == ("C", "C")


def test_gt_bases_0_1():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|1")]))
    build_rec([call])
    assert call.gt_bases == ("C", "T")


def test_gt_bases_1_1():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "1|1")]))
    build_rec([call])
    assert call.gt_bases == ("T", "T")


def test_gt_bases_0_2():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|2")]))
    build_rec([call])
    assert call.gt_bases == ("C", "A")


# Call.gt_type() --------------------------------------------------------------


def test_gt_type_het():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|1")]))
    assert call.gt_type == vcfpy.HET


def test_gt_type_hom_ref():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0/0")]))
    assert call.gt_type == vcfpy.HOM_REF


def test_gt_type_hom_alt():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "1/1")]))
    assert call.gt_type == vcfpy.HOM_ALT


# Call.is_het() ---------------------------------------------------------------


def test_is_het_het():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|1")]))
    assert call.is_het


def test_is_het_hom_ref():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0/0")]))
    assert not call.is_het


def test_is_het_hom_alt():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "1/1")]))
    assert not call.is_het


# Call.is_variant() -----------------------------------------------------------


def test_is_variant_het():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0|1")]))
    assert call.is_variant


def test_is_variant_hom_ref():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "0/0")]))
    assert not call.is_variant


def test_is_variant_hom_alt():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "1/1")]))
    assert call.is_variant


# Call.is_filtered() ----------------------------------------------------------


def test_gt_type_filtered_no_ft():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "1/1")]))
    assert not call.is_filtered()


def test_gt_type_filtered_empty():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "1/1"), ("FT", [])]))
    assert not call.is_filtered()


def test_gt_type_filtered_pass():
    call = record.Call("sample", vcfpy.OrderedDict([("GT", "1/1"), ("FT", ["PASS"])]))
    assert not call.is_filtered()
