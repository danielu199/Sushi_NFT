from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username="kryptosushi", password="krypto4everyone!", geckodriver_path='/Users/daniel/Downloads/geckodriver', headless_browser=False)
session.login()

'''with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)'''

session.like_by_tags(['NFT','cryptoart','nftcollector','cryptokitties','apes','yachtclub'], amount=50,interact=True)
session.set_do_comment(True, percentage=100,)
session.set_comments(["Nice, follow @kryptosushi", "Amazing", "Super"])
session.set_do_follow(enabled=True, percentage=100)
session.set_user_interact(amount=10, randomize=True, percentage=100)

session.end()