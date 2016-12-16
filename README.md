# Dude-Bot

## Instalation

Make sure you have recording and python installed

    $ sudo apt-get install libav-tools portaudio19-dev python-setuptools easy_install pip

Install [pyvona](https://github.com/zbears/pyvona) and its dependencies

    $ sudo pip install pyvona requests pygame

Install virtualenv

    $ sudo apt-get install python-virtualenv


[optional] (see Usage)

Download and Install [wolframAlpha python library](https://github.com/jaraco/wolframalpha)

    $ sudo python setup.py build

    $ sudo python setup.py

Get an [WolframAlpha API](http://products.wolframalpha.com/api/) APP-ID

Get an [IVONA Speech Cloud Account](https://www.ivona.com/us/for-business/speech-cloud/) and generate credentials: Access and Secret Key


Create configuration file `config.cfg` at project root

```
[main]
app_id = YOUR-APIKEYHERE
access_key = IVONA_ACCESS_KEY
secret_key = IVONA_SECRET_KEY
```

Edit the bot configuration file `bot_config.json` at project root

```
{
	"triggers": ['dude', 'hey dude', 'hey mate', 'ok dude', 'okay dude'],
	"greetings": ["Sire?", "One is glad to be of service!", "How can I help?", "What is it!?! Can't you see I'm busy?", "WHAT???"],
	"voice": {"voice_name": "Brian", "language": "en-GB", "gender": "Male"}
}
```

- **triggers**: the triggers that "wake" the bot
- **grettings**: the bot responses to being woken
- **voice**: the voice configuration from ivona

## Usage

Create a virtual environment and install wolframalpha (if you didn't before) and pyramid.

    $ mkdir venv
    $ export VENV=path-to-your-dir/venv
    $ virtualenv --system-site-packages $VENV
    $ . $VENV/bin/activate
    $ $VENV/bin/pip install wolframalpha
    $ $VENV/bin/pip install "pyramid==1.7.3"

## Run

    $ $VENV/bin/python api_dudebot.py

The app will start listening on port: `8080`.

## Resources

- [Raspberry Pi Voice Recognition Works Like Siri](https://oscarliang.com/raspberry-pi-voice-recognition-works-like-siri/)
- [Pyvona - A python wrapper for Amazon's IVONA API](http://zacharybears.com/pyvona/)
- [BEST VOICE RECOGNITION SOFTWARE FOR RASPBERRY PI](http://diyhacking.com/best-voice-recognition-software-for-raspberry-pi/)
