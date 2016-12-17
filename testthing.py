import os

print(os.path.realpath(__file__))


def resolve_uri(uri_or_error):
    """Resolve the URI and return the appropriate message."""
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), uri_or_error)
    if os.path.isdir(file_path):
        file_list = os.listdir(file_path)
        files = ''
        for file in file_list:
            files += '<ul>' + file + '</ul>'
        body_content = '<html><body>{}</body></html>'.format(files)
        content_type = 'directory'
        print(body_content, content_type)

resolve_uri('src/transferfiles/testdir')
