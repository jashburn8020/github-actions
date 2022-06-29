"""Return some literal stuff."""

from emoji import demojize

def alias(emoji: str) -> str:
    """Return the alias of an emoji."""
    return demojize(emoji)
