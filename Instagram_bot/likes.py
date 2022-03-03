"""
This template is written by @timgrossmann

What does this quickstart script aim to do?
- This script is automatically executed every 6h on my server via cron
"""

import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'kryptosushi'
insta_password = 'danirocks!'

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood']

friends = ['list of friends I do not want to interact with']

like_tag_list = ['nft', 'nftart', 'art',
                 'digitalart', 'nfts', 'nftartist',
                 'crypto', 'cryptoart', 'nftcommunity',
                 'nftcollector', 'ethereum', 'bitcoin',
                 'blockchain', 'cryptocurrency', 'opensea',
                 'artist', 'artwork', 'eth', 'nftcollectors',
                 'cryptoartist', 'contemporaryart', 'nftdrop',
                 'nftcollectibles', 'btc', 'openseanft', 'defi',
                 'design', 'artoftheday', 'bhfyp']

# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['vegan', 'veggie', 'plantbased']

accounts = ['accounts with similar content']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  geckodriver_path='/Users/daniel/Downloads/geckodriver',
                  headless_browser=False)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=30000,
                                    min_followers=300)

    #session.set_dont_include(friends)
    #session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 7),
                         amount=random.randint(50, 100), interact=True)

    #session.unfollow_users(amount=random.randint(75, 150),
     #                      InstapyFollowed=(True, "all"), style="FIFO",
      #                     unfollow_after=90 * 60 * 60, sleep_delay=501)

    """ Joining Engagement Pods...
    """
    photo_comments = ['Nice shot! @kryptosushi',
        'I love your profile! @kryptosushi',
        'Wonderful :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

    session.set_do_comment(enabled = False, percentage = 95)
    session.set_comments(photo_comments)
    session.join_pods(topic='food')