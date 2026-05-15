from setuptools import setup

APP = ["部门业务机会分析.py"]
DATA_FILES = []

OPTIONS = {
    "argv_emulation": False,
    "plist": {
        "CFBundleName": "部门业务机会分析",
        "CFBundleDisplayName": "部门业务机会分析",
        "CFBundleVersion": "1.0",
        "CFBundleIdentifier": "com.analysis.sales",
        "NSHighResolutionCapable": True,
        "LSUIElement": True,
    },
    "packages": [
        "pandas",
        "numpy",
        "matplotlib",
        "docx",
        "openpyxl",
        "tkinter",
        "re",
        "os",
        "datetime",
        "collections"
    ],
    "excludes": [
        "tkinter.test",
        "matplotlib.tests",
        "numpy.testing",
        "pandas.tests",
        "unittest",
        "setuptools",
        "pip",
        "wheel"
    ],
    "optimize": 2,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)