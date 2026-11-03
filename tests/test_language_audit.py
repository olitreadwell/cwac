"""Tests the language filtering in src/audit_plugins/language_audit.py."""

import pytest
from bs4 import BeautifulSoup

from src.audit_plugins.language_audit import LanguageAudit


@pytest.mark.parametrize(
  'lang,expected',
  [
    ('en', True),
    ('en-NZ', True),
    ('EN-nz', True),
    ('  en  ', True),
    ('', True),
    ('mi', False),
    ('fr', False),
    ('de-DE', False),
    ('enclitic', False),
  ],
)
def test_is_english_lang(lang: str, expected: bool) -> None:
  """Treats English (and empty) tags as English and everything else as non-English."""
  assert LanguageAudit.is_english_lang(lang) is expected


def test_filter_removes_element_with_non_english_lang() -> None:
  """Drops an element whose own lang attribute is non-English, keeps English siblings."""
  soup = BeautifulSoup(
    '<p lang="mi">He kupu Maori</p><p>An English sentence.</p>',
    'html.parser',
  )
  LanguageAudit.filter_out_non_english_language(soup)
  text = soup.get_text()
  assert 'Maori' not in text
  assert 'English sentence' in text


def test_filter_removes_text_inheriting_non_english_from_ancestor() -> None:
  """Drops text that inherits a non-English lang from an ancestor element."""
  soup = BeautifulSoup(
    '<div lang="mi"><p>He kupu Maori</p></div><p>An English sentence.</p>',
    'html.parser',
  )
  LanguageAudit.filter_out_non_english_language(soup)
  text = soup.get_text()
  assert 'Maori' not in text
  assert 'English sentence' in text


def test_filter_keeps_elements_declared_english() -> None:
  """Keeps text explicitly declared as English (en or en-*)."""
  soup = BeautifulSoup(
    '<p lang="en">Plain English.</p><p lang="en-NZ">New Zealand English.</p>',
    'html.parser',
  )
  LanguageAudit.filter_out_non_english_language(soup)
  text = soup.get_text()
  assert 'Plain English' in text
  assert 'New Zealand English' in text


def test_filter_leaves_untagged_text_untouched() -> None:
  """Keeps text that has no lang attribute anywhere."""
  soup = BeautifulSoup('<p>No language attribute here.</p>', 'html.parser')
  LanguageAudit.filter_out_non_english_language(soup)
  assert 'No language attribute here.' in soup.get_text()


def test_filter_drops_whole_non_english_ancestor_including_nested_english() -> None:
  """Removes a non-English ancestor as a whole, including any nested English element.

  This is a deliberate simplification: a re-declared English part inside a
  non-English block is rare, and removing the block is safer for a readability
  score than trying to re-parent it.
  """
  soup = BeautifulSoup(
    '<div lang="mi"><p lang="en">Nested English quote.</p></div>',
    'html.parser',
  )
  LanguageAudit.filter_out_non_english_language(soup)
  assert soup.get_text().strip() == ''
