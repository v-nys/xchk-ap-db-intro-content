
from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('databanken intro','Databanken Intro',[(BasisstructurenVanEenRelationeleDatabaseView,[WatIsEenRelationeleDatabaseView]),(CreateStatementView,[SubtalenVanMySqlView,DiagramnotatieTabelView,DatabaseSelecterenView]),(DatabaseSelecterenView,[SubtalenVanMySqlView]),(DatatypesGeheleGetallenView,[WatIsMysqlView]),(DatatypesSimpeleTekstView,[WatIsMysqlView]),(DiagramnotatieTabelView,[DatatypesSimpeleTekstView,DatatypesGeheleGetallenView]),(InstallatieDockerView,[WatIsDockerView]),(LokaleVsRemoteDatabaseView,[VerbindenMetDeDatabaseServerViaWorkbenchView]),(MysqlDockerImageView,[InstallatieDockerView]),(MysqlWorkbenchInstallerenView,[WatIsMysqlView]),(SchermovernameView,[]),(SubtalenVanMySqlView,[WatIsMysqlView]),(VerbindenMetDeDatabaseServerViaWorkbenchView,[MysqlWorkbenchInstallerenView]),(VerbindenMetEenLokaleDatabaseServerViaWorkbenchView,[MysqlDockerImageView,LokaleVsRemoteDatabaseView]),(VoordelenVanEenDatabaseView,[WatIsEenDatabankView]),(WatIsDockerView,[]),(WatIsEenDatabankView,[]),(WatIsEenRelationeleDatabaseView,[VoordelenVanEenDatabaseView]),(WatIsMysqlView,[BasisstructurenVanEenRelationeleDatabaseView])])
