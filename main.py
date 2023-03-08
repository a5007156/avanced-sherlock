import requests

def check_username(username):
    variations = [
        username.replace("e", "3"),
        username.replace("a", "4"),
        username.replace("i", "1"),
        username.replace("o", "0"),
        username.replace("s", "5"),
        username.replace("g", "9"),
        username.replace("l", "1"),
        username.replace("b", "6"),
        username.replace("t", "7"),
        username.upper(),
        username.lower(),
        username.title(),
        username.swapcase(),
        username.replace(" ", ""),
        username.replace(" ", "_"),
        username.replace(" ", "-"),
        username + "_",
        username + "-",
        username + "!",
        username + "?",
        username + "123",
        username + "1234",
        username + "12345",
        username + "321",
        username + "4321",
        username + "54321",
        "the" + username,
        "the_" + username,
        "the-" + username,
        "the_" + username + "_",
        "the-" + username + "-",
        "the_" + username + "!",
        "the-" + username + "!",
        "the_" + username + "?",
        "the-" + username + "?",
        "the" + username + "123",
        "the" + username + "1234",
        "the" + username + "12345",
        "the" + username + "321",
        "the" + username + "4321",
        "the" + username + "54321",
        username + "official",
        username + "_official",
        username + "-official",
        username + "_official_",
        username + "-official-",
        username + "official!",
        username + "official?",
        username + "official123",
        username + "official1234",
        username + "official12345",
        username + "official321",
        username + "official4321",
        username + "official54321",
        username + "real",
        username + "_real",
        username + "-real",
        username + "_real_",
        username + "-real-",
        username + "real!",
        username + "real?",
        username + "real123",
        username + "real1234",
        username + "real12345",
        username + "real321",
        username + "real4321",
        username + "real54321",
    ]

    websites = [    "https://facebook.com/",    "https://twitter.com/",    "https://instagram.com/",    "https://github.com/",    "https://linkedin.com/",    "https://pinterest.com/",    "https://reddit.com/",    "https://tumblr.com/",    "https://tiktok.com/",    "https://wordpress.com/",    "https://youtube.com/",    "https://stackoverflow.com/",    "https://quora.com/",    "https://soundcloud.com/",    "https://deviantart.com/",    "https://medium.com/",    "https://vimeo.com/",    "https://myspace.com/",    "https://livejournal.com/",    "https://flickr.com/",    "https://dribbble.com/",    "https://behance.net/",    "https://angel.co/",    "https://slack.com/",    "https://bitbucket.org/",    "https://codepen.io/",    "https://coursera.org/",    "https://dailymotion.com/",    "https://discord.com/",    "https://etsy.com/",    "https://foursquare.com/",    "https://freecodecamp.org/",    "https://gitlab.com/",    "https://giphy.com/",    "https://hackernews.com/",    "https://imgur.com/",    "https://instructables.com/",    "https://kickstarter.com/",    "https://last.fm/",    "https://mixcloud.com/",    "https://producthunt.com/",    "https://skype.com/",    "https://slackware.com/",    "https://slideshare.net/",    "https://stackoverflow.com/",    "https://wikipedia.org/",    "https://wordpress.org/",    "https://yelp.com/",    "https://zillow.com/",    "https://zoom.us/"]

    results = {}

    for website in websites:
        usernames = []
        response = requests.get(website + username)

        if response.status_code == 200:
            usernames.append(username)

        for variation in variations:
            response = requests.get(website + variation)

            if response.status_code == 200:
                usernames.append(variation)

        if usernames:
            results[website] = usernames

    return results

input = input("Username to look for: ")
results = check_username(input)
for website, usernames in results.items():
    print(f"{website}: {' '.join(usernames)}")
