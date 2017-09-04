"""Opens a very basic print dialogue. Styling of the output of this is entirely on your instance!"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin


class PrintXBlock(XBlock):
    """
    Simple XBlock that places a button that triggers the print dialogue.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    display_name = String(display_name="Display name", default='Print')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the PrintXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/printxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/printxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/printxblock.js"))
        frag.initialize_js('PrintXBlock')
        return frag
    
    # Make fields editable in studio
    editable_fields = ('display_name')
