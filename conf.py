from __future__ import unicode_literals
import yaml
BLOG_AUTHOR = "phlsphy"  # (translatable)
BLOG_TITLE = "phlsphy.net"  # (translatable)
SITE_URL = "http://www.phlsphy.net/"
BLOG_EMAIL = " "
BLOG_DESCRIPTION = "A little space on the internet for phlsphy."  # (translatable)
COMMENT_SYSTEM = None
DEFAULT_LANG = "en"
TRANSLATIONS = {
    DEFAULT_LANG: "",
}
NAVIGATION_LINKS = {}
THEME = "base"
THEME_COLOR = '#5670d4'
POSTS = (
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.ipynb", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
)
PAGES = (
    ("stories/*.md", "", "story.tmpl"),
)
TIMEZONE = "UTC"
COMPILERS = {
    "markdown": ('.md', '.mdown', '.markdown'),
    "ipynb": ('.ipynb'),
    "rest": ('.rst', '.txt'),
}
METADATA_FORMAT = "YAML"
INDEX_PATH = "posts"
COPY_SOURCES = False
SHOW_SOURCELINK = False
PRETTY_URLS = False
DISABLED_PLUGINS = ["robots"]
GLOBAL_CONTEXT = {}
WRITE_TAG_CLOUD = False
GENERATE_RSS = False
DISABLED_PLUGINS = ['classify_page_index', 'classify_sections', 'classify_indexes', 'classify_archive', 'tags', 'sitemap', 'robots', 'create_bundles']

GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'
GITHUB_REMOTE_NAME = 'origin'
GITHUB_COMMIT_SOURCE = True