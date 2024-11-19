# Class Inheritance

## Learning Goals

- Inheritance

- The super method

## Exercises

### Inheritance

1. Make the `Dog` class inherit from `Mammal` (be sure to import!)

2. Amend the `__init__` method for Dog so it properly utilizes the `super` method.

3. Amend the `__repr__` method so it makes sense with the new attributes from `Mammal`.

4. Change the behavior for the `make_sound` method in `Dog` so it returns something that makes more sense. You will not need to use `super`.

5. Change the `sleep` and `run_around` methods for `Dog` so that they use the `super` keyword. Add additional dog-centric behavior to the methods (for example print or return something new that gives us an idea of what the `Dog` instance is doing).