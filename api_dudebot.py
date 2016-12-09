import os
import logging
import pyvona
import wolframalpha
import ConfigParser
import random

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from wsgiref.simple_server import make_server

# setup logging
logging.basicConfig()
log = logging.getLogger(__file__)

# get configuration
configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.cfg'
configParser.read(configFilePath)

app_id = configParser.get('main', 'app_id')
access_key = configParser.get('main', 'access_key')
secret_key = configParser.get('main', 'secret_key')


# available commands
commands = { "commands" : { "question" : \
                            ['question', 'questions', 'pergunta', 'questao']}}

# greetings
greetings = ["Sire?", "One is glad to be of service!", \
             "How can I help?", "What is it!?! Can't you see I'm busy?", \
             "WHAT???"]

# setup pyvona voice
voice = pyvona.create_voice(access_key, secret_key)
voice.voice_name="Brian"
voice.language="en-GB"
voice.gender="Male"

# setup wolfram alpha
wa = wolframalpha.Client(app_id)

# app setup
port = 8080


def speak(text):
    voice.speak(text)

# views
@view_config(
    route_name='ping',
    request_method=('GET'),
    renderer='json'
)
def ping(request):
    return {"message": "pong"}


# views
@view_config(
    route_name='trigger',
    request_method=('GET'),
    renderer='json'
)
def listen(request):
    greet = random.choice(greetings)
    log.info(greet)
    speak(greet)
    return {"message": "triggered"}


@view_config(
    route_name='commands',
    request_method=('GET'),
    renderer='json'
)
def get_commands(request):
    return commands


@view_config(
    route_name='execute',
    request_method=('POST'),
    renderer='json'
)
def execute_command(request):
    data = request.json_body
    log.info(data)
    result = ""
    if data.command and data.command == 'question':
        res = wa.query(data.message)
        for pod in res.pods:
            for sub in pod.subpods:
                result += sub.text + "\n"
    return {"message": result}


@view_config(
    context='pyramid.exceptions.NotFound',
    renderer='json'
)
def notfound_view(request):
    request.response.status = '404 Not Found'
    return { "code" : 404, "message" : 'Not Found'}


if __name__ == '__main__':
    log.info("App listening at port %d" % port)
    # configurations settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all']  = True
    # configuration setup
    config = Configurator(settings=settings)
    # routes setup
    config.add_route('ping', '/ping')
    config.add_route('trigger', '/trigger')
    config.add_route('commands', '/commands')
    config.add_route('execute', '/execute')
    # scan for @view_config decorators
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
