import pyarrow.parquet as pq
import pandas as pd
from typing import Callable, Iterator, Union, Optional, List
from wehoop.config import WBB_BASE_URL, WBB_TEAM_BOX_URL, WBB_PLAYER_BOX_URL, WBB_TEAM_SCHEDULE_URL
from wehoop.errors import SeasonNotFoundError

def load_wbb_pbp(years: List[int]) -> pd.DataFrame:
    """
    Load women's college basketball play by play data going back to 2003
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WBB_BASE_URL.format(year=i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_wbb_team_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load women's college basketball team boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WBB_TEAM_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wbb_player_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load women's college basketball player boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WBB_PLAYER_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wbb_schedule(years: List[int]) -> pd.DataFrame:
    """
    Load women's college basketball schedule data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(WBB_TEAM_SCHEDULE_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data





