"""Build must not crash when the markdown has no h1 heading."""

import os

from resume_markdown.__main__ import make_html


def test_make_html_without_h1_uses_filename_as_title(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    html = make_html("Just some text without a heading.\n", prefix="nohead")
    assert "<title>nohead</title>" in html
    assert "no h1 heading found" in capsys.readouterr().out


def test_make_html_with_h1_keeps_heading_title(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    html = make_html("# Jane Doe\n\nSome text.\n", prefix="resume")
    assert "<title>Jane Doe</title>" in html

