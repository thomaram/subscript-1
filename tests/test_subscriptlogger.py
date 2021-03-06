import subscript


def test_subscriptlogger():
    """Test that the subscript logger can compute a correct name for itself"""
    assert subscript.getLogger().name == "subscript"
    assert subscript.getLogger("").name == "subscript"
    assert subscript.getLogger("subscript.eclcompress").name == "subscript.eclcompress"
    assert (
        subscript.getLogger("subscript.eclcompress.eclcompress").name
        == "subscript.eclcompress"
    )
    assert (
        subscript.getLogger("subscript.eclcompress.eclcompress.eclcompress").name
        == "subscript.eclcompress"
    )
    assert (
        subscript.getLogger("subscript.eclcompress.eclcompress.somesubmodule").name
        == "subscript.eclcompress.somesubmodule"
    )
