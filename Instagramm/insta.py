import instaloader
from instaloader import Instaloader
from functions.functions import get_discount_code

GROUP_ID = 12345  # Replace with your group ID

# Create the Instaloader instance
l = Instaloader()

for post in l.get_hashtag_posts(GROUP_ID):
    if post.caption.lower() == 'хочу купон':
        # Check if user is subscribed to the group
        if post.owner_id in l.get_followers(GROUP_ID):
            # Get discount code link
            link = get_discount_code('instagram', post.owner_id)
            if link:
                # Open image and send it to the user
                image = open(link)
                l.upload_photo(image, caption="Your coupon!")
            else:
                # Send message about existing active coupon
                l.send_direct_message(post.owner_id, 'You already have an active coupon.')
        else:
            # Send message about subscription
            l.send_direct_message(post.owner_id, 'Subscribe to our channel and try again.')