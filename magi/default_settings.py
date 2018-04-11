from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _, string_concat
from magi.django_translated import t
from django.conf import settings

RAW_CONTEXT = {
    'debug': settings.DEBUG,
    'site': settings.SITE,
    'extends': 'base.html',
    'forms': {},
    'form': None,
}

_usernameRegexp = '[\w.@+-]+'

############################################################
# Javascript translated terms

FORCE_ADD_TO_TRANSLATION = [
    _('Liked this activity'),
    _('Loading'), _('No result.'),
    _('Local time'),
    _('days'), _('hours'), _('minutes'), _('seconds'),
]

DEFAULT_JAVASCRIPT_TRANSLATED_TERMS = [
    'Liked this activity',
    'Loading', 'No result.',
    'You can\'t cancel this action afterwards.', 'Confirm', 'Cancel',
    'days', 'hours', 'minutes', 'seconds',
    'Local time',
]

############################################################
# Groups

DEFAULT_GROUPS = [
    ('manager', {
        'translation': _('Manager'),
        'description': 'The leader of our staff team is here to make sure that the website is doing well! They make sure we all get things done together and the website keeps getting new users everyday.',
        'permissions': ['edit_roles', 'edit_staff_status', 'edit_donator_status', 'see_profile_edit_button', 'edit_staff_configurations', 'add_badges', 'see_collections_details'],
    }),
    ('circles', {
        'translation': string_concat('Circles - ', _('Manager')),
        'description': 'Supervises and helps the creation and growth of all the websites. Advises but generally doesn\'t interfere with the managers\' decisions.',
        'requires_staff': True,
    }),
    ('team', {
        'translation': _('Team manager'),
        'description': 'Knows all the team members and discuss with them on a regular basis to make sure they are all active.',
        'permissions': ['edit_staff_status', 'edit_roles', 'see_profile_edit_button'],
        'requires_staff': True,
        'outside_permissions': [
            'Administrate the contributors on GitHub',
            'Administrate the contributors on Tweetdeck',
            'Administrate the moderators on Disqus',
        ],
    }),
    ('finance', {
        'translation': _('Finance manager'),
        'description': 'The finances manager keeps track of our monthly spending and donations, makes sure donators get their rewards, and we have enough funds every month to cover the server and other expenses.',
        'permissions': ['add_donation_badges', 'manage_donation_months', 'edit_donator_status'],
        'requires_staff': True,
        'requires_staff': True,
        'outside_permissions': [
            'Access Patreon manager',
            'Access donators forms responses',
        ],
    }),
    ('db', {
        'translation': _('Database maintainer'),
        'description': 'We gather all the game data in one convenient place for you~ Some of our team members extract the assets and data directly from the game, some enter missing info manually. We do our best to publish all the game data as soon as it gets published!',
        'permissions': ['manage_main_items'],
        'requires_staff': True,
        'outside_permissions': [
            'API key',
        ],
    }),
    ('cm', {
        'translation': _('Community manager'),
        'description': 'We got you covered with all the game news on the website! Thanks to our active team, you know that by following our latest activities, you\'ll never miss anything!',
        'permissions': ['edit_staff_configurations'],
        'requires_staff': True,
    }),
    ('twitter_cm', {
        'translation': string_concat(_('Community manager'), ' (', _('Twitter'), ')'),
        'description': 'We got you covered with all the game news on Twitter! Thanks to our active team, you know that by following us on Twitter, you\'ll never miss anything!',
        'requires_staff': True,
        'outside_permissions': [
            'Tweetdeck',
        ],
    }),
    ('external_cm', {
        'translation': _('External communication'),
        'description': 'We\'re very active on other social media, such as Facebook, reddit and various forums! Our team will take the time to inform the other community about our website news and hopefully get more users from there, as well as valuable feedback to improve the website!',
        'requires_staff': True,
    }),
    ('support', {
        'translation': _('Support'),
        'description': 'Need help with our website or the game? Our support team is here to help you and answer your questions!',
        'requires_staff': True,
        'outside_permissions': [
            'Tweetdeck',
            'Receive private messages on Facebook',
            'Receive private messages on Reddit',
            'Receive emails',
        ],
    }),
    ('a_moderator', {
        'translation': string_concat(_('Moderator'), ' (', _('Active'), ')'),
        'description': 'We want all of our users of all ages to have a pleasant a safe stay in our website. That\'s why our team of moderators use the website everyday and report anything that might be inappropriate or invalid!',
        'requires_staff': True,
    }),
    ('d_moderator', {
        'translation': string_concat(_('Moderator'), ' (', _('Decisive'), ')'),
        'description': 'When something gets reported, our team of decisive moderators will make a decision on whether or not it should be edited or deleted. This 2-steps system ensures that our team makes fair decisions!',
        'permissions': ['moderate_reports', 'edit_reported_things'],
        'requires_staff': True,
        'outside_permissions': [
            'Disqus moderation',
        ],
    }),
    ('entertainer', {
        'translation': _('Community entertainer'),
        'description': 'We keep the community active and happy by organizing fun stuff: contests, giveaways, games, etc. We\'re open to feedback and ideas!',
        'permissions': ['edit_staff_configurations', 'add_badges'],
        'requires_staff': True,
        'outside_permissions': [
            'Tweetdeck',
        ],
    }),
    ('discord', {
        'translation': string_concat(_('Moderator'), ' (Discord)'),
        'description': '',
        'permissions': ['translate_items', 'translate_staff_configurations'],
        'requires_staff': False,
        'outside_permissions': [
            'Discord moderator role',
        ],
    }),
    ('translator', {
        'translation': _('Translator'),
        'description': 'Many people can\'t understand English very well, so by doing so our amazing translators work hard to translate our websites in many languages. By doing so they\'re helping hundreds of people access the information we provide easily and comfortably.',
        'permissions': ['translate_items', 'translate_staff_configurations'],
        'requires_staff': False,
        'outside_permissions': [
            'POEditor access',
        ],
    }),
    ('design', {
        'translation': _('Graphic designer'),
        'description': 'Our graphic designers help with banners, flyers, or any other graphic edit we need to communicate about the website or organize special events.',
        'requires_staff': False,
    }),
    ('artist', {
        'translation': _('Artist'),
        'description': 'Our artists help with illustrations and drawings we need to communicate about the website or organize special events.',
        'requires_staff': False,
    }),
    ('developer', {
        'translation': _('Developer'),
        'description': 'Developers contribute to the website by adding new features or fixing bugs, and overall maintaining the website.',
        'permissions': ['advanced_staff_configurations', 'see_collections_details'],
        'requires_staff': False,
    }),
    ('sysadmin', {
        'translation': _('System administrator'),
        'description': 'Our system administrators take care of the infrasturcture of our websites, including maintaining the servers, deploying new versions, ensuring that we scale according to traffic and under budget, and overall instrastructure monitoring.',
        'permissions': ['advanced_staff_configurations', 'see_collections_details'],
        'requires_staff': False,
    }),
]

