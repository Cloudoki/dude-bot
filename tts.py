import pyvona
import sys
import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.cfg'

configParser.read(configFilePath)

v = pyvona.create_voice(configParser.get('main', 'access_key'), configParser.get('main', 'secret_key'))
v.voice_name="Nicole"
v.language="en-AU"
v.gender="Female"
v.speak(' '.join(sys.argv[1:]))
