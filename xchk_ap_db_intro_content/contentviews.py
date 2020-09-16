from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class DatatypesSimpeleTekstView(ContentView):
    uid = 'xchk_ap_db_intro_content_datatypes_simpele_tekst'
    title = 'datatypes: simpele tekst'
    template = 'xchk_ap_db_intro_content/datatypes_simpele_tekst.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class BasisstructurenVanEenRelationeleDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_basisstructuren_van_een_relationele_database'
    title = 'Basisstructuren van een relationele database'
    template = 'xchk_ap_db_intro_content/basisstructuren_van_een_relationele_database.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class LokaleVsRemoteDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_lokale_vs_remote_database'
    title = 'Lokale vs. remote database'
    template = 'xchk_ap_db_intro_content/lokale_vs_remote_database.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class VoordelenVanEenDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_voordelen_van_een_database'
    title = 'Voordelen van een database'
    template = 'xchk_ap_db_intro_content/voordelen_van_een_database.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class SubtalenVanMySqlView(ContentView):
    uid = 'xchk_ap_db_intro_content_subtalen_van_my_sql'
    title = 'subtalen van (My)SQL'
    template = 'xchk_ap_db_intro_content/subtalen_van_my_sql.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class InstallatieTeamviewerView(ContentView):
    uid = 'xchk_ap_db_intro_content_installatie_teamviewer'
    title = 'installatie TeamViewer'
    template = 'xchk_ap_db_intro_content/installatie_teamviewer.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class DiagramnotatieTabelView(ContentView):
    uid = 'xchk_ap_db_intro_content_diagramnotatie_tabel'
    title = 'diagramnotatie tabel'
    template = 'xchk_ap_db_intro_content/diagramnotatie_tabel.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class AlleAfsprakenView(ContentView):
    uid = 'xchk_ap_db_intro_content_alle_afspraken'
    title = 'alle afspraken'
    template = 'xchk_ap_db_intro_content/alle_afspraken.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class VoorbeeldVanEenRelationeleDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_voorbeeld_van_een_relationele_database'
    title = 'Voorbeeld van een relationele database'
    template = 'xchk_ap_db_intro_content/voorbeeld_van_een_relationele_database.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class InstallatieDockerView(ContentView):
    uid = 'xchk_ap_db_intro_content_installatie_docker'
    title = 'installatie Docker'
    template = 'xchk_ap_db_intro_content/installatie_docker.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class MysqlWorkbenchEnCliInstallerenView(ContentView):
    uid = 'xchk_ap_db_intro_content_mysql_workbench_en_cli_installeren'
    title = 'MySQL Workbench en CLI installeren'
    template = 'xchk_ap_db_intro_content/mysql_workbench_en_cli_installeren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WatIsEenDatabankView(ContentView):
    uid = 'xchk_ap_db_intro_content_wat_is_een_databank'
    title = 'Wat is een databank'
    template = 'xchk_ap_db_intro_content/wat_is_een_databank.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class VerbindenMetEenLokaleDatabaseServerViaWorkbenchView(ContentView):
    uid = 'xchk_ap_db_intro_content_verbinden_met_een_lokale_database_server_via_workbench'
    title = 'Verbinden met een lokale database server via Workbench'
    template = 'xchk_ap_db_intro_content/verbinden_met_een_lokale_database_server_via_workbench.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CreateStatementView(ContentView):
    uid = 'xchk_ap_db_intro_content_create_statement'
    title = 'CREATE statement'
    template = 'xchk_ap_db_intro_content/create_statement.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class MysqlDockerImageView(ContentView):
    uid = 'xchk_ap_db_intro_content_mysql_docker_image'
    title = 'MySQL Docker image'
    template = 'xchk_ap_db_intro_content/mysql_docker_image.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class DatatypesGeheleGetallenView(ContentView):
    uid = 'xchk_ap_db_intro_content_datatypes_gehele_getallen'
    title = 'datatypes: gehele getallen'
    template = 'xchk_ap_db_intro_content/datatypes_gehele_getallen.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WatIsDockerView(ContentView):
    uid = 'xchk_ap_db_intro_content_wat_is_docker'
    title = 'Wat is Docker?'
    template = 'xchk_ap_db_intro_content/wat_is_docker.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class VerbindenMetDeDatabaseServerViaWorkbenchView(ContentView):
    uid = 'xchk_ap_db_intro_content_verbinden_met_de_database_server_via_workbench'
    title = 'Verbinden met de database server via Workbench'
    template = 'xchk_ap_db_intro_content/verbinden_met_de_database_server_via_workbench.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WatIsMysqlView(ContentView):
    uid = 'xchk_ap_db_intro_content_wat_is_mysql'
    title = 'Wat is MySQL?'
    template = 'xchk_ap_db_intro_content/wat_is_mysql.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WelkeSoortenDatabasesBestaanErNogView(ContentView):
    uid = 'xchk_ap_db_intro_content_welke_soorten_databases_bestaan_er_nog'
    title = 'Welke soorten databases bestaan er nog?'
    template = 'xchk_ap_db_intro_content/welke_soorten_databases_bestaan_er_nog.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WatIsEenRelationeleDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_wat_is_een_relationele_database'
    title = 'Wat is een relationele database?'
    template = 'xchk_ap_db_intro_content/wat_is_een_relationele_database.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class DatabaseSelecterenView(ContentView):
    uid = 'xchk_ap_db_intro_content_database_selecteren'
    title = 'database selecteren'
    template = 'xchk_ap_db_intro_content/database_selecteren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))
