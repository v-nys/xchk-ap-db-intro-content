from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from xchk_docker_content import *
from xchk_mysql_content.contentviews import *
from .contentviews import *

course = Course('apdbintro',
                'APDBIntro',
                [(WhatIsMySQLView,[WhatIsDockerView])])
