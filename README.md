ywow - year's worth of weibo
----------------------------

A simple project to contain a minimal amount of code sufficient for
fetching sample data from Sina Weibo, in support of a research project.

Based on the configuration in a local settings file, the ```fetch.py```
script will execute a call to Weibo's 'statuses/public_timeline' API
call, then store that data to a local file in utf-8-encoded JSON and a 
simplified delimited text file.  The location of these files will be under
the ```DATA_DIR``` specified in ```config.py```, and within that, under
a ```DATA_DIR/YYYY/MM/HH``` hierarchy to spread the files out.

Developed at the GWU Libraries in Washington, DC, USA.

See also LICENSE.txt.


installation
------------

Developed using python 2.7+ for deployment on ubuntu-12.04; your mileage
may vary.

* install ubuntu package dependencies:

        % sudo apt-get install git python-virtualenv s3cmd

* get this repository:

        % git clone https://github.com/gwu-libraries/ywow.git

* create and activate a virtualenv sandbox for python and dependencies:

        % virtualenv ENV
        % source ENV/bin/activate

* install requirements:

        % pip install -r requirements.txt

* create a ```data``` directory:

        % mkdir data

* copy the settings template to a local python file:

        % cp config.py.template config.py

* edit ```config.py``` appropriately, including the full absolute path
  to your ```data``` directory.

* NOTE:  you will need an active weibo API key and token.  For background
  on obtaining these, see:

        Weibo API docs: http://open.weibo.com/wiki/Oauth/authorize/en
        CMU's API guide: http://www.cs.cmu.edu/~lingwang/weiboguide/
        Example usage from python library: http://lxyu.github.io/weibo/
        Copy (fork) of above under GW Librares' github account: https://github.com/gwu-libraries/weibo

* test the script on the command line:

        % python fetch.py 
