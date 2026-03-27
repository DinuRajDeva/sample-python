"""Core application logic."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


def run(name: str | None = None) -> int:
    """Run the app; prints a greeting. Returns exit code 0."""
    print(greet(name or "world"))
    return 0
