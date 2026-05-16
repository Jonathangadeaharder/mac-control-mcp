"""Test ax module fallback paths when Quartz/AX unavailable."""

from __future__ import annotations

import pytest


@pytest.mark.unit
def test_require_quartz_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.actions._QUARTZ_AVAILABLE", False)
    from mac_control_mcp.ax.actions import _require_quartz
    with pytest.raises(RuntimeError, match="pyobjc Quartz not installed"):
        _require_quartz()


@pytest.mark.unit
def test_mouse_click_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.actions._QUARTZ_AVAILABLE", False)
    from mac_control_mcp.ax.actions import mouse_click
    with pytest.raises(RuntimeError, match="pyobjc Quartz not installed"):
        mouse_click(0, 0)


@pytest.mark.unit
def test_mouse_move_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.actions._QUARTZ_AVAILABLE", False)
    from mac_control_mcp.ax.actions import mouse_move
    with pytest.raises(RuntimeError):
        mouse_move(0, 0)


@pytest.mark.unit
def test_type_text_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.actions._QUARTZ_AVAILABLE", False)
    from mac_control_mcp.ax.actions import type_text
    with pytest.raises(RuntimeError):
        type_text("hello")


@pytest.mark.unit
def test_scroll_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.actions._QUARTZ_AVAILABLE", False)
    from mac_control_mcp.ax.actions import scroll
    with pytest.raises(RuntimeError):
        scroll(0, 0, 1)


@pytest.mark.unit
def test_hotkey_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.actions._QUARTZ_AVAILABLE", False)
    from mac_control_mcp.ax.actions import hotkey
    with pytest.raises(RuntimeError):
        hotkey(["cmd", "c"])


@pytest.mark.unit
def test_snapshot_app_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.snapshot._AX_AVAILABLE", False)
    from mac_control_mcp.ax.snapshot import snapshot_app
    with pytest.raises(RuntimeError, match="pyobjc ApplicationServices not installed"):
        snapshot_app("Finder")


@pytest.mark.unit
def test_focused_element_raises_when_unavailable(monkeypatch):
    monkeypatch.setattr("mac_control_mcp.ax.snapshot._AX_AVAILABLE", False)
    from mac_control_mcp.ax.snapshot import focused_element
    with pytest.raises(RuntimeError):
        focused_element()
