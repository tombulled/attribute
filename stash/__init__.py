from .attributes import Attribute, DefaultedAttribute, Stasher

STASHER = Stasher()

get = STASHER.get
delete = STASHER.delete
has = STASHER.has
set = STASHER.set
reset = STASHER.reset
setdefault = STASHER.setdefault
