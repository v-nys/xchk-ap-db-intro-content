from xchk_core.contentviews import ContentView
from xchk_core.strats import *
from xchk_ap_db_intro_content.strats import *

class DatatypesSimpeleTekstView(ContentView):
    uid = 'xchk_ap_db_intro_content_datatypes_simpele_tekst'
    title = 'datatypes: simpele tekst'
    template = 'xchk_ap_db_intro_content/datatypes_simpele_tekst.html'
    strat = xchk_ap_db_intro_content_datatypes_simpele_tekst_strat

class BasisstructurenVanEenRelationeleDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_basisstructuren_van_een_relationele_database'
    title = 'Basisstructuren van een relationele database'
    template = 'xchk_ap_db_intro_content/basisstructuren_van_een_relationele_database.html'
    strat = xchk_ap_db_intro_content_basisstructuren_van_een_relationele_database_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}

class LokaleVsRemoteDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_lokale_vs_remote_database'
    title = 'Lokale vs. remote database'
    template = 'xchk_ap_db_intro_content/lokale_vs_remote_database.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class VoorbeeldinstructiesMySQLView(ContentView):
    uid = 'xchk_ap_db_intro_content_voorbeeldinstructies_mysql'
    title = 'Voorbeeldinstructies MySQL'
    template = 'xchk_ap_db_intro_content/voorbeeldinstructies_mysql.html'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())

class VoordelenVanEenDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_voordelen_van_een_database'
    title = 'Voordelen van een database'
    template = 'xchk_ap_db_intro_content/voordelen_van_een_database.html'
    strat = xchk_ap_db_intro_content_voordelen_van_een_database_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}


class SubtalenVanMySqlView(ContentView):
    uid = 'xchk_ap_db_intro_content_subtalen_van_my_sql'
    title = 'subtalen van (My)SQL'
    template = 'xchk_ap_db_intro_content/subtalen_van_my_sql.html'
    strat = xchk_ap_db_intro_content_subtalen_van_my_sql_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}


class SchermovernameView(ContentView):
    uid = 'xchk_ap_db_intro_content_schermovername'
    title = 'schermovername'
    template = 'xchk_ap_db_intro_content/schermovername.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class DiagramnotatieTabelView(ContentView):
    uid = 'xchk_ap_db_intro_content_diagramnotatie_tabel'
    title = 'diagramnotatie tabel'
    template = 'xchk_ap_db_intro_content/diagramnotatie_tabel.html'
    strat = xchk_ap_db_intro_content_diagramnotatie_tabel_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}

class InstallatieDockerView(ContentView):
    uid = 'xchk_ap_db_intro_content_installatie_docker'
    title = 'installatie Docker'
    template = 'xchk_ap_db_intro_content/installatie_docker.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class MysqlWorkbenchInstallerenView(ContentView):
    uid = 'xchk_ap_db_intro_content_mysql_workbench_installeren'
    title = 'MySQL Workbench installeren'
    template = 'xchk_ap_db_intro_content/mysql_workbench_installeren.html'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())


class WatIsEenDatabankView(ContentView):
    uid = 'xchk_ap_db_intro_content_wat_is_een_databank'
    title = 'Wat is een databank'
    template = 'xchk_ap_db_intro_content/wat_is_een_databank.html'
    strat = xchk_ap_db_intro_content_wat_is_een_databank_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}

class VerbindenMetEenLokaleDatabaseServerViaWorkbenchView(ContentView):
    uid = 'xchk_ap_db_intro_content_verbinden_met_een_lokale_database_server_via_workbench'
    title = 'Verbinden met een lokale database server via Workbench'
    template = 'xchk_ap_db_intro_content/verbinden_met_een_lokale_database_server_via_workbench.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CreateStatementView(ContentView):
    uid = 'xchk_ap_db_intro_content_create_statement'
    title = 'CREATE statement'
    template = 'xchk_ap_db_intro_content/create_statement.html'
    strat = xchk_ap_db_intro_content_create_statement_strat

class DropStatementView(ContentView):
    uid = 'xchk_ap_db_intro_content_drop_statement'
    title = 'DROP statement'
    template = 'xchk_ap_db_intro_content/drop_statement.html'
    strat = xchk_ap_db_intro_content_drop_statement_strat

class MysqlDockerImageView(ContentView):
    uid = 'xchk_ap_db_intro_content_mysql_docker_image'
    title = 'MySQL Docker image'
    template = 'xchk_ap_db_intro_content/mysql_docker_image.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class DatatypesGeheleGetallenView(ContentView):
    uid = 'xchk_ap_db_intro_content_datatypes_gehele_getallen'
    title = 'datatypes: gehele getallen'
    template = 'xchk_ap_db_intro_content/datatypes_gehele_getallen.html'
    strat = xchk_ap_db_intro_content_datatypes_gehele_getallen_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}

class DatatypesTemporeleTypesView(ContentView):
    uid = 'xchk_ap_db_intro_content_datatypes_temporele_types'
    title = 'datatypes: temporeel'
    template = 'xchk_ap_db_intro_content/datatypes_temporeel.html'
    strat = xchk_ap_db_intro_content_datatypes_temporeel_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}

class DatatypesBooleansView(ContentView):
    uid = 'xchk_ap_db_intro_content_datatypes_booleans'
    title = 'datatypes: booleans'
    template = 'xchk_ap_db_intro_content/datatypes_booleans.html'
    strat = xchk_ap_db_intro_content_datatypes_booleans_strat

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
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())

class WatIsEenRelationeleDatabaseView(ContentView):
    uid = 'xchk_ap_db_intro_content_wat_is_een_relationele_database'
    title = 'Wat is een relationele database?'
    template = 'xchk_ap_db_intro_content/wat_is_een_relationele_database.html'
    strat = xchk_ap_db_intro_content_wat_is_een_relationele_database_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}

class DatabaseSelecterenView(ContentView):
    uid = 'xchk_ap_db_intro_content_database_selecteren'
    title = 'database selecteren'
    template = 'xchk_ap_db_intro_content/database_selecteren.html'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())

class IfNotExistsView(ContentView):
    uid = 'xchk_ap_db_intro_content_if_not_exists'
    title = 'if not exists'
    template = 'xchk_ap_db_intro_content/if_not_exists.html'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())

class InsertStatementView(ContentView):
    uid = 'xchk_ap_db_intro_content_insert_statement'
    title = 'INSERT statement'
    template = 'xchk_ap_db_intro_content/insert_statement.html'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())

class SelectStatementView(ContentView):
    uid = 'xchk_ap_db_intro_content_select_statement'
    title = 'SELECT statement'
    template = 'xchk_ap_db_intro_content/select_statement.html'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())

class NotNullView(ContentView):
    uid = 'xchk_ap_db_intro_content_not_null'
    title = 'not NULL'
    template = 'xchk_ap_db_intro_content/not_null.html'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())

class ZelftestTheorieEenView(ContentView):
    uid = 'xchk_ap_db_intro_content_zelftest_theorie_een'
    title = 'zelftest theorie 1'
    template = 'xchk_ap_db_intro_content/zelftest_theorie_een.html'
    strat = xchk_ap_db_intro_content_self_test_theory_strat
    custom_data = {'rendered_mc_qs': strat.refusing_check.negated_predicate.conjuncts[2].render()}
