const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'wehoop-py',
  tagline: "The SportsDataverse's Python Package for Women's Basketball Data.",
  url: 'https://wehoop-py.sportsdataverse.org',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'sportsdataverse', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.
  themeConfig: {
    hideableSidebar: true,
    sidebarCollapsible: false,
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    image: 'img/wehoop-py-gh.png',
    navbar: {
      hideOnScroll: true,
      // title: 'wehoop-py',
      logo: {
        alt: 'wehoop Logo',
        src: 'img/logo.ico',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
        },
        {
          label: 'News',
          to: 'CHANGELOG',
          position: 'left',
        },
        {
          label: 'SDV',
          position: 'left',
          items: [
            {
              href: 'https://sportsdataverse.org',
              label: 'SportsDataverse',
            },
            {
              label: 'Python Packages',
            },
            {
              label: 'cfbfastR-py',
              href: 'https://cfbfastR-py.sportsdataverse.org',
            },
            {
              label: 'hoopR-py',
              href: 'https://hoopR-py.sportsdataverse.org',
            },
            {
              label: 'R Packages',
            },
            {
              label: 'cfbfastR',
              href: 'https://saiemgilani.github.io/cfbfastR/',
            },
            {
              label: 'hoopR',
              href: 'https://saiemgilani.github.io/hoopR/',
            },
            {
              label: 'wehoop',
              href: 'https://saiemgilani.github.io/wehoop/',
            },
            {
              label: 'recruitR',
              href: 'https://saiemgilani.github.io/recruitR/',
            },
            {
              label: 'puntr',
              href: 'https://puntalytics.github.io/puntr/',
            },
            {
              label: 'gamezoneR',
              href: 'https://jacklich10.github.io/gamezoneR/',
            },
          ]
        },
        {
          href: 'https://github.com/saiemgilani/wehoop-py',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Docs',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Twitter',
              href: 'https://twitter.com/saiemgilani',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/saiemgilani/wehoop-py',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} <strong>wehoop-py</strong>, developed by <a href='https://twitter.com/saiemgilani'>Saiem Gilani</a>, part of the <a href='https://sportsdataverse.org'>SportsDataverse</a>.`,
    },
    prism: {
      theme: lightCodeTheme,
      darkTheme: darkCodeTheme,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/saiemgilani/wehoop/edit/master/website/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
