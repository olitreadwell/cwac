"""Tests the language audit's English-text detection."""

from bs4 import BeautifulSoup

from src.audit_plugins.language_audit import LanguageAudit


def test_is_english_text_defaults_to_true_without_lang_attributes() -> None:
  """Return True when no lang attribute is present on the element or its ancestors."""
  soup = BeautifulSoup('<html><body><p>Hello world</p></body></html>', 'html.parser')

  assert LanguageAudit.is_english_text(soup.find('p')) is True


def test_is_english_text_accepts_english_lang_on_element() -> None:
  """Return True when the element itself declares an English lang."""
  soup = BeautifulSoup('<p lang="en">Hello</p>', 'html.parser')

  assert LanguageAudit.is_english_text(soup.find('p')) is True


def test_is_english_text_accepts_english_lang_with_region() -> None:
  """Return True for an English lang that includes a region suffix."""
  soup = BeautifulSoup('<p lang="en-NZ">Hello</p>', 'html.parser')

  assert LanguageAudit.is_english_text(soup.find('p')) is True


def test_is_english_text_rejects_non_english_lang_on_element() -> None:
  """Return False when the element itself declares a non-English lang."""
  soup = BeautifulSoup('<p lang="mi">Kia ora</p>', 'html.parser')

  assert LanguageAudit.is_english_text(soup.find('p')) is False


def test_is_english_text_rejects_non_english_lang_on_ancestor() -> None:
  """Return False when an ancestor declares a non-English lang."""
  soup = BeautifulSoup('<div lang="mi"><p>Kia ora</p></div>', 'html.parser')

  assert LanguageAudit.is_english_text(soup.find('p')) is False


def test_is_english_text_uses_the_nearest_lang_attribute() -> None:
  """Return True when the element's own English lang overrides a non-English ancestor."""
  soup = BeautifulSoup(
    '<div lang="mi"><p lang="en">Hello</p></div>',
    'html.parser',
  )

  assert LanguageAudit.is_english_text(soup.find('p')) is True


def test_is_english_text_matches_lang_case_insensitively() -> None:
  """Return True when the lang attribute uses uppercase letters."""
  soup = BeautifulSoup('<p lang="EN">Hello</p>', 'html.parser')

  assert LanguageAudit.is_english_text(soup.find('p')) is True
