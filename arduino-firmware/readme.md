# Firmware Arduino Nano para La Pequeña Fábrica

Este repositorio contiene el firmware que usa cada uno de los brazos robotizados de la fábrica, escrito para placas Arduino Nano. Más abajo están las instrucciones para usar la interfaz por línea de comandos de Arduino, `arduino-cli`, la cual es muy útil para cargar el programa desde cada Raspberry Pi.


## Configurar `arduino-cli`

Para configurar el entorno de trabajo es necesario instalar `arduino-cli`, lo cual puede hacerse con tu gestor de paquetes favorito:
En linux:
```sh
sudo apt install arduino-cli
```

En Mac:
```sh
brew install arduino-cli
```

Luego, verificar que están disponibles las herramientas para las tarjetas Arduino con controladores AVR. Esto se realiza con el comando `core search`

```sh
arduino-cli core search
                                                                                                                             02:49:59
ID                    Version   Name                                                                                 
arduino:avr           1.8.4     Arduino AVR Boards                                                                   
arduino:mbed_edge     2.6.1     Arduino Mbed OS Edge Boards                                                          
arduino:mbed_nano     2.6.1     Arduino Mbed OS Nano Boards                                                          
arduino:mbed_nicla    2.6.1     Arduino Mbed OS Nicla Boards                                                         
arduino:mbed_portenta 2.6.1     Arduino Mbed OS Portenta Boards                                                      
arduino:mbed_rp2040   2.6.1     Arduino Mbed OS RP2040 Boards                                                        
...
```

Luego, se debe instalar las herramientas para tarjetas AVR:
```sh
arduino-cli core install arduino:avr
```
Para comprobar que la instalación está correcta se puede utilizar el comando `core list`:
```sh
arduino-cli core list
ID          Installed Latest Name                                      
arduino:avr 1.8.4     1.8.4  Arduino AVR Boards                        
```

Finalmente, para compilar el sketch es necesario navegar hasta esta carpeta y usar el comando `compile`, especificando la tarjeta `arduino:avr:nano`:

```sh
cd <path_to_mlf>/arduino-firmware
arduino-cli compile -b arduino:avr:nano
```

## Cargar un programa a la tarjeta