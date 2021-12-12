# imports
import dataclasses
import types
import modcall
import sys

# errors
class NoStashError(Exception): pass

# utils
def provide(value):
    def wrapper():
        return value

    return wrapper

def module(name: str):
    return sys.modules[name]

# sentinels
Missing = object()

# types
class Stash(types.SimpleNamespace): pass

@dataclasses.dataclass
class Stasher:
    attr: str = '__stash'

    def new(self, obj) -> None:
        if self.mounted(obj):
            raise Exception('Already mounted')

        setattr(obj, self.attr, Stash())

        return self.get(obj)

    def mounted(self, obj) -> bool:
        return hasattr(obj, self.attr)

    def get(self, obj, default = Missing):
        if default is Missing:
            if not hasattr(obj, self.attr):
                raise NoStashError(f'{obj} has no stash at attr {self.attr!r}')

            return getattr(obj, self.attr)

        return getattr(obj, self.attr, default)

_module = module(__name__)

stasher = Stasher()
stash = stasher.new(_module)

def get(obj = None):
    return stasher.get(obj) if obj is not None else stash

new = stasher.new

modcall(_module, get)