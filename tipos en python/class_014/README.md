# Tipos en Python

Aunque Python es un lenguaje de tipado dinámico, podemos aportar información de tipo a variables y funciones.

Esto permite impedir ciertos errores que han ocurrido en nuestro código, como pasar un `int` a un función que se esperaba un `str`.


El tipado estático y el tipado dinámico se refieren a cuándo se verifica el tipo de una variable en un lenguaje de programación.

**Tipado Estático**

En un lenguaje de programación de tipado estático, el tipo de una variable se verifica en tiempo de compilación. Una vez que una variable ha sido declarada con un tipo, no puedes cambiarla a otro tipo más adelante. Los errores de tipo se detectan antes de que el programa se ejecute. Ejemplos de lenguajes de tipado estático son C++, Java y Rust.

**Tipado Dinámico**

Por otro lado, en un lenguaje de programación de tipado dinámico, el tipo se verifica en tiempo de ejecución y puedes cambiar el tipo de una variable en cualquier momento. Los errores de tipo solo se detectarán cuando el programa se ejecute. Python, Ruby y JavaScript son ejemplos de lenguajes de tipado dinámico.

Por ejemplo, en Python (tipado dinámico) puedes hacer esto:

```python
x = 5  # x es un entero
x = "hello"  # ahora x es una cadena
```

Pero en Java (tipado estático), hacer algo similar daría lugar a un error de compilación:

```java
int x = 5;  // x es un entero
x = "hello";  // Error de compilación
```

Cada enfoque tiene sus pros y contras. El tipado estático puede ayudar a prevenir errores de tipo y puede hacer que el código sea más autoexplicativo, pero puede ser más verboso. El tipado dinámico puede hacer que el código sea más flexible y conciso, pero puedes encontrar errores de tipo solo cuando el código se ejecuta.


**Lo mejor de cada mundo**

En las nuevas versiones de Python, podemos combinar ambas cosas y tener lo mejor de cada mundo.