# Pico Dinosaur Game

A [Chrome offline dinosaur](chrome://dino/) game implemented on a Pi Pico with a P5 display and push button.


## Initial setup

### Python venv
1. Install `python3`
2. Create a virtualenv using `python -m venv .venv`
3. Activate the virtualenv using `.\.venv\Scripts\Activate.ps1`
4. Install the requirements using `pip install -r host-requirements.txt`


### CircuitPython deps
```shell
circup install -r device-requirements.txt
```


## Creating graphic assets

You can use [Piskel](https://www.piskelapp.com/) and import the BMP files to edit them.

For simplicity, they are saved as 256 color Bitmap in MS Paint. This results in green (usually) being index 250 in the palette and we make this transparent by fixed index in the code.

