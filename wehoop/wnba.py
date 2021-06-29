import pyarrow.parquet as pq
import pandas as pd
from typing import List, Callable, Iterator, Union, Optional
from wehoop.config import WNBA_BASE_URL, WNBA_TEAM_BOX_URL, WNBA_PLAYER_BOX_URL, WNBA_TEAM_SCHEDULE_URL
from wehoop.errors import SeasonNotFoundError

def load_wnba_pbp(seasons: List[int]) -> pd.DataFrame:
    """
    Load WNBA play by play data going back to 2002
    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.
    Returns:
        pbp_df (pandas dataframe): Pandas dataframe containing
        play-by-plays available for the requested seasons.
    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_BASE_URL.format(season=i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_wnba_team_boxscore(seasons: List[int]) -> pd.DataFrame:
    """
    Load WNBA team boxscore data
    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.
    Returns:
        team_boxscore_df (pandas dataframe): Pandas dataframe containing the
        team boxscores available for the requested seasons.
    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_TEAM_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wnba_player_boxscore(seasons: List[int]) -> pd.DataFrame:
    """
    Load WNBA player boxscore data
    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.
    Returns:
        player_boxscore_df (pandas dataframe): Pandas dataframe containing the
        player boxscores available for the requested seasons.
    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_PLAYER_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wnba_schedule(seasons: List[int]) -> pd.DataFrame:
    """
    Load WNBA schedule data
    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.
    Returns:
        schedule_df (pandas dataframe): Pandas dataframe containing the
        schedule for  the requested seasons.
    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_TEAM_SCHEDULE_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data





