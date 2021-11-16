from . import constants
from . import types

def get_stash(func_or_cls_or_obj):
    if not hasattr(func_or_cls_or_obj, constants.ATTRIBUTE):
        setattr(func_or_cls_or_obj, constants.ATTRIBUTE, types.Stash())

    return getattr(func_or_cls_or_obj, constants.ATTRIBUTE)
