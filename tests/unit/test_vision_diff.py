"""Unit tests for vision/diff.py with mocked capture_screen."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_wait_for_change_detects_change(mocker):
    mock_capture = mocker.patch("mac_control_mcp.vision.capture.capture_screen")
    mock_capture.side_effect = [
        {"data": "AAAA"},  # baseline
        {"data": "BBBB"},  # first poll - changed
        {"data": "BBBB"},  # final full screenshot
    ]
    from mac_control_mcp.vision.diff import wait_for_change
    result = wait_for_change(timeout_s=5.0, poll_interval=0.1)
    assert result["changed"] is True
    assert result["elapsed_s"] > 0


@pytest.mark.unit
def test_wait_for_change_timeout(mocker):
    mock_capture = mocker.patch("mac_control_mcp.vision.capture.capture_screen")
    mock_capture.return_value = {"data": "AAAA"}  # never changes
    from mac_control_mcp.vision.diff import wait_for_change
    result = wait_for_change(timeout_s=0.3, poll_interval=0.05)
    assert result["changed"] is False
    assert result["elapsed_s"] >= 0.25


@pytest.mark.unit
def test_hash_image_b64():
    from mac_control_mcp.vision.diff import _hash_image_b64
    h1 = _hash_image_b64("AAAA")
    h2 = _hash_image_b64("AAAA")
    h3 = _hash_image_b64("BBBB")
    assert h1 == h2
    assert h1 != h3
