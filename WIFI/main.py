import subprocess

perfil_red = input('Introduce el nombre del perfil de red WiFi')

try:
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'],
                                         shell=True).decode('utf-8', errors='backslashreplace')
    if 'Contenido de la clave' in resultados:
        for line in resultados.split('\n'):
            if 'Contenido de la clave' in line:
                password = line.split(':')[1].strip()
                print(perfil_red, password)
                break
    else:
        print('No se a encontrado la contraseña')
except subprocess.CalledProcessError:
    print('No se a encontrado la informacion del perfil')