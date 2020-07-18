from distutils.core import setup
setup(
    name='covid_mx_data',
    packages=['covid_mx_data'],
    version='0.1',
    license='MIT',
    description='Descarga archivos de datos de Covid 19 de la Dirección General de Epidemiología (DGE) de la Secretaría de Salud del Gobierno de México.',
    author='Iván Fouilloux',
    author_email='contacto@ivanfouilloux.com',
    url='https://github.com/ivan-fouilloux/CovidMxData',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['COVID', 'MEXICO', 'DGE', 'SSA',
              'GOB', 'MX', 'COVID19', 'COVIDMX'],
    install_requires=[            # I get to this in a second
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 5 - Production/Stable',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
