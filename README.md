# bz-mass-file

This script is useful to file a lot of bug into bugzilla, by parsing a file and
using the (http://bugzilla.readthedocs.org/en/latest/api/index.html)[Bugzilla
Rest API].

You need to put a bugzilla API key in the file `key.txt` (you can get one in the
"Preferences" page on a bugzilla). Also this is hacked up and hard coded, it's
likely you need to change the code a bit.

# File format

```
<Git commit of a spec change>\n
<Summary>\n
<Description>\n
\n
Git commit of a spec change\n
Summary\n
Description\n
\n
Git commit of a spec change\n
Summary\n
Description\n
```
