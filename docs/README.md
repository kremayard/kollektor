<a name="kollektor"></a>

# kollektor

Collection utility for Python.

<a name="kollektor.Kollektor"></a>

## Kollektor Objects

```python
class Kollektor(object)
```

Base class for kollektor.

<a name="kollektor.Kollektor.__init__"></a>

#### \_\_init\_\_

```python
__init__(*args: Any) -> None
```

Construct a new 'Kollektor' object.

**Parameters**:

- `*args`: items for collection.

<a name="kollektor.Kollektor.length"></a>

#### length

```python
@property
length() -> int
```

Get collection length.

**Returns**:

- `int`: Collection length.

<a name="kollektor.Kollektor.find"></a>

#### find

```python
find(item: Any) -> Union[Any, Nothing]
```

Find an object from collection.

**Parameters**:

- item (`Any`): The item will be found.

**Returns**:

- `Any`: Found object.
- `kollektor.Nothing`

<a name="kollektor.Kollektor.has"></a>

#### has

```python
has(item: Any) -> bool
```

Check an object is in collection.

**Parameters**:

- item (`Any`): The item will be checked.

**Returns**:

- `bool`: True or False

<a name="kollektor.Kollektor.append"></a>

#### append

```python
append(*args: Any) -> tuple
```

Append one or more object to the collection.

**Parameters**:

- `*args`: The item(s) will be added.

**Returns**:

- `tuple`: Added items.

<a name="kollektor.Kollektor.remove"></a>

#### remove

```python
remove(*args: Any) -> tuple
```

Remove one or more object from the collection.

**Parameters**:

- `*args`: The item(s) will be removed.

**Returns**:

- `tuple`: New items.

<a name="kollektor.Kollektor.first"></a>

#### first

```python
first() -> Union[Any, Nothing]
```

Get first element from the collection.

**Returns**:

- `Any`: object.
- `kollektor.Nothing`

<a name="kollektor.Kollektor.last"></a>

#### last

```python
last() -> Union[Any, Nothing]
```

Get last element from the collection.

**Returns**:

- `Any`: object.
- `kollektor.Nothing`

<a name="kollektor.Kollektor.index"></a>

#### index

```python
index(index: int) -> Union[Any, Nothing]
```

Find an object from collection with index.

**Returns**:

- `Any`: object.
- `kollektor.Nothing`

<a name="kollektor.Kollektor.filter"></a>

#### filter

```python
filter(fn: Callable) -> tuple
```

Filter objects from collection.

**Returns**:

- `tuple`: Filtered object(s).

<a name="kollektor.Kollektor.each"></a>

#### each

```python
each(fn: Callable) -> list
```

Iterate objects from collection.

**Returns**:

- `list`: List of returned values.

<a name="kollektor.classes"></a>

# kollektor.classes

<a name="kollektor.classes.Nothing"></a>

## Nothing Objects

```python
class Nothing()
```

None-Type replacement for Kollektor.
