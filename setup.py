import os
import setuptools


with open(f"{os.path.dirname(os.path.abspath(__file__))}/requirements.txt") as requirements:
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/README.md") as readme:
        setuptools.setup(
            name="rojo",
            version="1.0.2",
            description="...written in Python",  # FIXME
            long_description=readme.read(),
            long_description_content_type="text/markdown",
            author="Vladimir Chebotarev",
            author_email="vladimir.chebotarev@gmail.com",
            license="MIT",
            classifiers=[
                "Development Status :: 5 - Production/Stable",
                "Environment :: Console",
                "Intended Audience :: Developers",
                "Intended Audience :: Science/Research",
                "Intended Audience :: System Administrators",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Programming Language :: Python :: 3 :: Only",  # FIXME
                "Topic :: Scientific/Engineering",
                "Topic :: Software Development",
                "Topic :: System :: Benchmark",
                "Topic :: Utilities",
            ],
            keywords=[],  # FIXME
            project_urls={
                "Documentation": "https://github.com/excitoon/rojo/blob/master/README.md",
                "Source": "https://github.com/excitoon/rojo",
                "Tracker": "https://github.com/excitoon/rojo/issues",
            },
            url="https://github.com/excitoon/rojo",
            packages=[],
            scripts=["rojo", "rojo.cmd"],
            install_requires=requirements.read().splitlines(),
        )
