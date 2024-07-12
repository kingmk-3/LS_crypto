# `Project 1 : Hill cipher`

## Description of the function in the project.py:

### First of all suffient commenting is there

### Modes: `I have create 4 modes, 1 : for encryption, 2 : key discovery, 3 : all key discovery, 4 : exit`

### Besides this script also ask everytime whether or not you want to change the key

### The difference between mode 2 and 3 is that 2 just returns only one key from the solution space

## Concept for Key discover:

### Juts the basic linear algebra, was used. First we know that

    \[ K.P =C \]
    that means,
    \[ P^{T}.K^{T}=C^{T} \]
    So we find the solution space for each of the column \(K^{T}\)
    Then take those combination of coloumn that result in invertible matrix \(K\)
