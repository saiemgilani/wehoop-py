import pyarrow.parquet as pq
import pandas as pd
from typing import Callable, Iterator, Union, Optional, List
from wehoop.config import WNBA_BASE_URL, WNBA_TEAM_BOX_URL, WNBA_PLAYER_BOX_URL, WNBA_TEAM_SCHEDULE_URL
from wehoop.errors import SeasonNotFoundError

def load_wnba_pbp(years: List[int]) -> pd.DataFrame:
    """
    Load WNBA play by play data going back to 2003
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WNBA_BASE_URL.format(year=i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_wnba_team_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load WNBA team boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WNBA_TEAM_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wnba_player_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load WNBA player boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WNBA_PLAYER_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wnba_schedule(years: List[int]) -> pd.DataFrame:
    """
    Load NBA schedule data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WNBA_TEAM_SCHEDULE_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data





