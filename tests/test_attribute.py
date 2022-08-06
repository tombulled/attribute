from typing import Any, Callable

import attribute
import pytest


@pytest.fixture
def default() -> Any:
    return "default"


@pytest.fixture
def default_factory() -> Callable:
    return dict


@pytest.fixture
def value() -> Any:
    return "value"


@pytest.fixture
def present(default) -> attribute.Attribute:
    return attribute.Attribute("present", default=default)


@pytest.fixture
def missing(default) -> attribute.Attribute:
    return attribute.Attribute("missing", default=default)


@pytest.fixture
def obj() -> object:
    class Cls:
        present = "present"

    return Cls


def test_get_item(
    obj: object, missing: attribute.Attribute, present: attribute.Attribute
) -> None:
    assert present[obj] == getattr(obj, present.name)

    with pytest.raises(AttributeError):
        missing[obj]


def test_default(default: Any) -> None:
    assert attribute.Attribute("foo", default=default).default == default


def test_default_factory(default_factory) -> None:
    assert (
        attribute.Attribute("foo", default_factory=default_factory).default
        == default_factory()
    )


def test_default_and_default_factory_specified(default, default_factory) -> None:
    with pytest.raises(ValueError):
        attribute.Attribute("foo", default=default, default_factory=default_factory)


def test_get(
    obj: object,
    missing: attribute.Attribute,
    present: attribute.Attribute,
    default: Any,
) -> None:
    assert present.get(obj) == getattr(obj, present.name)
    assert missing.get(obj) == default


def test_delete(obj: object, present: attribute.Attribute, default: Any) -> None:
    present.delete(obj)

    assert present.get(obj) == default


def test_has(
    obj: object, missing: attribute.Attribute, present: attribute.Attribute
) -> None:
    assert present.has(obj) is True
    assert missing.has(obj) is False


def test_set(obj: object, missing: attribute.Attribute, value: Any) -> None:
    missing.set(obj, value)

    assert missing.get(obj) == value


def test_setdefault_missing(
    obj: object, missing: attribute.Attribute, value: Any
) -> None:
    missing.setdefault(obj, value)

    assert missing.get(obj) == value


def test_setdefault_present(obj: object, present: attribute.Attribute) -> None:
    value: Any = present.get(obj)

    present.setdefault(obj, "new-value")

    assert present.get(obj) == value
