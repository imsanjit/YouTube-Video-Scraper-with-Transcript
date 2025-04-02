# YouTube-Video-Scraper
How to Scrape YouTube Data using Python.


**Note:** Use <a href="https://colab.research.google.com/">google colab</a> to run the code

### Step 1: Get your YouTube API key
1. Go to <a href="https://console.developers.google.com/">console.developers.google.com</a>
2. Create project
3. Select project
4. Search for youtube data api v3
5. Enable api
6. Go to Credentials in the left nav.
7. Create credentials and select api key
8. Copy api key

### Step 2: Get any YouTube channel ID
1. Go to the YouTube channel
2. Copy all text after "https://www.youtube.com/channel/"

**or**
   
1. Go to the YouTube channel page.
2. "View page source" or "CRTL + U", then search for "channel/" word. You will find URL something like this: https://www.youtube.com/channel/UCtdaxC.
3. Now, copy all text after "https://www.youtube.com/channel/"

**Example:** If your youtube channel link is https://www.youtube.com/channel/UCtdaxC, pick **UCtdaxC**

### Step 3: Run all the code
1. Enter your YouTube api key (from step 1) to code
2. Enter your YouTube ID (from step 2) to code
