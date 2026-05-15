from setuptools import setup

APP = ["部门业务机会分析.py"]
DATA_FILES = []

OPTIONS = {
    "argv_emulation": True,
    "iconfile": None,
    "plist": {
        "CFBundleName": "部门业务机会分析",
        "CFBundleDisplayName": "部门业务机会分析",
        "CFBundleVersion": "1.0",
        "CFBundleIdentifier": "com.analysis.sales",
        "NSHighResolutionCapable": True,
        "LSUIElement": True,  # 不弹出黑框
    },
    "packages": [
        "pandas", "numpy", "matplotlib", "docx", "openpyxl", "tkinter"
    ],
    "excludes": [
        "tkinter.test",
        "matplotlib.tests",
        "numpy.testing",
        "pandas.tests",
        "setuptools",
        "pip",
        "wheel",
        "unittest",
        "distutils"
    ],
    "optimize": 2,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)