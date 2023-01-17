from dotenv import load_dotenv
import os
import instaloader
from time import sleep


def get_comments_from_post(shortcode):
    load_dotenv('.env')
    L = instaloader.Instaloader()
    L.login('ri_guima', 'Richard23102019*')
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    return [comment.text for comment in list(post.get_comments())]
