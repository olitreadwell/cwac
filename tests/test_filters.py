"""Tests the URL filter functions in src/filters.py."""

import urllib.parse
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from src.filters import (
  URLFilter,
  url_filter_by_header_content_type,
  url_filter_filetype,
  url_filter_fragment,
  url_filter_http,
  url_filter_https_only,
  url_filter_not_same_domain,
  url_filter_same_protocol,
)


def parse(url: str) -> urllib.parse.ParseResult:
  """Parse a URL into the ParseResult shape the filters expect."""
  return urllib.parse.urlparse(url)


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


def test_url_filter_https_only_requires_https_when_configured() -> None:
  config = SimpleNamespace(only_allow_https=True)
  assert url_filter_https_only(config, parse('https://example.com')) is True
  assert url_filter_https_only(config, parse('http://example.com')) is False


def test_url_filter_https_only_allows_any_scheme_when_not_configured() -> None:
  config = SimpleNamespace(only_allow_https=False)
  assert url_filter_https_only(config, parse('http://example.com')) is True
  assert url_filter_https_only(config, parse('ftp://example.com')) is True


def test_url_filter_fragment_rejects_same_page_urls() -> None:
  assert url_filter_fragment(MagicMock(), parse('https://example.com/page')) is True
  assert url_filter_fragment(MagicMock(), parse('https://example.com/page#section')) is False


def test_url_filter_http_allows_http_and_https_only() -> None:
  assert url_filter_http(MagicMock(), parse('https://example.com')) is True
  assert url_filter_http(MagicMock(), parse('http://example.com')) is True
  assert url_filter_http(MagicMock(), parse('ftp://example.com')) is False
  assert url_filter_http(MagicMock(), parse('mailto:user@example.com')) is False


def test_url_filter_not_same_domain_compares_netloc_without_www() -> None:
  assert url_filter_not_same_domain('https://example.com/a', 'https://example.com/b') is True
  assert url_filter_not_same_domain('https://www.example.com/a', 'https://example.com/b') is True
  assert url_filter_not_same_domain('https://example.com/a', 'https://other.org/b') is False


def test_url_filter_same_protocol_compares_schemes() -> None:
  assert url_filter_same_protocol('https://example.com/a', 'https://other.org/b') is True
  assert url_filter_same_protocol('https://example.com/a', 'http://other.org/b') is False


def test_url_filter_by_header_content_type_accepts_text_html() -> None:
  headers = {'Content-Type': 'text/html; charset=utf-8'}
  assert url_filter_by_header_content_type('https://example.com', headers) is True


def test_url_filter_by_header_content_type_rejects_non_html() -> None:
  headers = {'Content-Type': 'application/pdf'}
  assert url_filter_by_header_content_type('https://example.com', headers) is False


def test_url_filter_by_header_content_type_rejects_missing_content_type() -> None:
  assert url_filter_by_header_content_type('https://example.com', {}) is False


def test_url_filter_registers_all_builtin_filters() -> None:
  url_filter = URLFilter(SimpleNamespace())
  assert set(url_filter.url_filters) == {
    'Non-empty fragment',
    'HTTPS only',
    'Non-http/s path',
    'Non-allowed file extension',
    'Whitelist',
  }


def test_run_url_filters_accepts_url_that_passes_every_filter() -> None:
  config = SimpleNamespace(only_allow_https=False, url_lookup={'example.com'})
  url_filter = URLFilter(config)
  assert url_filter.run_url_filters('https://example.com/page') is True


def test_run_url_filters_rejects_url_failing_any_filter() -> None:
  config = SimpleNamespace(only_allow_https=False, url_lookup={'example.com'})
  url_filter = URLFilter(config)
  assert url_filter.run_url_filters('http://example.com/report.pdf') is False
  assert url_filter.run_url_filters('https://other.org/page') is False
