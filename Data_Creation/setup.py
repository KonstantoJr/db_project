import tables_init
import FOITHTHS
import DOMATIA
import ESTIA
import KANEI_AITHSH
import AITHSH_SITHSHS
import AITHSH_STEGASHS

tables_init.generate("merimna.db")
FOITHTHS.generate("Names.xls", "merimna.db")
DOMATIA.generate("DOMATIA.xls", "merimna.db")
ESTIA.generate("ESTIA.xls", "merimna.db")
KANEI_AITHSH.generate("merimna.db")
AITHSH_SITHSHS.generate("KATOIKIES.xls", "merimna.db")
AITHSH_STEGASHS.generate("KATOIKIES.xls", "merimna.db")
