import html
import json
from inspect import signature
from masonite.utils.helpers import flatten
from masonite.response import Response
from masonite.utils.structures import load



class InertiaResponse:

    def get_response(self):
        return self.rendered_template
