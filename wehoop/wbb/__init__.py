import pyarrow.parquet as pq
import pandas as pd
from typing import List, Callable, Iterator, Union, Optional
from wehoop.config import WBB_BASE_URL, WBB_TEAM_BOX_URL, WBB_PLAYER_BOX_URL, WBB_TEAM_SCHEDULE_URL
from wehoop.errors import SeasonNotFoundError
from wehoop.dl_utils import download

def load_wbb_pbp(seasons: List[int]) -> pd.DataFrame:
    """Load women's college basketball play by play data going back to 2002

    Example:
        `wbb_df = wehoop.wbb.load_wbb_pbp(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        play-by-plays available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(WBB_BASE_URL.format(season=i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_wbb_team_boxscore(seasons: List[int]) -> pd.DataFrame:
    """Load women's college basketball team boxscore data

    Example:
        `wbb_df = wehoop.wbb.load_wbb_team_boxscore(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        team boxscores available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise ValueError("season cannot be less than 2002")
        i_data = pd.read_parquet(WBB_TEAM_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wbb_player_boxscore(seasons: List[int]) -> pd.DataFrame:
    """Load women's college basketball player boxscore data

    Example:
        `wbb_df = wehoop.wbb.load_wbb_player_boxscore(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        player boxscores available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise ValueError("season cannot be less than 2002")
        i_data = pd.read_parquet(WBB_PLAYER_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wbb_schedule(seasons: List[int]) -> pd.DataFrame:
    """Load women's college basketball schedule data

    Example:
        `wbb_df = wehoop.wbb.load_wbb_schedule(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        schedule for  the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise ValueError("season cannot be less than 2002")
        i_data = pd.read_parquet(WBB_TEAM_SCHEDULE_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def wbb_calendar(season: int) -> pd.DataFrame:
    """wbb_calendar - look up the women's college basketball calendar for a given season

    Args:
        season (int): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing
        calendar dates for the requested season.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    if int(season) < 2002:
        raise SeasonNotFoundError("season cannot be less than 2002")
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/scoreboard?dates={}".format(season)
    resp = download(url=url)
    txt = json.loads(resp)['leagues'][0]['calendar']
    reg = pd.DataFrame(txt[0]['entries'])
    post = pd.DataFrame(txt[1]['entries'])
    full_schedule = pd.concat([reg,post], ignore_index=True)
    full_schedule['season']=season
    return full_schedule

