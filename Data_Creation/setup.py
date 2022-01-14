import tables_init
import FOITHTHS
import DOMATIA
import ESTIA
import KANEI_AITHSH
import AITHSH_SITHSHS
import AITHSH_STEGASHS
import EGGRAFA

tables_init.generate("sqlite.sql", "merimna.db")
FOITHTHS.generate("excel_files/Names.xls", "merimna.db")
ESTIA.generate("merimna.db")
DOMATIA.generate("merimna.db")
KANEI_AITHSH.generate("merimna.db")
AITHSH_SITHSHS.generate("excel_files/KATOIKIES.xls", "merimna.db")
AITHSH_STEGASHS.generate("excel_files/KATOIKIES.xls", "merimna.db")
EGGRAFA.generate("merimna.db")
