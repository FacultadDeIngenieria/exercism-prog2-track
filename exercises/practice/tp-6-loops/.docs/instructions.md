Dada la siguiente consigna, implementar y lograr imprimir en pantalla el output esperado.

Para la primera parte, hacer una función llamada **enumerate_list** que dada una lista de Strings, retorne una nueva lista y en cada elemento agregar su número de índice, un punto, un tabulado (\t) y el valor String. Si el arreglo tiene strings vacíos no debe mostrar nada, ni el elemento correspondiente en la lista.

```python
colors = ["Red", "Green", "", "White", "Black"]
enumerate_list(colors)
#retorna la lista:
# ["0.  Red","1.  Green", "2.  White", "3.  Black"]
```

Para la segunda parte, hacer un método llamado **enumerate_backwards** que dado una lista de Strings, returne una nueva lista, al igual que en enumerate_list, pero cada palabra deberia estas escrita a la inversa. Si el arreglo tiene Strings vacíos se deben saltear esos elementos de la nueva lista.

```python
colors = ["Red", "Green", "", "White", "Black"]
enumerate_backwards(colors)
#retorna la lista:
# ["0. deR", "1. neerG", "2. etihW", "3. kcalB"]  
```