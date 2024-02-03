
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

<!-- Referencias -->
[devcontainer]: https://code.visualstudio.com/docs/remote/containers
[devcontainersext]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
[git]: https://git-scm.com/
[knkillname]: https://www.knkillname.org/
[uaem]: http://www.uaem.mx
[ubuntu]: https://ubuntu.com/tutorials/install-ubuntu-desktop
[vscode]: https://code.visualstudio.com
[wsl2]: https://docs.microsoft.com/es-mx/windows/wsl/install
