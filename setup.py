from setuptools import setup, find_packages

# Read the content of the README file for long description
readme = ''
try:
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
except FileNotFoundError:
    print("Warning: README.rst not found. Skipping long description.")

setup(
    name='djangoshortwalk',
    version='1.0',
    description="For irritated Django developers who type 'python manage.py' too many times...",
    long_description=readme,
    long_description_content_type='text/x-rst',
    author="Mr. Bipin Rajesh Tatkare",
    author_email="techbipinrt2526@gmail.com",
    url="https://github.com/techbipin/dj-shortwalk",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'dj=dj_shortwalk.dj_shortwalk:main',
        ],
    },
    python_requires='>=3.12',
)
