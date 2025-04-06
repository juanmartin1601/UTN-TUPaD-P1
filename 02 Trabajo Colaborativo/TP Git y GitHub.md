# TP Git y GitHub

link repo ejercicio 2: git@github.com:juanmartin1601/ejercicio2-primeros-repos-utn.git  
link repo ejercicio 3: [git@github.com](mailto:git@github.com):juanmartin1601/conflict-exercise.git

Respuestas sobre Git y GitHub 

## ¿Qué es GitHub? 

GitHub es una plataforma basada en la web para alojar y gestionar código fuente utilizando   
Git como sistema de control de versiones. 

## ¿Cómo crear un repositorio en GitHub? 

1\. Iniciar sesión en GitHub   
2\. Hacer click en el botón "+" en la esquina superior derecha   
3\. Seleccionar "New repository"   
4\. Introducir un nombre y descripción   
5\. Eligir la visibilidad (público o privado)   
6\. Hacer click en "Create repository" 

## ¿Cómo crear una rama en Git? 

git branch nombre-de-la-rama 

## ¿Cómo cambiar a una rama en Git? 

git checkout nombre-de-la-rama 

## ¿Cómo fusionar ramas en Git? 

git checkout rama-destino   
git merge rama-origen 

## ¿Cómo crear un commit en Git? 

git add .   
git commit \-m "Mensaje descriptivo" 

## ¿Cómo enviar un commit a GitHub? 

git push origin nombre-de-la-rama 

## ¿Qué es un repositorio remoto? 

Un repositorio remoto es una versión del proyecto almacenada en un servidor en Internet,   
permitiendo la colaboración entre varios desarrolladores. 

## ¿Cómo agregar un repositorio remoto a Git? 

git remote add nombre-remoto URL-del-repositorio 

## ¿Cómo empujar cambios a un repositorio remoto? 

git push nombre-remoto nombre-de-la-rama 

## ¿Cómo tirar de cambios de un repositorio remoto? 

git pull nombre-remoto nombre-de-la-rama 

## ¿Qué es un fork de repositorio? 

Un fork es una copia de un repositorio ajeno en tu cuenta de GitHub, que te permite   
experimentar con cambios sin afectar el proyecto original. 

## ¿Cómo crear un fork de un repositorio? 

1\. Navegar al repositorio en GitHub   
2\. Hacer click en el botón "Fork" en la esquina superior derecha 

## ¿Cómo enviar una solicitud de extracción (pull request) 

## a un repositorio? 

1\. Ir a tu fork en GitHub   
2\. Hacer click en "Pull request"   
3\. Seleccionar la rama origen y destino   
4\. Añadir un título y descripción   
5\. Hacer click en "Create pull request" 

## ¿Cómo aceptar una solicitud de extracción? 

1\. Navegar a la sección "Pull requests" del repositorio   
2\. Hacer click en el pull request que deseamos aceptar   
3\. Revisar los cambios   
4\. Hacer click en "Merge pull request" 

## ¿Qué es una etiqueta en Git? 

Una etiqueta es un marcador que se asigna a un commit específico, generalmente para   
marcar versiones o lanzamientos importantes. 

## ¿Cómo crear una etiqueta en Git? 

git tag \-a v1.0 \-m "Versión 1.0" 

## ¿Cómo enviar una etiqueta a GitHub? 

git push origin v1.0  

## ¿Qué es un historial de Git? 

El historial de Git es el registro cronológico de todos los commits realizados en un   
repositorio. 

## ¿Cómo ver el historial de Git? 

git log 

## ¿Cómo buscar en el historial de Git? 

git log \--grep="término de búsqueda" 

## ¿Cómo borrar el historial de Git? 

git checkout \--orphan nueva-rama   
git add \-A   
git commit \-m "Commit inicial"   
git branch \-D main   
git branch \-m main   
git push \-f origin main 

## ¿Qué es un repositorio privado en GitHub? 

Un repositorio privado es visible solo para el propietario y los colaboradores que específicamente se inviten. 

## ¿Cómo crear un repositorio privado en GitHub? 

1\. Iniciar sesión en GitHub   
2\. Hacer clic en "+"   
3\. Seleccionar "New repository"   
4\. Introducir un nombre   
5\. Seleccionar "Private"   
6\. Hacer click en "Create repository" 

## ¿Cómo invitar a alguien a un repositorio privado en 

## GitHub? 

1\. entrar a nuestro repositorio  
2\. hacer click en "Settings"   
3\. Seleccionar "Collaborators"   
4\. hacer click en "Add people"   
5\. Introduccir el nombre de usuario o email 

## ¿Qué es un repositorio público en GitHub? 

Un repositorio público es visible para cualquier persona en Internet, quien puede ver y clonar el proyecto. 

## ¿Cómo crear un repositorio público en GitHub? 

1\. Iniciar sesión en GitHub   
2\. clickear en "+"   
3\. Seleccionar "New repository"   
4\. Introducir un nombre   
5\. Seleccionar "Public"   
6\. Hacer click en "Create repository" 

## ¿Cómo compartir un repositorio público en GitHub? 

Se comparte la URL del repositorio, que tendrá este formato:   
https://github.com/tu-usuario/nombre-del-repositorio