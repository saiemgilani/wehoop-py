# wehoop package

## Submodules

## wehoop.config module

## wehoop.dl_utils module


### wehoop.dl_utils.download(url, num_retries=5)
## wehoop.errors module

Custom exceptions for wehoop module


### exception wehoop.errors.SeasonNotFoundError()
Bases: `Exception`

## wehoop.schedule module


### wehoop.schedule.wbb_calendar(season: int)

### wehoop.schedule.wnba_calendar(season: int)

## wehoop.wbb module


### wehoop.wbb.load_wbb_pbp(seasons: List[int])
Load women’s college basketball play by play data going back to 2002
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pbp_df (pandas dataframe): Pandas dataframe containing the
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wbb.load_wbb_player_boxscore(seasons: List[int])
Load women’s college basketball player boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    player_boxscore_df (pandas dataframe): Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wbb.load_wbb_schedule(seasons: List[int])
Load women’s college basketball schedule data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    schedule_df (pandas dataframe): Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wbb.load_wbb_team_boxscore(seasons: List[int])
Load women’s college basketball team boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    team_boxscore_df (pandas dataframe): Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.

## wehoop.wnba module


### wehoop.wnba.load_wnba_pbp(seasons: List[int])
Load WNBA play by play data going back to 2002
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pbp_df (pandas dataframe): Pandas dataframe containing
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wnba.load_wnba_player_boxscore(seasons: List[int])
Load WNBA player boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    player_boxscore_df (pandas dataframe): Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wnba.load_wnba_schedule(seasons: List[int])
Load WNBA schedule data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    schedule_df (pandas dataframe): Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wnba.load_wnba_team_boxscore(seasons: List[int])
Load WNBA team boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    team_boxscore_df (pandas dataframe): Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.

## Module contents
