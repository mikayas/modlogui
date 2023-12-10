from utils import Tags


def head(page):
    '''component for general window configuration'''

    page.title = Tags.FULLNAME
    page.window_resizable = False
    page.window_maximizable = False
    page.window_height = 580
    page.window_width = 768
    page.window_opacity = 0.95


class Head_pages:
    '''general settings components for pages'''

    HEIGHT = 500

