
from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('databankenintro','Databanken Intro',[(ZelftestTheorieEenView,[DatatypesTemporeleTypesView,
                                                                               IfNotExistsView,
                                                                               DropStatementView,
                                                                               SelectStatementView,
                                                                               MysqlWorkbenchInstallerenView]),
                                                      (NotNullView,[CreateStatementView]),
                                                      (InsertStatementView,[NotNullView]),
                                                      (SelectStatementView,[InsertStatementView]),
                                                      (IfNotExistsView,[DatatypesBooleansView]),
                                                      (DatatypesTemporeleTypesView,[CreateStatementView]),
                                                      (DatatypesBooleansView,[CreateStatementView]),
                                                      (BasisstructurenVanEenRelationeleDatabaseView,[WatIsEenRelationeleDatabaseView]),
                                                      (DropStatementView,[CreateStatementView]),
                                                      (CreateStatementView,[DiagramnotatieTabelView,DatabaseSelecterenView]),
                                                      (DatabaseSelecterenView,[SubtalenVanMySqlView]),
                                                      (DatatypesGeheleGetallenView,[SubtalenVanMySqlView]),
                                                      (DatatypesSimpeleTekstView,[SubtalenVanMySqlView]),
                                                      (DiagramnotatieTabelView,[DatatypesSimpeleTekstView,DatatypesGeheleGetallenView]),
                                                      #(LokaleVsRemoteDatabaseView,[VerbindenMetDeDatabaseServerViaWorkbenchView]),
                                                      (MysqlWorkbenchInstallerenView,[WatIsMysqlView]),
                                                      (VoorbeeldinstructiesMySQLView,[WatIsMysqlView]),
                                                      (SubtalenVanMySqlView,[VoorbeeldinstructiesMySQLView]),
                                                      #(VerbindenMetDeDatabaseServerViaWorkbenchView,[MysqlWorkbenchInstallerenView]),
                                                      (VoordelenVanEenDatabaseView,[WatIsEenDatabankView]),
                                                      (WatIsEenDatabankView,[]),
                                                      (WatIsEenRelationeleDatabaseView,[VoordelenVanEenDatabaseView]),
                                                      (WatIsMysqlView,[BasisstructurenVanEenRelationeleDatabaseView])])
