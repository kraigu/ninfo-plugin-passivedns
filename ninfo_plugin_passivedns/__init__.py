from ninfo import PluginBase

class passivedns_plug(PluginBase):
    """This plugin returns any hostnames seen to resolve to this ip"""

    name = "passivedns"
    title = "Passive DNS"
    description = "Passive DNS"
    cache_timeout = 60*10
    #partial ipv6 addresses currently get typed as usernames, needs to be fixed
    types = ['ip', 'ip6', 'hostname','username']

    def setup(self):
        from passive_dns import client
        self.c=client.SearchClient()

    def get_info(self, arg):
        info = self.c.search(arg)
        return {'records':info}

plugin_class = passivedns_plug
