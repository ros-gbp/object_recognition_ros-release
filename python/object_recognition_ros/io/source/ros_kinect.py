"""
Module defining several outputs for the object recognition pipeline
"""

from ecto_image_pipeline.io.source import create_source
from object_recognition_core.io.source import SourceBase
import ecto

########################################################################################################################

class RosKinect(ecto.BlackBox, SourceBase):
    """
    A source for any ORK pipeline that listens to Kinect topics
    """
    def __init__(self, *args, **kwargs):
        ecto.BlackBox.__init__(self, *args, **kwargs)
        SourceBase.__init__(self)

    def declare_cells(self, p):
        return {'main': create_source(*('image_pipeline', 'OpenNISubscriber'), **p)}

    def declare_forwards(self, _p):
        return ({'main': 'all'}, {'main': 'all'}, {'main': 'all'})

    def connections(self, _p):
        return [self.main]
