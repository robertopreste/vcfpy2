#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
"""Reading of VCF files from plain and bgzip-ed files
"""

import os

from vcfpy2 import reader

__author__ = "Manuel Holtgrewe <manuel.holtgrewe@bihealth.de>"


def test_read_text():
    path = os.path.join(os.path.dirname(__file__), "vcfs/full_vcf43.vcf")
    r = reader.Reader.from_path(path)
    assert r.parser
    assert r.header
    assert len(r.header.lines) == 18
    assert r.header.samples
    assert r.header.samples.names == ["NA00001", "NA00002", "NA00003"]
    records = []
    for record in r:
        records.append(record)
    assert len(records) == 5


def test_read_bgzip():
    path = os.path.join(os.path.dirname(__file__), "vcfs/full_vcf43.vcf.gz")
    r = reader.Reader.from_path(path)
    assert r.parser
    assert r.header
    assert len(r.header.lines) == 18
    assert r.header.samples
    assert r.header.samples.names == ["NA00001", "NA00002", "NA00003"]
    records = []
    for record in r:
        records.append(record)
    assert len(records) == 5


def test_read_text_no_samples():
    path = os.path.join(os.path.dirname(__file__), "vcfs/full_vcf43_no_samples.vcf")
    r = reader.Reader.from_path(path)
    assert r.parser
    assert r.header
    assert len(r.header.lines) == 18
    assert r.header.samples
    assert r.header.samples.names == []
    records = []
    for record in r:
        records.append(record)
    assert len(records) == 5
