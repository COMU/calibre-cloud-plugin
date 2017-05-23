# calibre-cloud-plugin

Calibre plugin for cloud strorages

There are 4 buttons for Yandex.

->Dowload(When files deleted on site and local automaticly delete as well )
->Upload(When files deleted on local and other site automaticly delete as well)
->Pull(Fetch missing files)
->Push(Loads missing files)

This plugin has a GoogleDrive support, you can work with that your book's can storge to on google drive. 
GoogleDrive side has a 4 button.
->Auth (When you are want to login with google drive use this button)
->Deauth(This button for forget your google drive credentials)
->Download(Automaticly snyc your drive files to local files)
->Upload(Automaticly snyc your local files to drive files)


Dependency
-Webdavclient-
$sudo apt-get install libxml2-dev libxslt-dev python-dev
$sudo apt-get install libcurl4-openssl-dev python-pycurl
$pip install webdavclient 

-Pydrive
$pip install pydrive
