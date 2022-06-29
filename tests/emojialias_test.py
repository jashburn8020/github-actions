import emojialias

def test_alias() -> None:
    assert emojialias.alias("👍") == ":thumbs_up:"
