# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Chart(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Chart - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'units': 'str',
            'base': 'int',
            'include_obsolete_metrics': 'bool',
            'description': 'str',
            'sources': 'list[ChartSourceQuery]',
            'no_default_events': 'bool',
            'interpolate_points': 'bool',
            'chart_settings': 'ChartSettings',
            'summarization': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'units': 'units',
            'base': 'base',
            'include_obsolete_metrics': 'includeObsoleteMetrics',
            'description': 'description',
            'sources': 'sources',
            'no_default_events': 'noDefaultEvents',
            'interpolate_points': 'interpolatePoints',
            'chart_settings': 'chartSettings',
            'summarization': 'summarization'
        }

        self._name = None
        self._units = None
        self._base = None
        self._include_obsolete_metrics = None
        self._description = None
        self._sources = None
        self._no_default_events = None
        self._interpolate_points = None
        self._chart_settings = None
        self._summarization = None

    @property
    def name(self):
        """
        Gets the name of this Chart.
        Name of the source

        :return: The name of this Chart.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Chart.
        Name of the source

        :param name: The name of this Chart.
        :type: str
        """
        self._name = name

    @property
    def units(self):
        """
        Gets the units of this Chart.
        String to label the units of the chart on the Y-axis

        :return: The units of this Chart.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this Chart.
        String to label the units of the chart on the Y-axis

        :param units: The units of this Chart.
        :type: str
        """
        self._units = units

    @property
    def base(self):
        """
        Gets the base of this Chart.
        If the chart has a log-scale Y-axis, the base for the logarithms

        :return: The base of this Chart.
        :rtype: int
        """
        return self._base

    @base.setter
    def base(self, base):
        """
        Sets the base of this Chart.
        If the chart has a log-scale Y-axis, the base for the logarithms

        :param base: The base of this Chart.
        :type: int
        """
        self._base = base

    @property
    def include_obsolete_metrics(self):
        """
        Gets the include_obsolete_metrics of this Chart.
        Whether to show obsolete metrics.  Default: false

        :return: The include_obsolete_metrics of this Chart.
        :rtype: bool
        """
        return self._include_obsolete_metrics

    @include_obsolete_metrics.setter
    def include_obsolete_metrics(self, include_obsolete_metrics):
        """
        Sets the include_obsolete_metrics of this Chart.
        Whether to show obsolete metrics.  Default: false

        :param include_obsolete_metrics: The include_obsolete_metrics of this Chart.
        :type: bool
        """
        self._include_obsolete_metrics = include_obsolete_metrics

    @property
    def description(self):
        """
        Gets the description of this Chart.
        Description of the chart

        :return: The description of this Chart.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Chart.
        Description of the chart

        :param description: The description of this Chart.
        :type: str
        """
        self._description = description

    @property
    def sources(self):
        """
        Gets the sources of this Chart.
        Query expression to plot on the chart

        :return: The sources of this Chart.
        :rtype: list[ChartSourceQuery]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this Chart.
        Query expression to plot on the chart

        :param sources: The sources of this Chart.
        :type: list[ChartSourceQuery]
        """
        self._sources = sources

    @property
    def no_default_events(self):
        """
        Gets the no_default_events of this Chart.
        Whether to hide events related to the sources in the charts produced. Default false (i.e. shows events)

        :return: The no_default_events of this Chart.
        :rtype: bool
        """
        return self._no_default_events

    @no_default_events.setter
    def no_default_events(self, no_default_events):
        """
        Sets the no_default_events of this Chart.
        Whether to hide events related to the sources in the charts produced. Default false (i.e. shows events)

        :param no_default_events: The no_default_events of this Chart.
        :type: bool
        """
        self._no_default_events = no_default_events

    @property
    def interpolate_points(self):
        """
        Gets the interpolate_points of this Chart.
        Whether to interpolate points in the charts produced. Default: true

        :return: The interpolate_points of this Chart.
        :rtype: bool
        """
        return self._interpolate_points

    @interpolate_points.setter
    def interpolate_points(self, interpolate_points):
        """
        Sets the interpolate_points of this Chart.
        Whether to interpolate points in the charts produced. Default: true

        :param interpolate_points: The interpolate_points of this Chart.
        :type: bool
        """
        self._interpolate_points = interpolate_points

    @property
    def chart_settings(self):
        """
        Gets the chart_settings of this Chart.
        Chart settings

        :return: The chart_settings of this Chart.
        :rtype: ChartSettings
        """
        return self._chart_settings

    @chart_settings.setter
    def chart_settings(self, chart_settings):
        """
        Sets the chart_settings of this Chart.
        Chart settings

        :param chart_settings: The chart_settings of this Chart.
        :type: ChartSettings
        """
        self._chart_settings = chart_settings

    @property
    def summarization(self):
        """
        Gets the summarization of this Chart.
        Summarization strategy for the chart.  MEAN is default

        :return: The summarization of this Chart.
        :rtype: str
        """
        return self._summarization

    @summarization.setter
    def summarization(self, summarization):
        """
        Sets the summarization of this Chart.
        Summarization strategy for the chart.  MEAN is default

        :param summarization: The summarization of this Chart.
        :type: str
        """
        allowed_values = ["MEAN", "MEDIAN", "MIN", "MAX", "SUM", "COUNT", "LAST", "FIRST"]
        if summarization not in allowed_values:
            raise ValueError(
                "Invalid value for `summarization`, must be one of {0}"
                .format(allowed_values)
            )
        self._summarization = summarization

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
