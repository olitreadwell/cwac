"""Tests the behaviour of URL filter functions."""

import pytest

from src import filters


def test_url_filter_not_same_domain_returns_false_for_different_domains() -> None:
  """Returns False when the two URLs have different domains."""
  assert filters.url_filter_not_same_domain('https://a.govt.nz', 'https://b.govt.nz') is False


def test_url_filter_not_same_domain_returns_true_for_same_domain() -> None:
  """Returns True when the two URLs share a domain, ignoring www and case."""
  assert filters.url_filter_not_same_domain('https://www.example.govt.nz/', 'https://Example.Govt.Nz/page') is True


def test_url_filter_not_same_domain_logs_base_and_filtered_url(caplog: pytest.LogCaptureFixture) -> None:
  """The log labels which URL is the base and which is being filtered out."""
  with caplog.at_level('INFO', logger='cwac'):
    filters.url_filter_not_same_domain('https://findajob.msd.govt.nz', 'https://www.msd.govt.nz')

  assert caplog.records
  message = caplog.records[0].getMessage()
  assert 'base_url: https://www.msd.govt.nz' in message
  assert 'filtered_url: https://findajob.msd.govt.nz' in message
