from Url2mdlink.url2mdlink.url2mdlink import transform

import subprocess

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))


url = 'https://www.facebook.com'
markdown = transform(url)
print(markdown)
write_to_clipboard(markdown)

print(transform.__doc__)