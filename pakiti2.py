from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE

from subprocess import call

requires_api_version = '2.3'
plugin_type = (TYPE_CORE, TYPE_INTERACTIVE)

def posttrans_hook(conduit):
    conduit.info(2, 'Calling pakiti2-client')
    try:
        call(['/usr/sbin/pakiti2-client'])
    except OSError:
        conduit.info(2, 'Something went wrong, OSError caught while calling pakiti2-client')
