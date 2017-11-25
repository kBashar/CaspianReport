# CaspianReport: Interactive map

[Click here to visit!](http://modaoudi.github.io/CaspianReport)

### About
In this site you can watch CaspianReport videos of a country of your choice.
The code is pretty simple, all you need is an IDE/editor and basic knowledge in HTML,
CSS, Javascript and Python.

### Requirements
* This site site uses jVectorMap as the Javascript map library. You don't need
install it because the files are included in the repository.
But if you want to extend go to their site[jVectorMap](http://jvectormap.com/).
* You need a basic http-server to be able to run the fetching from json files.
If you work with WebStorm/PyCharm/Jetbrains you can just `run index.html`.
* Python 3
* In order to be able to make requests for Youtube videos you need an Google API key
for Youtube and put it inside the ``api.json`` file.

###TODO
* ~~Fetch all videos (script)~~
* ~~Sort videos by country (script)~~
* ~~Integrate interactive map in html~~
* ~~Make site responsive~~
* __Problem__: Better search of countries in video tags (eg. US/United States/United States [of] America)
* Make the site decent, because it looks like crap.
* Play the videos on site 