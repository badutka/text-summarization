import abc


class Pipeline(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'main') and
                callable(subclass.main) or
                NotImplemented)

    @abc.abstractmethod
    def main(self) -> None:
        """Run the particular pipeline"""
        raise NotImplementedError
