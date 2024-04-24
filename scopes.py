import os

import sentry_sdk
from dotenv import load_dotenv

load_dotenv()
dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(dsn=dsn)
print(sentry_sdk.Hub.current._stack)

with sentry_sdk.configure_scope() as scope:
    print(sentry_sdk.Hub.current._stack)
    scope.set_tag("scope1", "configure_scope")
    sentry_sdk.capture_message("before_configure_scope")  # scope1:configure_scope

with sentry_sdk.push_scope() as scope:
    print(sentry_sdk.Hub.current._stack)
    scope.set_tag("scope2", "push_scope")
    sentry_sdk.capture_message("push_scope")  # scope1:configure_scope scope2:push_scope

with sentry_sdk.configure_scope() as scope:
    print(sentry_sdk.Hub.current._stack)
    scope.set_tag("scope3", "configure_scope")
    sentry_sdk.capture_message(
        "after_configure_scope"
    )  # scope1:configure_scope scope3:configure_scope
