# stash
Stash data in objects

## Usage
```python
>>> import stash
>>>
>>> # stash's stash
>>> stash.stash
Stash()
>>> stash.stash.foo = 'bar'
>>> stash.stash
Stash(foo='bar')
>>>
>>> # create stashes
>>> import sys
>>> s = stash.new(sys)
>>> s
Stash()
>>> s.name = 'Sam'
>>> s
Stash(name='Sam')
```