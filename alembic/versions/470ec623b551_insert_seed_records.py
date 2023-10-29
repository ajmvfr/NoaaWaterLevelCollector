"""insert seed records

Revision ID: 470ec623b551
Revises: ab79d7d6e1c8
Create Date: 2023-10-28 16:13:45.297055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '470ec623b551'
down_revision: Union[str, None] = 'ab79d7d6e1c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("insert into station (station_code) values ('BEAP1'),('WPMP1')") # BEAVER
    op.execute("insert into station (station_code) values ('NCSP1'),('LLWO1'),('ZLPP1'),('WURP1'),('PRVP1')") # BEAVER FEEDER
    op.execute("insert into station (station_code) values ('MGYP1'),('DSHP1'),('EMXP1'),('PTTP1')") # OHIO 
    op.execute("insert into station (station_code) values ('MFFP1'),('CARP1'),('DQHP1')") # OHIO FEEDERS
    op.execute("insert into station (station_code) values ('SHRP1'),('ACMP1'),('NATP1'),('FREP1'),('CLNP1'),('KTTP1'),('MOSP1'),('RMRP1')") # ALLEGHENY
    op.execute("insert into station (station_code) values ('GTYP1'),('PNEP1'),('VGFP1'),('CCDP1'),('MHDP1') ") # ALLEGHENY FEEDER
    op.execute("insert into station (station_code) values ('BDDP1'),('ELZP1'),('CHRP1'),('MAXP1'),('GYLP1'),('PMRP1')") # MONONGAHELA
    op.execute("insert into station (station_code) values ('TTKP1'),('WRDP1'),('JFRP1'),('SNPP1'),('LLPW2')")  # MONONGAHELA FEEDER
    op.execute("insert into station (station_code) values ('STSP1'),('CLLP1')") #YOUGHIOGHENY

    pass


def downgrade() -> None:
    pass
