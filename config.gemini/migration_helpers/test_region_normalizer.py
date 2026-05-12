# config.gemini/migration_helpers/test_region_normalizer.py
import pytest
from .region_normalizer import normalize_region_name

def test_kab_prefix_normalization():
    assert normalize_region_name("KAB. SIDOARJO") == "sidoarjo"
    assert normalize_region_name("kab. BANDUNG") == "bandung"
    assert normalize_region_name("KAB. PASURUAN") == "pasuruan"

def test_kota_prefix_normalization():
    assert normalize_region_name("KOTA SURABAYA") == "kota surabaya"
    assert normalize_region_name("kota MALANG") == "kota malang"
    assert normalize_region_name("KOTA JAKARTA PUSAT") == "kota jakarta pusat"

def test_provinsi_prefix_normalization():
    assert normalize_region_name("PROVINSI JAWA TIMUR") == "jawa timur"
    assert normalize_region_name("Provinsi. Bali") == "bali"

def test_mixed_case_and_whitespace():
    assert normalize_region_name("  jakarta  ") == "jakarta"
    assert normalize_region_name("PROVINSI BANTEN") == "banten"
    assert normalize_region_name("JAWA BARAT") == "jawa barat"

def test_no_prefix():
    assert normalize_region_name("Jakarta") == "jakarta"
    assert normalize_region_name("Bandung") == "bandung"

def test_empty_string():
    assert normalize_region_name("") == ""

def test_non_string_input():
    assert normalize_region_name(None) == ""
    assert normalize_region_name(123) == ""
