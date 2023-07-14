from datetime import datetime, timedelta
from typing import Literal

from discord.utils import format_dt

def timestamp(
    seconds: int | float, style: Literal
) -> str:
    dt = datetime.utcnow() + timedelta(seconds=seconds)
    return format_dt(dt, style)

