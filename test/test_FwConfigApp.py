#!/usr/bin/env python
"""
test_FwConfigApp.py

Description:
Automated pytest script for FwConfigApp.py.

Usage:
    py.test -vv test_FwConfigApp.py \
      --junitxml='./test_file_transfer_util_junit.xml'
"""

import os

from FwConfigApp import _validate_ip_octet
from FwConfigApp import _validate_ip_address

# ----------------------------------------------------------------------------
# Test setup
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Test functions
# ----------------------------------------------------------------------------
def test_validate_ip_octet_is_in_range_center():
    """
    test_validate_ip_octet_is_in_range_center

    This test will test the ability of the _validate_ip_octet function to be
    be able to determine that a provided octet value is within the min/max
    ip octet range.
    """

    expected_result = True

    test_octet_value = 100
    actual_result = _validate_ip_octet(test_octet_value)

    assert actual_result == expected_result


def test_validate_ip_octet_is_in_range_low():
    """
    test_validate_ip_octet_is_in_range_low

    This test will test the ability of the _validate_ip_octet function to be
    be able to determine that a provided octet value is within the min/max
    ip octet range when provided value is set to the minimum acceptable value.
    """

    expected_result = True

    test_octet_value = 0
    actual_result = _validate_ip_octet(test_octet_value)

    assert actual_result == expected_result


def test_validate_ip_octet_is_in_range_high():
    """
    test_validate_ip_octet_is_in_range_high

    This test will test the ability of the _validate_ip_octet function to be
    be able to determine that a provided octet value is within the min/max
    ip octet range when provided value is set to the maximum acceptable value.
    """
    expected_result = True

    test_octet_value = 255
    actual_result = _validate_ip_octet(test_octet_value)

    assert actual_result == expected_result


def test_validate_ip_octet_is_out_range_high():
    """
    test_validate_ip_octet_is_out_range_high

    This test will test the ability of the _validate_ip_octet function to be
    be able to determine that a provided octet value is outside the min/max
    ip octet range when provided value is just above the maximum acceptable
    value.
    """
    expected_result = False

    test_octet_value = 256
    actual_result = _validate_ip_octet(test_octet_value)

    assert actual_result == expected_result


def test_validate_ip_octet_is_out_range_low():
    """
    test_validate_ip_octet_is_out_range_low

    This test will test the ability of the _validate_ip_octet function to be
    be able to determine that a provided octet value is outside the min/max
    ip octet range when provided value is just below the minimum acceptable
    value.
    """
    expected_result = False

    test_octet_value = -1
    actual_result = _validate_ip_octet(test_octet_value)

    assert actual_result == expected_result


def test_validate_ip_address_ip_good():
    """
    test_validate_ip_address_ip_good

    This test will test the ability of the _validate_ip_address function to be
    able to detect a valid IP address.
    """

    expected_result = True

    test_ip_address = '192.168.20.4'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_1_out_of_range():
    """
    test_validate_ip_address_ip_bad_octet_1_out_of_range

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (first address octet out of range)
    """

    expected_result = False

    test_ip_address = '256.168.20.4'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_2_out_of_range():
    """
    test_validate_ip_address_ip_bad_octet_2_out_of_range

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (second address octet out of range)
    """

    expected_result = False

    test_ip_address = '192.256.20.4'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_3_out_of_range():
    """
    test_validate_ip_address_ip_bad_octet_3_out_of_range

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (third address octet out of range)
    """

    expected_result = False

    test_ip_address = '192.168.256.4'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_4_out_of_range():
    """
    test_validate_ip_address_ip_bad_octet_4_out_of_range

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (fourth address octet out of range)
    """

    expected_result = False

    test_ip_address = '192.168.20.256'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_1_not_num_():
    """
    test_validate_ip_address_ip_bad_octet_1_not_num_

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (first address octet not a number)
    """

    expected_result = False

    test_ip_address = 'bob.168.20.256'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_2_not_num_():
    """
    test_validate_ip_address_ip_bad_octet_2_not_num_

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (second address octet not a number)
    """

    expected_result = False

    test_ip_address = '192.bob.20.256'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_3_not_num_():
    """
    test_validate_ip_address_ip_bad_octet_3_not_num_

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (third address octet not a number)
    """

    expected_result = False

    test_ip_address = '192.168.bob.256'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result


def test_validate_ip_address_ip_bad_octet_4_not_num_():
    """
    test_validate_ip_address_ip_bad_octet_4_not_num_

    This test will test the ability of the _validate_ip_address function to be
    able to detect a bad IP address (first address octet not a number)
    """

    expected_result = False

    test_ip_address = '192.168.20.bob'
    actual_result = _validate_ip_address(test_ip_address)

    assert actual_result == expected_result
