from Cocoa import NSDocument
import objc
from objc import super

class MyDocument (NSDocument):
    window = objc.IBOutlet()

    def initWithType_error_(self, tp, error):
        self = super(MyDocument, self).initWithType_error_(tp, error)
        if self is None:
            return None
        return self

    def windowNibName(self):
        return "Document"
