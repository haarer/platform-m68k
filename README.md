# Motorola 68K: development platform for [PlatformIO](http://platformio.org)

Motorola (now Freescale M68K processors are still used in embedded development in certain industries. The are widely known by their use in amiga, apple and atari home computers.


![alt text](https://github.com/haarer/platform-m68k/workflows/Examples/badge.svg "Atmel AVR development platform")

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:


```ini

platform = https://github.com/haarer/platform-m68k.git
board = GenericM68332
...
```

