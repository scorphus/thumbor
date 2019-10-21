# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):
    """
        Usage: /filters:blur(<radius> [, <sigma>])
        Examples of use:
            /filters:blur(1)/
            /filters:blur(4)/
            /filters:blur(4, 2)/
    """

    @filter_method(BaseFilter.PositiveNonZeroNumber, BaseFilter.DecimalNumber)
    def blur(self, radius, sigma=0):
        self.engine.blur(radius, sigma)
