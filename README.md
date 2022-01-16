# stash
Stash data in objects

## Installation
```console
pip install git+https://github.com/tombulled/stash@main
```

## Usage

### Basic Stashing
```python
import stash

def foo():
    pass

my_stash = stash.bind(foo)

my_stash.message = 'Hello, World!'
```

```python
>>> stash.get(foo)
namespace(message='Hello, World!')
```

### Custom Stashing
```python
import stash

stasher = stash.Stasher(attr='__labels__', container=dict)

def foo():
    pass

labels = stasher.bind(foo)

labels['author'] = 'John Doe'
labels['deprecated'] = True
```

```python
>>> stasher.get(foo)
{'author': 'John Doe', 'deprecated': True}
```