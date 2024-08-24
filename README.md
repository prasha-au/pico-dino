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

Piskel can export to PNG and you can use the command below (on OSX) to convert it to BMP.

```bash
sips -s format jpeg test.png --out test.jpg
```


