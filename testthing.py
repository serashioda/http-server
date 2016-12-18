import os
import base64

FILETYPE = {
    'jpg': 'image/jpg',
    'jpeg': 'image/jpeg',
    'txt': 'text/plain',
    'gif': 'image/gif',
    'png': 'image/png',
    'py': 'text/plain'
}
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
    elif os.path.isfile(file_path):
        #check the filetype
        file_extension = file_path.split('.')[-1]
        print('File Type:', file_extension)
        if FILETYPE[file_extension] == 'text/plain':
            with open(file_path, 'r') as myfile:
                body_content = myfile.read()
            content_type = FILETYPE[file_extension]
            print('Content Type:', content_type)
        elif FILETYPE[file_extension].split('/')[0] == 'image':
            with open(file_path, 'rb') as imageFile:
                body_content = base64.b64encode(imageFile.read())
            content_type = FILETYPE[file_extension]
            print('Content Type:', content_type)
            print('Body:', body_content)

resolve_uri('src/transferfiles/testdir/img.jpg')
