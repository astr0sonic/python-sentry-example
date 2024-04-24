import logging
import os

import sentry_sdk
from dotenv import load_dotenv

load_dotenv()
dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(dsn=dsn)

foo = "foo"
bar = "bar"
baz = foo + bar

sentry_sdk.capture_message(message="info message", level=logging.INFO)

a = 1
b = 0
try:
    c = a / b
except ZeroDivisionError as e:
    sentry_sdk.capture_exception(e)

sentry_sdk.capture_event(
    event={
        "message": "user finished",
        "level": "info",
        "extra": {"user_id": 123456, "username": "user"},
    },
)
