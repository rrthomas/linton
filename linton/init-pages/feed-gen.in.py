#!/usr/bin/env python3

import sys, yaml, urllib.parse
from datetime import datetime
from pathlib import Path
from feedgen.feed import FeedGenerator, FeedEntry


def assert_type(value, type_):
    assert type(value) is type_, f'{value} is a {type(value)} not a {type_}'
    return value

assert len(sys.argv) == 2, sys.argv
feed_type = sys.argv[1]
assert feed_type in ('atom', 'rss'), feed_type

feed = yaml.safe_load(sys.stdin)
assert_type(feed, dict)
assert_type(feed['self-url'], str)
assert_type(feed['feed-description'], str)
assert_type(feed['posts'], list)

# Compute base URL of relative URLs in the feed.
scheme, netloc, path, _, _ = urllib.parse.urlsplit(feed['self-url'])
directory = str(Path(path).parent)
base_url = urllib.parse.urlunsplit((scheme, netloc, directory, '', ''))

fg = FeedGenerator()
fg.id(feed['self-url'])
fg.title('$include(Title.in.txt)')
fg.description(feed['feed-description'])
fg.author({
    'name': '$include(Author.in.txt)',
    'email': '$include(Email.in.txt)',
})
fg.link(href=feed['self-url'], rel='alternate')
fg.link(href=feed['self-url'], rel='self')

for post in feed['posts']:
    assert_type(post, dict)
    assert_type(post['path'], str)
    assert_type(post['published'], datetime)
    updated = post.get('updated', post['published'])
    assert_type(updated, datetime)
    assert_type(post['title'], str)
    assert_type(post['summary'], str)
    post_url = base_url + '/' + post['path']
    fe = fg.add_entry()
    fe.guid(post_url, permalink=True)
    fe.link({
        'href': post_url,
        'rel': 'alternate',
    })
    fe.published(post['published'])
    fe.updated(updated)
    fe.title(post['title'])
    fe.description(post['summary'], isSummary=True)

if feed_type == 'atom':
    sys.stdout.buffer.write(fg.atom_str(pretty=True, encoding='utf-8'))
elif feed_type == 'rss':
    sys.stdout.buffer.write(fg.rss_str(pretty=True, encoding='utf-8'))
else:
    raise ValueError(f"Unknown feed type {feed_type} (should be 'atom' or 'rss')")
