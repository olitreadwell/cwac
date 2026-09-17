"""Tests the URL filter functions in src/filters.py."""

import urllib.parse
from unittest.mock import MagicMock

import pytest

from src.filters import url_filter_filetype, url_filter_whitelist


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


def make_config(url_lookup: set[str]) -> MagicMock:
  """Build a stub Config whose url_lookup contains the given lowercase hostnames."""
  config = MagicMock()
  config.url_lookup = url_lookup
  return config


@pytest.mark.parametrize(
  'url,expected',
  [
    # Host is listed exactly.
    ('https://example.govt.nz/page', True),
    # Same host with a www. prefix; it should still match the non-www entry.
    ('https://www.example.govt.nz/page', True),
    # Host is not listed at all.
    ('https://other.govt.nz/page', False),
  ],
)
def test_url_filter_whitelist_plain_hostnames(url: str, expected: bool) -> None:
  """Accepts URLs whose host is whitelisted (with or without a www. prefix), rejects the rest."""
  config = make_config({'example.govt.nz'})
  parsed = urllib.parse.urlparse(url)
  assert url_filter_whitelist(config, parsed) is expected


@pytest.mark.parametrize(
  'url',
  [
    'https://Example.govt.nz/page',
    'https://EXAMPLE.GOVT.NZ/page',
  ],
)
def test_url_filter_whitelist_matches_mixed_case_host_against_www_entry(url: str) -> None:
  """Matches a mixed-case host against a www.-prefixed whitelist entry.

  Hostnames are case-insensitive, and the whitelist is stored lower-cased. A
  mixed-case host with no www. prefix must still match a whitelist entry that
  only has the www. form.
  """
  config = make_config({'www.example.govt.nz'})
  parsed = urllib.parse.urlparse(url)
  assert url_filter_whitelist(config, parsed) is True


@pytest.mark.parametrize(
  'url',
  [
    'https://WWW.example.govt.nz/page',
    'https://Www.Example.Govt.NZ/page',
  ],
)
def test_url_filter_whitelist_matches_mixed_case_www_host_against_bare_entry(url: str) -> None:
  """Matches a mixed-case www.-prefixed host against a bare whitelist entry.

  Stripping the www. prefix must not be case-sensitive. A host with a
  mixed-case www. prefix must still match a whitelist entry that only has
  the non-www. form.
  """
  config = make_config({'example.govt.nz'})
  parsed = urllib.parse.urlparse(url)
  assert url_filter_whitelist(config, parsed) is True
