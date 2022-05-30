
# Python's Libraries
import enum
import logging


class BaseEnum(enum.Enum):

    @classmethod
    def has_value(cls, _value):
        return _value in cls._value2member_map_


class BaseError(Exception):

    def __init__(self, _message, _error=None, _source=None, _logger=None):
        self.logger = _logger or logging.getLogger(__name__)

        self.message = _message
        self.source = _source
        self.error = _error

        self.logger.error(self.get_FullErrorMessage())

        super().__init__(_message)

    def get_FullErrorMessage(self):
        value = f'{self.message}'
        if self.source:
            value = f'{value} ({self.source})'

        if self.error:
            value = f'{value}: {self.error}'

        return value

    def __str__(self):
        return self.get_FullErrorMessage()
