import os

import sentry_sdk
import sentry_sdk.scope
from dotenv import load_dotenv

load_dotenv()
dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(dsn=dsn)

scope = sentry_sdk.scope.Scope.get_current_scope()
scope.set_tag("scope1", "scope1")
sentry_sdk.capture_message("message1")  # scope1:scope1

with sentry_sdk.new_scope() as scope:
    scope.set_tag("scope2", "scope2")
    sentry_sdk.capture_message("message2")  # scope1:scope1 scope2:scope2

scope.set_tag("scope3", "scope3")
sentry_sdk.capture_message("message3")  # scope1:scope1 scope3:scope3
