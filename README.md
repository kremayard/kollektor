<div align="center">
<h1>Kollektor</h1>
<p>Collection utility for Python.</p>
<p><i>This project is a part of Krema.</i></p>
<br>
</div>

## Documentation
Check [/docs/](https://github.com/kremayard/kollektor/tree/main/docs) folder for more information.
## Installation
Run `unikorn add kremayard kollektor` and you are ready to go!

## Example
```py
from unikorn import kollektor

collection = kollektor.Kollektor(2, 3, 4)

# Print Collection Length
print(collection.length)

# Add New Objects to the Collection
collection.append(1, 5, 6)

# Remove Object from Collection.
collection.remove(2)

# Print First & Last Object.
print(collection.first())
print(collection.last())

# Get all Items in the Collection
print(collection.items)
```