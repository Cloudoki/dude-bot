import pyvona
import sys
import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.cfg'

configParser.read(configFilePath)

v = pyvona.create_voice(configParser.get('main', 'access_key'), configParser.get('main', 'secret_key'))
v.speak(' '.join(sys.argv[1:]))
