# wehoop.wbb package

## Module contents


### wehoop.wbb.load_wbb_pbp(seasons: List[int])
Load women’s college basketball play by play data going back to 2002

Ex:

    wbb_df = wehoop.wbb.load_wbb_pbp(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wbb.load_wbb_player_boxscore(seasons: List[int])
Load women’s college basketball player boxscore data

Ex:

    wbb_df = wehoop.wbb.load_wbb_player_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wbb.load_wbb_schedule(seasons: List[int])
Load women’s college basketball schedule data

Ex:

    wbb_df = wehoop.wbb.load_wbb_schedule(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wbb.load_wbb_team_boxscore(seasons: List[int])
Load women’s college basketball team boxscore data

Ex:

    wbb_df = wehoop.wbb.load_wbb_team_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wbb.wbb_calendar(season: int)
wbb_calendar - look up the women’s college basketball calendar for a given season

Args:

    season (int): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing
    calendar dates for the requested season.

Raises:

    ValueError: If season is less than 2002.
