# Dude-Bot

## Instalation

Make sure you have recording and python installed

    $ sudo apt-get install libav-tools portaudio19-dev python-setuptools easy_install pip

Download and Install [wolframAlpha python library](https://github.com/jaraco/wolframalpha)

    $ sudo python setup.py build

    $ sudo python setup.py

Install [pyvona](https://github.com/zbears/pyvona) and its dependencies

    $ sudo pip install pyvona requests pygame

Install virtualenv

    $ sudo apt-get install python-virtualenv


Get an [WolframAlpha API](http://products.wolframalpha.com/api/) APP-ID

Get an [IVONA Speech Cloud Account](https://www.ivona.com/us/for-business/speech-cloud/) and generate credentials: Access and Secret Key


Create configuration file `config.cfg` at project root

```
[main]
app_id = YOUR-APIKEYHERE
access_key = IVONA_ACCESS_KEY
secret_key = IVONA_SECRET_KEY
```

## Usage

Create a virtual environment and install pyramid.

    $ mkdir venv
    $ export VENV=path-to-your-dir/venv
    $ virtualenv --system-site-packages $VENV
    $ . $VENV/bin/activate
    $ $VENV/bin/pip install "pyramid==1.7.3"

## Run

    $ $VENV/bin/python api_dudebot.py

The app will start listening on port: `8080`.

## Resources

- [Raspberry Pi Voice Recognition Works Like Siri](https://oscarliang.com/raspberry-pi-voice-recognition-works-like-siri/)
- [Pyvona - A python wrapper for Amazon's IVONA API](http://zacharybears.com/pyvona/)
- [BEST VOICE RECOGNITION SOFTWARE FOR RASPBERRY PI](http://diyhacking.com/best-voice-recognition-software-for-raspberry-pi/)
