
# uaem.notas.prodimag

[*Dr. Mario Abarca*][knkillname]

Notas del curso *Procesamiento Digital de Imágenes* de la
[Universidad Autónoma del Estado de Morelos][uaem].
Las notas están escritas en formato *Jupyter Notebook* y se encuentran en el
directorio `notas`.
Para abrir y ejecutar las notas, sigue las instrucciones en la sección
[*Inicio rápido*](#inicio-rápido).

## Inicio rápido

La forma canónica de usar este repositorio es a través de
[Visual Studio Code][vscode] con la extensión
[Dev Containers][devcontainersext].
Revisa la documentación de Microsoft
[*Developing inside a Container*][devcontainer] para obtener instrucciones
detalladas.
Asimismo es recomendable que tengas instalado [git][git] para clonar y mantener
actualizado el repositorio.

### Instrucciones para usuarios de Windows

Borra Windows y [instala Ubuntu][ubuntu]; o si lo prefieres, instala el
[Subsistema de Windows para Linux (WSL)][wsl2] y sigue las instrucciones para
usuarios de Ubuntu.

1. Localiza *Símbolo del sistema* en el menú de inicio.
2. Haz clic secundario sobre el icono y selecciona *Ejecutar como
   administrador*.
3. Ejecuta el siguiente comando para obtener el subsistema de Windows para
   Linux:

   ```cmd
   wsl --install
   ```

### Instrucciones para usuarios de Ubuntu

1. Puedes instalar *Visual Studio Code* descargando el paquete `.deb` desde la
   [página oficial][vscode] o usando los siguientes comandos en la terminal:

   ```bash
   wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

   sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

   sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

   rm -f packages.microsoft.gpg
   
   sudo apt update && sudo apt install code
   ```

2. Instala *git*, *Docker* y otras herramientas de desarrollo esenciales:

   ```bash
   sudo apt install build-essential git docker-compose-v2 docker-buildx

   sudo usermod -aG docker $USER

   reboot  # Esto reiniciará tu computadora
   ```

3. Instala la extensión *Dev Containers* desde la tienda de extensiones de
   *Visual Studio Code*, o bien, ejecutando el siguiente comando:

   ```bash
    code --install-extension ms-vscode-remote.remote-containers
    ```

4. Clona el repositorio:

   ```bash
   git clone https://github.com/knkillname/uaem.notas.prodimag
    ```

5. Abre el directorio del repositorio con *Visual Studio Code*:

   ```bash
   code uaem.notas.prodimag
   ```

## Preguntas frecuentes

### ¿Cómo puedo abrir y ejecutar las notas?

1. Abre el directorio del repositorio con *Visual Studio Code*.
2. *Visual Studio Code* detectará que el directorio contiene un archivo
   `devcontainer.json` y te preguntará si deseas abrir el directorio en un
   contenedor. Haz clic en *Reopen in Container*.
3. *Visual Studio Code* abrirá una nueva ventana con el directorio montado en un
   contenedor de Docker. La *primera vez* que hagas esto, *Visual Studio Code*
   descargará la imagen del contenedor, instalará las dependencias y abrirá un
   terminal en el contenedor; este proceso puede tardar varios minutos.
4. Abre el directorio `notas` y haz clic en el capítulo que desees abrir.

### ¿Cómo puedo actualizar las notas?

Suponiendo que ya tienes el repositorio clonado con *git* tal como se indica en
[Inicio rápido](#inicio-rápido), puedes actualizar las notas mediante dos sopas:

- **Sopa 1** (Interfaz gráfica):
  1. Abre el directorio del repositorio con *Visual Studio Code*.
  2. En la barra de estado encontrarás el botón de *Sincronizar cambios*; tiene
   un aspecto similar a dos flechas circulares 🗘.
  3. Haz clic en el botón y *Visual Studio Code* se encargará de actualizar el
   repositorio.

- **Sopa 2** (Línea de comandos):
   1. Abre una terminal en el directorio del repositorio.
   2. Ejecuta el siguiente comando:

       ```bash
       git pull
       ```

### ¿Cómo puedo ejecutar las notas sin *Visual Studio Code*?

Si no deseas usar *Visual Studio Code* o si tienes problemas con el contenedor,
puedes ejecutar las notas en tu sistema local. Para ello, a lo mínimo
necesitarás tener instalado *Python* 3.11 con acceso a *pip*.

1. Asegúrate de tener instalado *pipenv*. Si la sentencia `pipenv --version`
   devuelve un error, instala *pipenv* con el siguiente comando:

      ```bash
      pip install --user pipenv
      ```

      Si este comando no funciona, prueba con
      `python3 -m pip install --user pipenv`.
2. Abre una terminal en el directorio `notas` y ejecuta el siguiente comando:

   ```bash
   pipenv install --dev
   ```

   Esta sentencia instalará todas las dependencias necesarias para ejecutar las
   notas, incluyendo *Jupyter Lab*.
3. Ejecuta el siguiente comando para abrir *Jupyter Lab*:

   ```bash
   pipenv run jupyter lab
   ```

Por favor nota que no me hago responsable de que el formato de las notas sea
distinto al esperado si decides ejecutarlas en otro entorno que no sea el
contenedor de *Visual Studio Code*.

### ¿Cómo puedo contribuir?

Si encuentras un error en las notas o si deseas agregar contenido, puedes
hacerlo de la siguiente manera:

1. Crea una rama local en tu repositorio. En Visual Studio Code, haz clic en el
   icono de la rama en la barra de estado (usualmente dice `main`) y selecciona
   *Create new branch*.
2. Escribe un nombre descriptivo para la rama que refleje el cambio que
   realizarás, por ejemplo *Nota sobre la transformada de Fourier*.
3. Haz los cambios necesarios en las notas.
4. Guarda cada cambio mediante un *commit* con un mensaje descriptivo, usando
   las palabras *agregar*, *corregir*, o *eliminar* según sea el caso.
5. Una vez que hayas terminado, haz clic en el icono de la rama en la barra de
   estado y selecciona *Push*.
6. Finalmente, en GitHub, haz clic en el botón *Compare & pull request* y sigue
   las instrucciones para solicitar que tus cambios sean integrados en la rama
   principal.

<!-- Referencias -->
[devcontainer]: https://code.visualstudio.com/docs/remote/containers
[devcontainersext]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
[git]: https://git-scm.com/
[knkillname]: https://www.knkillname.org/
[uaem]: http://www.uaem.mx
[ubuntu]: https://ubuntu.com/tutorials/install-ubuntu-desktop
[vscode]: https://code.visualstudio.com
[wsl2]: https://docs.microsoft.com/es-mx/windows/wsl/install
