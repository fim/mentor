Mentor
======

A simple file sharing app over HTTP/HTTPS

Simply provide a list of files and directories to share and they will be
shared without the need for any webserver or any extra configuration. Also
supports hole punching using UPnP

Requirements
------------

 * Python (2.7 tested)
 * gevent
 * miniupnpc (if using UPnP)
 * M2Crypto  (if using SSL)

Installation
------------

```sh
$ pip install git+git://github.com/fim/mentor.git
```

Usage
-----

 * Share specific files

```sh
$ mentor file1 file2
```

* Share specific files over HTTPS

```sh
$ mentor -s file1 file2
```

* Share specific files and folders recursively with UPnP hole punching

```sh
$ mentor -u -r dir1 file1 file2
```
