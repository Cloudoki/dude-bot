import sys
import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.cfg'

configParser.read(configFilePath)

print configParser.get('main', sys.argv[1])
