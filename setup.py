"""
Script for building the PyObjCExample Mac app

Usage: python setup.py py2app
"""
from distutils.core import setup
import py2app

nib_name = 'MainMenu'
document_nib_name = "Document"
# Set the NIB name
plist = dict(
             NSMainNibFile=nib_name,
             CFBundleShortVersionString="1.0",
             NSHumanReadableCopyright="Released under the BSD license",
             # LSUIElement = True # Hide the app running in the dock
             CFBundleDocumentTypes=[
                    dict(
                        CFBundleTypeExtensions=[".gif"],
                        CFBundleTypeMIMETypes=["application/octect-stream"],
                        CFBundleTypeName="Binary",
                        CFBundleTypeRole="Editor",
                        LSTypeIsPackage=False,
                        NSDocumentClass="MyDocument",
                        NSPersistentStoreTypeKey="Binary",
                    ),
                ]
             )

OPTIONS = {
    'iconfile': 'icons/Tiff Q.icns',
    'resources': [

    ],
    'plist': plist
}

setup(
    name="Tiff Q",
    app=["main.py"],
    data_files=[nib_name + ".xib", document_nib_name + ".xib"],
    options={'py2app': OPTIONS}
)
