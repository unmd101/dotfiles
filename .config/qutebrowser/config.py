config.load_autoconfig()

# Custom Bindings
config.bind('po', 'spawn linkhandler {url}')
config.bind('pm', 'spawn ytmd {url}')
config.bind('pr', 'spawn --userscript readability {url}')
config.bind('pf', 'spawn --userscript openfeeds {url}')
config.bind('yo', 'hint links spawn linkhandler {hint-url}')
config.bind('ym', 'hint links spawn ytmd {hint-url}')
config.bind('yr', 'hint links spawn --userscript readability {url}')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('<Ctrl-1>', 'tab-focus 1')
config.bind('<Ctrl-2>', 'tab-focus 2')
config.bind('<Ctrl-3>', 'tab-focus 3')
config.bind('<Ctrl-4>', 'tab-focus 4')
config.bind('<Ctrl-5>', 'tab-focus 5')
config.bind('<Ctrl-6>', 'tab-focus 6')
config.bind('<Ctrl-7>', 'tab-focus 7')
config.bind('<Ctrl-8>', 'tab-focus 8')
config.bind('<Ctrl-9>', 'tab-focus -1')

# Search engines
c.url.searchengines = {'DEFAULT':'https://searx.fmac.xyz/search?q={}',
                       'gh': 'https://github.com/search?q={}',
                       'mv': 'https://movielens.org/explore?q={}',
                       'gr': 'https://www.goodreads.com/search?q={}',
                       'w': 'http://ru.wikipedia.org/w/index.php?title=Special:Search&search={}',
                       'y': 'https://www.youtube.com/results?search_query={}',
                       'rtk': 'https://rutracker.org/forum/tracker.php?nm={}',
                       'trans': 'https://translate.google.com/?source=osdd#view=home&op=translate&sl=en&tl=ru&text={}'
                       }
# Etc
c.auto_save.session = False
c.completion.cmd_history_max_items = 10
c.completion.height = "30%"
c.completion.scrollbar.width = 12
c.confirm_quit = ['downloads']
c.content.geolocation = False
c.content.ssl_strict = True
c.content.host_blocking.enabled = True
c.content.mouse_lock = False
c.content.notifications = False
c.downloads.location.prompt = False
c.downloads.remove_finished = 500
c.tabs.background = True
c.url.start_pages = ['https://searx.fmac.xyz/']
c.url.default_page = 'https://searx.fmac.xyz/'
c.fonts.default_family = "xos4 Terminus"
c.fonts.default_size = "8pt"

# Palette
base00 = "#1d2021"
base01 = "#3c3836"
base02 = "#504945"
base03 = "#665c54"
base04 = "#bdae93"
base05 = "#f4ecd7"
base06 = "#ebdbb2"
base07 = "#fbf1c7"
base08 = "#fb4934"
base09 = "#fe8019"
base0A = "#fabd2f"
base0B = "#b8bb26"
base0C = "#8ec07c"
base0D = "#83a598"
base0E = "#d3869b"
base0F = "#d65d0e"

# Competition
c.colors.completion.fg = base05
c.colors.completion.odd.bg = base00
c.colors.completion.even.bg = base00
c.colors.completion.category.fg = base0A
c.colors.completion.category.bg = base00
c.colors.completion.category.border.top = base00
c.colors.completion.category.border.bottom = base00
c.colors.completion.item.selected.fg = base01
c.colors.completion.item.selected.bg = base0A
c.colors.completion.item.selected.border.top = base0A
c.colors.completion.item.selected.border.bottom = base0A
c.colors.completion.item.selected.match.fg = base08
c.colors.completion.match.fg = base0B
c.colors.completion.scrollbar.fg = base05
c.colors.completion.scrollbar.bg = base00

# Downloads
c.colors.downloads.bar.bg = base00
c.colors.downloads.start.fg = base00
c.colors.downloads.start.bg = base0D
c.colors.downloads.stop.fg = base00
c.colors.downloads.stop.bg = base0C
c.colors.downloads.error.fg = base08

# Hints
c.colors.hints.fg = base00
c.colors.hints.bg = base0A
c.colors.hints.match.fg = base05
c.colors.keyhint.fg = base05
c.colors.keyhint.suffix.fg = base05
c.colors.keyhint.bg = base00

# Messages
c.colors.messages.error.fg = base00
c.colors.messages.error.bg = base08
c.colors.messages.error.border = base08
c.colors.messages.warning.fg = base00
c.colors.messages.warning.bg = base0E
c.colors.messages.warning.border = base0E
c.colors.messages.info.fg = base05
c.colors.messages.info.bg = base00
c.colors.messages.info.border = base00

# Prompts
c.colors.prompts.fg = base05
c.colors.prompts.border = base00
c.colors.prompts.bg = base00
c.colors.prompts.selected.bg = base0A

# Statusbar
c.colors.statusbar.normal.fg = base0B
c.colors.statusbar.normal.bg = base00
c.colors.statusbar.insert.fg = base00
c.colors.statusbar.insert.bg = base0D
c.colors.statusbar.passthrough.fg = base00
c.colors.statusbar.passthrough.bg = base0C
c.colors.statusbar.private.fg = base00
c.colors.statusbar.private.bg = base01
c.colors.statusbar.command.fg = base05
c.colors.statusbar.command.bg = base00
c.colors.statusbar.command.private.fg = base05
c.colors.statusbar.command.private.bg = base00
c.colors.statusbar.caret.fg = base00
c.colors.statusbar.caret.bg = base0E
c.colors.statusbar.caret.selection.fg = base00
c.colors.statusbar.caret.selection.bg = base0D
c.colors.statusbar.progress.bg = base0D
c.colors.statusbar.url.fg = base05
c.colors.statusbar.url.error.fg = base08
c.colors.statusbar.url.hover.fg = base05
c.colors.statusbar.url.success.http.fg = base0C
c.colors.statusbar.url.success.https.fg = base0B
c.colors.statusbar.url.warn.fg = base0E

# Tabs
c.colors.tabs.bar.bg = base00
c.colors.tabs.indicator.start = base0D
c.colors.tabs.indicator.stop = base0C
c.colors.tabs.indicator.error = base08
c.colors.tabs.odd.fg = base05
c.colors.tabs.odd.bg = base01
c.colors.tabs.even.fg = base05
c.colors.tabs.even.bg = base01
c.colors.tabs.pinned.even.bg = base0C
c.colors.tabs.pinned.even.fg = base07
c.colors.tabs.pinned.odd.bg = base0B
c.colors.tabs.pinned.odd.fg = base07
c.colors.tabs.pinned.selected.even.bg = base05
c.colors.tabs.pinned.selected.even.fg = base00
c.colors.tabs.pinned.selected.odd.bg = base00
c.colors.tabs.pinned.selected.odd.fg = base0E
c.colors.tabs.selected.odd.fg = base05
c.colors.tabs.selected.odd.bg = base00
c.colors.tabs.selected.even.fg = base05
c.colors.tabs.selected.even.bg = base00

# Tab padding
c.tabs.padding = {"bottom": 1, "left": 5, "right": 5, "top": 1}
c.tabs.favicons.scale = 1
