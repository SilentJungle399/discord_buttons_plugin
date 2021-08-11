import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord_buttons_plugin",
    version="0.1.2",
    author="SilentJungle399",
    description="A simple module to use for buttons in discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["discord.py", "requests"],
    url="https://github.com/SilentJungle399/discord_buttons_plugin",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
