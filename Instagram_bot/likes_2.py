"""
This template is written by @the-unknown

What does this quickstart script aim to do?
- This is my template which includes the new QS system.
  It includes a randomizer for my hashtags... with every run, it selects 10
  random hashtags from the list.

NOTES:
- I am using the bot headless on my vServer and proxy into a Raspberry PI I
have at home, to always use my home IP to connect to Instagram.
  In my comments, I always ask for feedback, use more than 4 words and
  always have emojis.
  My comments work very well, as I get a lot of feedback to my posts and
  profile visits since I use this tactic.

  As I target mainly active accounts, I use two unfollow methods.
  The first will unfollow everyone who did not follow back within 12h.
  The second one will unfollow the followers within 24h.
"""

# !/usr/bin/python2.7
import random
from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='kryptosushi', password='danirocks!', headless_browser=False, geckodriver_path='/Users/daniel/Downloads/geckodriver')

# let's go! :>
with smart_run(session):
    hashtags = ['nft', 'nftart', 'art',
                 'digitalart', 'nfts', 'nftartist',
                 'crypto', 'cryptoart', 'nftcommunity',
                 'nftcollector', 'ethereum', 'bitcoin',
                 'blockchain', 'cryptocurrency', 'opensea',
                 'artist', 'artwork', 'eth', 'nftcollectors',
                 'cryptoartist', 'contemporaryart', 'nftdrop',
                 'nftcollectibles', 'btc', 'openseanft', 'defi',
                 'design', 'artoftheday', 'bhfyp']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:7]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=80)
    session.set_do_comment(enabled=True, percentage=80)
    session.set_comments([
                             u'Amazing!! :heart_eyes: What do '
                             u'you think of my recent nft?',
                             u'What an amazing nft! :heart_eyes: What do '
                             u'you think of my recent nft?',
                             u'What an amazing nft! :heart_eyes: I think '
                             u'you might also like mine. :wink:',
                             u'Wonderful!! :heart_eyes: Would be awesome if '
                             u'you would checkout my collection as well!',
                             u'Wonderful!! :heart_eyes: I would be honored '
                             u'if you would checkout my images and tell me '
                             u'what you think. :wink:',
                             u'This is awesome!! :heart_eyes: Any feedback '
                             u'for my collection? :wink:',
                             u'This is awesome!! :heart_eyes:  maybe you '
                             u'like my NFT\'s, too? :wink:',
                             u'I really like the way you captured this. I '
                             u'bet you like my NFT\'s, too :wink:',
                             u'I really like the way you captured this. If '
                             u'you have time, check out my NFT\'s, too. I '
                             u'bet you will like them. :wink:',
                             u'Great capture!! :smiley: :thumbsup: What do '
                             u'you think of my NFT\'s?'],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    session.like_by_tags(my_hashtags, amount=90, media=None)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='food')