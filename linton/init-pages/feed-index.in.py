#!/usr/bin/env python3

import sys, yaml, urllib.parse, html
from dataclasses import dataclass
from datetime import datetime
from functools import total_ordering
from pathlib import Path


def assert_type(value, type_):
    assert type(value) is type_, f'{value} is a {type(value)} not a {type_}'
    return value

assert len(sys.argv) == 1, sys.argv


@dataclass
@total_ordering
class Post:
    updated: datetime
    title: str
    summary: str
    url: str

    def _sort_key(self):
        """Compare `updated` date first, then `object.id()`."""
        return (self.updated, id(self))

    def __le__(self, other):
        return self._sort_key() <= other._sort_key()

    def __eq__(self, other):
        return self._sort_key() == other._sort_key()

    def to_html(self):
        return f"""\
<article>
<h3><a href="{self.url}">{html.escape(self.title)}</a></h3>
<p><em>{html.escape(self.updated.strftime("%d %B %Y"))}</em></p>
<p>{html.escape(self.summary)}</p>
</article>
"""


feed = yaml.safe_load(sys.stdin)
assert_type(feed, dict)
assert_type(feed['self-url'], str)
assert_type(feed['feed-description'], str)
assert_type(feed['posts'], list)


# Compute base URL of relative URLs in the feed.
scheme, netloc, path, _, _ = urllib.parse.urlsplit(feed['self-url'])
directory = str(Path(path).parent)
base_url = urllib.parse.urlunsplit((scheme, netloc, directory, '', ''))

posts = []

for post in feed['posts']:
    assert_type(post, dict)
    assert_type(post['path'], str)
    assert_type(post['published'], datetime)
    updated = post.get('updated', post['published'])
    assert_type(updated, datetime)
    assert_type(post['title'], str)
    assert_type(post['summary'], str)
    post_url = base_url + '/' + post['path']
    posts.append(Post(updated, post['title'], post['summary'], post_url))

posts.sort(reverse=True)

for post in posts:
    print(post.to_html())
