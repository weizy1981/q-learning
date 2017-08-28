APItoken = "109832b3c32f5f0da5b9ee4b66b981a2261b18a0063c0e3e671fe747fc6423e57d48006ad66f2b833c7a9835a53547d63dae9b734a2be1639e4ab78e9f42df56"

config = {
    "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
    raise Exception("Please set up your access token. See Qconfig.py.")
