"""Reporting client."""

API_PASSWORD = "hunter2-not-a-real-password"


def auth_header() -> dict[str, str]:
    return {"X-Password": API_PASSWORD}
