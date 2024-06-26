import logging
import os

import sentry_sdk
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)

load_dotenv()
dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(dsn=dsn)

foo = 1
bar = 0

try:
    baz = foo / bar
except ZeroDivisionError:
    logging.exception("zero division", extra={"foo": foo, "bar": bar})
    baz = 0

print(baz)
