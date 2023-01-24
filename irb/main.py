from dotenv import load_dotenv
import os
import instaloader
import re
import pandas as pd


def get_votes_from_post(shortcode):
    load_dotenv('.env')
    L = instaloader.Instaloader()
    L.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    regex = re.compile(r'@\S+')
    result = []
    for comment in list(post.get_comments()):
        if regex.findall(comment.text):
            comment = {'author': comment.owner.username,
                       'vote': regex.findall(comment.text)[0]}
            if comment not in result:
                result.append(comment)
    return result


def generate_df(comments):
    companies = [c['vote'] for c in comments]
    unique_companies = list(dict.fromkeys([c['vote'] for c in comments]))
    df =  pd.DataFrame({'Empresa': unique_companies,
                        'Votos': [companies.count(c) for c in unique_companies]})
    return df.sort_values('Votos', ascending=False)
