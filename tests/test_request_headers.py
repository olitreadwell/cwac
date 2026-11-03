"""Tests for extra request headers."""

from types import SimpleNamespace
from typing import cast

import pytest
import responses
from responses import matchers

from config import Config
from src.filters import process_url_headers
from src.request_headers import ENV_VAR, extra_request_headers, parse_extra_headers


def test_parse_extra_headers_parses_multiple_headers() -> None:
  """Parses newline-separated `Name: value` pairs."""
  assert parse_extra_headers('Authorization: Bearer abc\nAccept-Language: en-NZ') == {
    'Authorization': 'Bearer abc',
    'Accept-Language': 'en-NZ',
  }


def test_parse_extra_headers_keeps_colons_in_values() -> None:
  """Only splits each line on the first colon."""
  assert parse_extra_headers('X-Source: a:b:c') == {'X-Source': 'a:b:c'}


def test_parse_extra_headers_skips_blank_and_invalid_lines() -> None:
  """Ignores blank lines and lines that are not a `Name: value` pair."""
  assert parse_extra_headers('\nX-Test: 1\nnot-a-header\n: value\n\t\nX-Other: 2\n') == {
    'X-Test': '1',
    'X-Other': '2',
  }


def test_extra_request_headers_reads_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
  """Reads the headers from the `EXTRA_HEADERS` environment variable."""
  monkeypatch.setenv(ENV_VAR, 'X-Test: 1')

  assert extra_request_headers() == {'X-Test': '1'}


def test_extra_request_headers_defaults_to_empty(monkeypatch: pytest.MonkeyPatch) -> None:
  """Returns no headers when the environment variable is not set."""
  monkeypatch.delenv(ENV_VAR, raising=False)

  assert not extra_request_headers()


@responses.activate
def test_process_url_headers_sends_extra_request_headers(monkeypatch: pytest.MonkeyPatch) -> None:
  """Sends configured extra request headers with the header check request."""
  monkeypatch.setenv(ENV_VAR, 'Authorization: Bearer abc')
  config = SimpleNamespace(user_agent='cwac-test')
  responses.head(
    'https://example.com/page',
    content_type='text/html',
    match=[matchers.header_matcher({'User-Agent': 'cwac-test', 'Authorization': 'Bearer abc'})],
  )

  process_url_headers(cast(Config, config), 'https://example.com/page')

  assert len(responses.calls) == 1
