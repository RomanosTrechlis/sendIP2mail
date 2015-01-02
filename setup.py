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
    os.system('SchTasks /Create /SC HOURLY /TN "IP Notification Change" /TR "python sendIP2mail.py"')
else:
    print "The script must be run manually"
