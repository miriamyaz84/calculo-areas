# Calculadora de Áreas

Este proyecto está hecho en Python y sirve para calcular el área de tres figuras:  
- un cuadrado  
- un círculo  
- un triángulo  

Hay un archivo llamado `areas.py` donde se escribieron tres funciones que hacen estos cálculos.  
El programa también revisa que los números que pongamos (como el lado, radio o altura) no sean negativos. Si lo son, devuelve un resultado vacío para indicar que no es válido.

También se creó un archivo llamado `test_areas.py` donde se hacen pruebas para asegurarse de que todo funcione bien.

---

## ¿Cómo usar el proyecto?

1. Asegúrate de tener instalado **Python 3** en tu computadora.
2. Abre una terminal o consola dentro de la carpeta del proyecto.
3. Escribe el siguiente comando para ejecutar las pruebas:

```bash
python test_areas.py
```

Si todo está bien, verás que dice **OK** al final.

---

## ¿Cómo ver los avances guardados?

Usamos una herramienta llamada **Git** para ir guardando nuestro trabajo por partes.  
Si quieres ver cada avance guardado, abre la terminal en la carpeta del proyecto y escribe:

```bash
git log --oneline
```

Ahí verás una lista de cambios que hicimos, por ejemplo:

```
f4a8c9b Se añadieron pruebas unitarias para el módulo
2c27e3d Se implementó el módulo con funciones para calcular áreas
91b6dc8 Initial project setup
```

Para salir, solo presiona la tecla `q`.

---

## Reflexión final

**¿Fue útil escribir pruebas?**  
Sí, porque nos ayudaron a comprobar que el código funciona como debe. También nos ayudaron a darnos cuenta si algo estaba mal y corregirlo a tiempo.

**¿Cómo nos ayudó Git?**  
Git nos permitió guardar el trabajo por etapas. Así, si algo salía mal, podíamos volver a un punto anterior sin perder todo lo que habíamos hecho.

**¿Qué tan importante es la documentación?**  
La documentación es muy importante porque ayuda a que otras personas (o nosotros mismos en el futuro) entiendan cómo funciona el proyecto y cómo usarlo, sin tener que revisar todo el código.

---

## ¿Cómo usar la calculadora desde la terminal?

También puedes ejecutar un menú interactivo con el archivo `main.py`.  
Este archivo te muestra opciones para calcular el área de un cuadrado, un círculo o un triángulo desde la terminal.

### Para usarlo:
1. Abre una terminal en la carpeta del proyecto.
2. Escribe el siguiente comando:

```bash
python main.py
```

3. Verás un menú con opciones del 1 al 4.
   - Puedes elegir la figura que quieres calcular.
   - Luego escribes los datos que te pide (como el lado, radio, base o altura).
   - Si los datos son válidos, te mostrará el resultado.
   - Si escribes algo incorrecto, te mostrará un mensaje de error.

4. Si eliges la opción 4, el programa termina.

Este archivo es útil para probar el programa de forma más fácil, sin tener que escribir código.
