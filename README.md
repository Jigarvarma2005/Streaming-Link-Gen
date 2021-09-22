# What is this repo about?
This is a telegram bot writen in python for genrating streaming links

# Demo BOT LINK:
<a href="https://t.me/StreamingLinkRobot"><img src="https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram"></a>

# Features supported:
- Stream m3u8 links
- Stream mpd links
- Stream brightcove video using video id
- Stream JW Player video using video id
- Stream Telegram media

# How to deploy?
Deploying is pretty much straight forward and is divided into several steps as follows:

### Heroku Deploy:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Jigarvarma2005/Streaming-Link-Gen)

# How to get token.pickle file (Recommnded)

- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Other and Create.
- Use the download button to download your credentials.
- Move that file to the root of mirror-bot, and rename it to credentials.json
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate token file (token.pickle) for Google Drive:
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```

# Using service accounts for uploading to avoid user rate limit
For Service Account to work, you must set USE_SERVICE_ACCOUNTS="True" in config file or environment variables
Many thanks to [AutoRClone](https://github.com/xyou365/AutoRclone) for the scripts
**NOTE:** Using service accounts is only recommended while uploading to a team drive.
## Generating service accounts
Step 1. Generate service accounts [What is service account](https://cloud.google.com/iam/docs/service-accounts)
---------------------------------
Let us create only the service accounts that we need. 
**Warning:** abuse of this feature is not the aim of this project and we do **NOT** recommend that you make a lot of projects, just one project and 100 sa allow you plenty of use, its also possible that over abuse might get your projects banned by google. 

```
Note: 1 service account can copy around 750gb a day, 1 project can make 100 service accounts so that's 75tb a day, for most users this should easily suffice. 
```

`python3 gen_sa_accounts.py --quick-setup 1 --new-only`

A folder named accounts will be created which will contain keys for the service accounts

NOTE: If you have created SAs in past from this script, you can also just re download the keys by running:
```
python3 gen_sa_accounts.py --download-keys project_id
```

### Add all the service accounts to the Team Drive
- Run:
```
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```

### Follow on:
<p align="left">
<a href="https://github.com/Jigarvarma2005"><img src="https://img.shields.io/badge/GitHub-Follow%20on%20GitHub-inactive.svg?logo=github"></a>
</p>
<p align="left">
<a href="https://twitter.com/Jigarvarma2005"><img src="https://img.shields.io/badge/Twitter-Follow%20on%20Twitter-informational.svg?logo=twitter"></a>
</p>
<p align="left">
<a href="https://instagram.com/Jigarvarma2005"><img src="https://img.shields.io/badge/Instagram-Follow%20on%20Instagram-important.svg?logo=instagram"></a>
</p>

#### Support Group
- [JV Community](https://t.me/jv_community)

### Credits
- [Jigar Varma](https://github.com/jigarvarma2005)
- [lzzy12](https://github.com/lzzy12)
- [SpEcHiDe](https://github.com/SpEcHiDe)
- [Pyrogram](https://github.com/pyrogram/pyrogram)
