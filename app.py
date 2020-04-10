from flask import Flask, render_template, request, Response
import fetch
import feed
import re

app = Flask(__name__)

# remove this for production
app.config["DEBUG"] = True


@app.route('/')
def list_feeds():
    feed = fetch.all_series()
    return render_template('list_feeds.html', feed=feed)


@app.route('/feed')
def create_feed():
    feed_id = request.args.get('id')
    if not re.match('[[a-z]|[0-9]|-]+', feed_id):  # just to prevent a request to somewhere else
        return Response('not a valid id', status=400, mimetype='text/plain')
    all_episodes = fetch.all_episodes(feed_id)
    all_series = fetch.all_series()
    res = feed.create_feed(feed_id, all_episodes, all_series, request.base_url)
    return Response(res, mimetype='text/xml')


if __name__ == '__main__':
    app.run()
