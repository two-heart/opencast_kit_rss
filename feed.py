from feedgen.feed import FeedGenerator


def create_feed(feed_id, all_episodes, all_series, path):
    fg = FeedGenerator()
    fg.load_extension('podcast')

    fg.id(str(path))
    fg.link(href='https://opencast.informatik.kit.edu/engage/ui/index.html', rel='alternate')
    meta_info = get_meta_info(feed_id, all_series)  # TODO check if none
    if meta_info is None:
        raise ValueError
    fg.title(meta_info['dcTitle'])
    fg.description(meta_info.get('dcDescription', meta_info['dcTitle']))
    for item in all_episodes:
        fe = fg.add_entry()
        fe.id(item['mediapackage']['media']['track']['url'])
        fe.title(item['mediapackage']['title'] + ' ' + item['dcCreated'])
        fe.published(item['dcCreated'])
        fe.description(meta_info.get('dcDescription', 'no description'))
        fe.enclosure(item['mediapackage']['media']['track']['url'], 0,
                     item['mediapackage']['media']['track']['mimetype'])
    return fg.rss_str(pretty=True)


def get_meta_info(feed_id, all_series):
    return next((item for item in all_series if item['id'] == feed_id), None)
