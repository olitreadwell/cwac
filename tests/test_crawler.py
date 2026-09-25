"""Tests the behaviour of the Crawler class."""

from unittest.mock import MagicMock

import pytest

from src.crawler import Crawler


def make_crawler(base_urls: list[str]) -> Crawler:
  """Create a Crawler stub with only the analytics needed for scope checks."""
  crawler = object.__new__(Crawler)
  crawler.analytics = MagicMock()
  crawler.analytics.base_urls = base_urls
  return crawler


def test_prevent_intersections_filters_outside_scope(caplog: pytest.LogCaptureFixture) -> None:
  """Logs base_url and filtered_url when a URL is not within the base scope."""
  crawler = make_crawler([])

  with caplog.at_level('INFO', logger='cwac'):
    result = crawler.url_filter_prevent_intersections(
      'https://example.govt.nz/news',
      'https://example.govt.nz/other',
    )

  assert result is False
  assert caplog.records
  message = caplog.records[0].getMessage()
  assert 'base_url: https://example.govt.nz/news' in message
  assert 'filtered_url: https://example.govt.nz/other' in message


def test_prevent_intersections_filters_in_another_scope(caplog: pytest.LogCaptureFixture) -> None:
  """Logs the more specific base_url when a URL belongs to another scope."""
  crawler = make_crawler(['https://example.govt.nz/news'])

  with caplog.at_level('INFO', logger='cwac'):
    result = crawler.url_filter_prevent_intersections(
      'https://example.govt.nz',
      'https://example.govt.nz/news/thing',
    )

  assert result is False
  assert caplog.records
  message = caplog.records[0].getMessage()
  assert 'base_url: https://example.govt.nz/news' in message
  assert 'filtered_url: https://example.govt.nz/news/thing' in message
