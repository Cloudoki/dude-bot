# Dude-Bot

## Instalation

Make sure you have recording and python installed

    $ sudo apt-get install libav-tools portaudio19-dev python-setuptools easy_install pip

Download and Install [wolframAlpha python library](https://github.com/jaraco/wolframalpha)

    $ sudo python setup.py build

    $ sudo python setup.py

Install [pyvona](https://github.com/zbears/pyvona) and its dependencies

    $ sudo pip install pyvona requests pygame

Make sure scripts are executable

    $ chmod +x \*.sh \*\*/\*.sh

Get an [WolframAlpha API](http://products.wolframalpha.com/api/) APP-ID

Get an [IVONA Speech Cloud Account](https://www.ivona.com/us/for-business/speech-cloud/) and generate credentials: Access and Secret Key

Use a google speech v2 [Developers Console](https://console.developers.google.com/apis/library) - [api-keys](http://www.chromium.org/developers/how-tos/api-keys),

NOTICE: Google has recently launched Cloud Google Speech.

Create configuration file `config.cfg` at project root

```
[main]
app_id = YOUR-APIKEYHERE
access_key = IVONA_ACCESS_KEY
secret_key = IVONA_SECRET_KEY
speech_key = GOOGLE_SPEECH_KEY
```

## Usage

    $ ./main.sh

## Resources

- [Raspberry Pi Voice Recognition Works Like Siri](https://oscarliang.com/raspberry-pi-voice-recognition-works-like-siri/)
- [Pyvona - A python wrapper for Amazon's IVONA API](http://zacharybears.com/pyvona/)
- [BEST VOICE RECOGNITION SOFTWARE FOR RASPBERRY PI](http://diyhacking.com/best-voice-recognition-software-for-raspberry-pi/)
