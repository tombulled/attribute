import dataclasses
import types
import typing


@dataclasses.dataclass
class Stasher:
    attr: str = "__stash"
    container: typing.Callable = types.SimpleNamespace

    def __getitem__(self, obj: typing.Any, /) -> typing.Any:
        return getattr(obj, self.attr)

    def bind(self, obj: typing.Any, /) -> typing.Any:
        if not self.bound(obj):
            self.reset(obj)

        return self.get(obj)

    def reset(self, obj: typing.Any, /) -> typing.Any:
        self.set(obj, self.container())

        return self.get(obj)

    def set(self, obj: typing.Any, value: typing.Any, /) -> None:
        setattr(obj, self.attr, value)

    def get(self, obj: typing.Any, /) -> typing.Any:
        return getattr(obj, self.attr, None)

    def bound(self, obj: typing.Any, /) -> bool:
        return hasattr(obj, self.attr)
