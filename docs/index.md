# Cifra de cesar

A idéia desse projeto é representar uma biblioteca capaz de executar a cifra de cesar (ROT13)

## Exemplos de uso

### Encriptação

```python
from cesar import encripta

encripta('Silverio')    # fvyirevb
```

### Decriptação
```python
from cesar import decripta

decripta('fvyirevb')    # Silverio
```

### Rotações diferentes de 13
```python
from cesar import decripta, encripta

encripta('Silverio')    # fvyirevb
decripta('fvyirevb', 14)    # Silverio
```

