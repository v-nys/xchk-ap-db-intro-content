from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class DemoAPDBIntroView(ContentView):
     
    uid = 'xchk_ap_db_intro_demo'
    template = 'xchk_ap_db_intro/xchk_ap_db_intro_demo.html'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))
