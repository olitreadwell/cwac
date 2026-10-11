"""Tests for the browser wrapper."""

from types import SimpleNamespace
from typing import cast

import pytest
from pytest_mock import MockerFixture

from config import Config
from src.browser import Browser
from src.request_headers import ENV_VAR


def build_config() -> SimpleNamespace:
  """Return the minimum configuration needed to spawn a browser."""
  return SimpleNamespace(
    audit_name='test-audit',
    chrome_binary_location='auto',
    chrome_driver_location='auto',
    headless=True,
    page_load_timeout=10,
    script_timeout=15,
    user_agent='cwac-test',
    viewport_sizes={'small': {'width': 320, 'height': 450}},
  )


def test_spawn_sends_extra_request_headers(mocker: MockerFixture, monkeypatch: pytest.MonkeyPatch) -> None:
  """Applies configured extra request headers to the browser."""
  monkeypatch.setenv(ENV_VAR, 'Authorization: Bearer abc\nAccept-Language: en-NZ')
  driver = mocker.Mock()
  mocker.patch('src.browser.webdriver.Chrome', return_value=driver)
  mocker.patch('src.browser.Service')

  Browser(cast(Config, build_config()), thread_id=1)

  driver.execute_cdp_cmd.assert_any_call('Network.enable', {})
  driver.execute_cdp_cmd.assert_any_call(
    'Network.setExtraHTTPHeaders',
    {'headers': {'Authorization': 'Bearer abc', 'Accept-Language': 'en-NZ'}},
  )


def test_spawn_without_extra_request_headers(mocker: MockerFixture, monkeypatch: pytest.MonkeyPatch) -> None:
  """Does not configure request headers when none are set."""
  monkeypatch.delenv(ENV_VAR, raising=False)
  driver = mocker.Mock()
  mocker.patch('src.browser.webdriver.Chrome', return_value=driver)
  mocker.patch('src.browser.Service')

  Browser(cast(Config, build_config()), thread_id=1)

  driver.execute_cdp_cmd.assert_not_called()
