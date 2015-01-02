from distutils.core import setup
            
setup(
    name='sendIP2mail',
    version='0.1',
    author='Romanos Trechlis <r.trechlis@gmail.com>',
    url='https://github.com/romanostrechlis/sendIP2mail',

    description="Utility to fetch your external IP address using ipgetter and send it to your email account",
    license="GNU2"
)

# this setup adds the script to Schedulled task in windows 7
import platform
if platform.system() == 'Windows' and platform.release() == '7':

    import os
    os.system('mkdir c:\sendIP')
    os.system('cp -r sendIP2mail.py c:\sendIP\sendIP2mail.py')
    os.system('cp -r myip.dat c:\sendIP\myip.dat')
    os.chmod('c:\sendIP\myip.dat',0o666)
    os.chmod('c:\sendIP\sendIP2mail.py',0o666)

    p = os.popen('attrib +h ' + 'c:\sendIP') # making the folder hidden
    p.close()

    os.system('SchTasks /Create /SC HOURLY /TN "IP Notification Change" /TR "python c:\sendIP\sendIP2mail.py"')
else:
    print "The script must be run manually"
