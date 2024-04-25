import logging
import os
from typing import Any, Dict

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.types import Event, Hint


def filter_sensitive_data(event: Event, hint: Hint) -> Event | None:
    print(event)
    print(hint)
    return event


def filter_sensitive_breadcrumb_data(
    crumb: Dict[str, Any], hint: Dict[str, Any]
) -> dict[str, Any] | None:
    print(crumb)
    print(hint)
    return crumb


logging.basicConfig(level=logging.DEBUG)

load_dotenv()
dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(
    dsn=dsn,
    before_send=filter_sensitive_data,
    before_breadcrumb=filter_sensitive_breadcrumb_data,
    include_local_variables=True,
)

foo = 1
bar = 0
try:
    baz = foo / bar
except ZeroDivisionError as e:
    logging.exception(e)
    baz = 0

print(baz)
