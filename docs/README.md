# Python Client Docs generation script

For python we generate the docs using sphinx. Sphinx requires a bunch of files, some of which we include (conf.py), and some the generate_docs.py script will generate for you.

Please note: in joueur/client.py importing ErrorCode and handle_error will fail. Sphinx actually runs the client when generating docs and that fails. It's easiest to comment out that import and instead do this:

```
#from joueur.error_code import ErrorCode, handle_error
ErrorCode = {}
def handle_error():
    pass
```

That way they still exist, but do nothing, and sphinx will be happy.

In addition, make sure the version of Sphinx you install is the Python 3 version.
