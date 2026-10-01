"""Extra request headers loaded from the `EXTRA_HEADERS` environment variable."""

import logging
import os

logger = logging.getLogger('cwac')

ENV_VAR = 'EXTRA_HEADERS'


def parse_extra_headers(value: str) -> dict[str, str]:
  """Parse the newline-separated `Name: value` pairs in `value`."""
  headers: dict[str, str] = {}

  for line in value.splitlines():
    if not line.strip():
      continue

    name, separator, header_value = line.partition(':')
    if not separator or not name.strip():
      logger.warning('Ignoring extra header as it is not a "Name: value" pair')
      continue

    headers[name.strip()] = header_value.strip()

  return headers


def extra_request_headers() -> dict[str, str]:
  """Return the extra request headers set through the environment."""
  return parse_extra_headers(os.environ.get(ENV_VAR, ''))
