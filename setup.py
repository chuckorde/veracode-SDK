from distutils.core import setup
setup(
        name = 'veracode-python',
        packages = ['veracode-python'],
        version = '0.1.8',
        license = 'MIT',
        description = 'Python wrapper for the Veracode APIs',
        author = 'Chuck Orde',
        author_email = 'chuckorde@gmail.com',
        url = 'https://github.com/chuckorde/veracode-python',
        download_url = 'https://github.com/chuckorde/veracode-python/archive/v0.1.8.tar.gz',
        keywords = ['Veracode', 'Security'],
        install_requires=[
            'lxml',
            'python-dateutil',
            'requests',
            'strconv',
            'xmltodict',
        ],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
         ],
)
