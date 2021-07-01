/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

module.exports = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [{type: 'autogenerated', dirName: '.'}],
  docs: [
    { type: 'doc', id: 'intro' },
    {
      type: 'category',
      label: 'WBB',
      items: [
        'WBB/load_wbb_pbp',
        'WBB/load_wbb_team_boxscore',
        'WBB/load_wbb_player_boxscore',
        'WBB/load_wbb_schedule',
        'WBB/wbb_calendar',
      ],
    },
    {
      type: 'category',
      label: 'WNBA',
      items: [
        'WNBA/load_wnba_pbp',
        'WNBA/load_wnba_team_boxscore',
        'WNBA/load_wnba_player_boxscore',
        'WNBA/load_wnba_schedule',
        'WNBA/wnba_calendar',
      ],
    },
  ],
  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['hello'],
    },
  ],
   */
};
