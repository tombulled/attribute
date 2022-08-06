# attribute
Attribute management made easy

## Installation
```console
pip install git+https://github.com/tombulled/attribute@main
```

## Usage
### Custom Attribute
```python
from attribute import Attribute

class Foo:
    bar: str = "hello!"
```
```python
>>> bar = Attribute("bar")
>>> bar.get(Foo)
"hello!"
```

### Bundled Attribute
```python
import attribute

class Foo:
    pass
```
```python
>>> attribute.name.get(Foo)
"Foo"
```