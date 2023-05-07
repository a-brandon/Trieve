![Logo](https://github.com/a-brandon/Trieve/blob/main/images/trieve_image.png)

# Trieve
Trieve is a simple web application built using Streamlit that automates the process of finding and downloading Spotify IDs to a text file. Typically, finding the ID of an artist requires navigating to their Spotify page and copying the ID at the end of the URL. While this is manageable for one or two artists, it becomes tedious for larger numbers. With Trieve, you can easily find and download the IDs for 10 or more artists in one go.

# Usage
Visit URL enter in the artist name (if there are multiple artists, there's a tooltip that tells you to separate artist names with a comma and a space). Artist names are case sensitive.

Trieve just makes use of Spotify's https://api.spotify.com/v1/search endpoint and builds a query string off it:
```
[spotify.search(q=f'artist:{name}', type='artist')]
```

Note that the app can go to sleep if it hasn't been used in a while. You'll see a page that prompts you to "wake it up". The process takes about two minutes for it to load again.

# Contributing
Any contributions are welcome. There are small edge cases that I'll work out in the future.
