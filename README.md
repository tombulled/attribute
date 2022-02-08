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

my_stash = stash.setdefault(foo)

my_stash.message = 'Hello, World!'
```

```python
>>> stash.get(foo)
namespace(message='Hello, World!')
```

### Custom Stashing
```python
import stash

stasher = stash.Stasher('_labels_', factory=dict)

def foo():
    pass

labels = stasher.setdefault(foo)

labels['author'] = 'John Doe'
labels['deprecated'] = True
```

```python
>>> stasher.get(foo)
{'author': 'John Doe', 'deprecated': True}
```