############################################################
# Navbar lists

DEFAULT_ENABLED_NAVBAR_LISTS = OrderedDict([
    ('you', {
        'title': lambda context: context['request'].user.username if context['request'].user.is_authenticated() else _('You'),
        'icon': 'profile',
        'order': ['user', 'settings', 'logout', 'login', 'signup'],
        'url': '/me/',
    }),
    ('more', {
        'title': '',
        'icon': 'more',
        'order': ['about', 'donate_list', 'help', 'map', 'report_list', 'badge_list', 'staffconfiguration_list', 'collections'],
        'url': '/about/',
    }),
])

############################################################
# Enabled pages

DEFAULT_ENABLED_PAGES = OrderedDict([
    ('index', {
        'custom': False,
        'enabled': False,
        'navbar_link': False,
    }),
    ('login', {
        'custom': False,
        'title': _('Login'),
        'navbar_link_list': 'you',
        'logout_required': True,
    }),
    ('signup', {
        'custom': False,
        'title': _('Sign Up'),
        'navbar_link_list': 'you',
        'logout_required': True,
    }),
    ('user', {
        'custom': False,
        'title': _('Profile'),
        'icon': 'profile',
        'url_variables': [
            ('pk', '\d+', lambda (context): str(context['request'].user.id)),
            ('username', _usernameRegexp, lambda (context): context['request'].user.username),
        ],
        'navbar_link_list': 'you',
        'authentication_required': True,
    }),
    ('settings', {
        'title': _('Settings'),
        'custom': False,
        'icon': 'settings',
        'navbar_link_list': 'you',
        'authentication_required': True,
    }),
    ('logout', {
        'custom': False,
        'title': _('Logout'),
        'icon': 'logout',
        'navbar_link_list': 'you',
        'authentication_required': True,
    }),
    ('about', [
        {
            'title': _('About'),
            'custom': False,
            'icon': 'about',
            'navbar_link_list': 'more',
        },
        {
            'ajax': True,
            'title': _('About'),
            'custom': False,
            'icon': 'about',
            'navbar_link_list': 'more',
        },
    ]),
    ('prelaunch', {
        'title': _('Coming soon'),
        'custom': False,
        'navbar_link': False,
    }),
    ('about_game', {
        'ajax': True,
        'title': _('About the game'),
        'custom': False,
        'icon': 'about',
    }),
    ('map', {
        'title': _('Map'),
        'custom': False,
        'icon': 'world',
        'navbar_link_list': 'more',
        'divider_after': True,
    }),
    ('help', [
        {
            'custom': False,
            'title': _('Help'),
            'icon': 'help',
            'navbar_link_list': 'more',
        },
        {
            'custom': False,
            'title': _('Help'),
            'url_variables': [
                ('wiki_url', '[^/]+'),
            ],
            'navbar_link': False,
        },
    ]),
    ('wiki', [
        {
            'enabled': False,
            'custom': False,
            'title': _('Wiki'),
            'icon': 'about',
        },
        {
            'enabled': False,
            'custom': False,
            'icon': 'about',
            'title': _('Wiki'),
            'url_variables': [
                ('wiki_url', '[^/]+'),
            ],
            'navbar_link': False,
        },
    ]),
    ('collections', {
        'title': 'Collections',
        'custom': False,
        'navbar_link_list': 'more',
        'icon': 'developer',
        'permissions_required': ['see_collections_details'],
    }),
    ('deletelink', {
        'ajax': True,
        'custom': False,
        'url_variables': [
            ('pk', '\d+'),
        ],
    }),
    ('likeactivity', {
        'ajax': True,
        'custom': False,
        'url_variables': [
            ('pk', '\d+'),
        ],
    }),
    ('follow', {
        'ajax': True,
        'custom': False,
        'url_variables': [
            ('username', _usernameRegexp),
        ],
    }),
    ('twitter_avatar', {
        'custom': False,
        'navbar_link': False,
        'url_variables': [
            ('twitter', '[^/]+'),
        ]
    }),
    ('changelanguage', {
        'ajax': True,
        'custom': False,
        'navbar_link': False,
    }),
    ('moderatereport', {
        'ajax': True,
        'custom': False,
        'navbar_link': False,
        'url_variables': [
            ('report', '\d+'),
            ('action', '\w+'),
        ],
    }),
    ('reportwhatwillbedeleted', {
        'ajax': True,
        'custom': False,
        'navbar_link': False,
        'url_variables': [
            ('report', '\d+'),
        ],
    }),
    ('successedit', {
        'ajax': True,
        'custom': False,
        'navbar_link': False,
    }),
    ('successadd', {
        'ajax': True,
        'custom': False,
        'navbar_link': False,
    }),
    ('successdelete', {
        'ajax': True,
        'custom': False,
        'navbar_link': False,
    }),
])

############################################################
# Default profile tabs

DEFAULT_PROFILE_TABS = OrderedDict([
    ('account', {
        'name': _('Accounts'),
        'icon': 'users',
    }),
    ('activity', {
        'name': _('Activities'),
        'icon': 'comments',
        'callback': 'profileLoadActivities',
    }),
    ('badge', {
        'name': _('Badges'),
        'icon': 'achievement',
        'callback': 'loadBadges',
    }),
])

############################################################
# Default navbar ordering

DEFAULT_NAVBAR_ORDERING = [
    'account_list',
    'you',
    'more',
]

############################################################
# Default prelaunch enabled pages

DEFAULT_PRELAUNCH_ENABLED_PAGES = [
    'login',
    'signup',
    'prelaunch',
    'about',
    'about_game',
    'changelanguage',
    'help',
]
