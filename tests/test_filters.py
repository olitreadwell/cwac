"""Tests the url_filter_filetype function in src/filters.py."""

import urllib.parse
from unittest.mock import MagicMock

import pytest

from src.filters import url_filter_filetype


@pytest.mark.parametrize(
  'url,expected',
  [
    ('https://example.com/page', True),
    ('https://example.com/page.html', True),
    ('https://example.com/report.pdf', False),
    ('https://example.com/report.PDF', False),
    ('https://example.com/archive.tar.gz', False),
    ('https://example.com/image.JPG', False),
    ('https://example.com/data.csv', False),
  ],
)
def test_url_filter_filetype(url: str, expected: bool) -> None:
  """Allows URLs without a disallowed file extension, rejects those with one (case-insensitively)."""
  parsed = urllib.parse.urlparse(url)
  assert url_filter_filetype(MagicMock(), parsed) is expected
