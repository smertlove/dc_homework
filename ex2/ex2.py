from pprint import pprint
import re



class Field(dict):

    _valid_key_pattern = re.compile("^(([a-zA-Z]\d+)|(\d+[a-zA-Z]))$")

    @classmethod
    def _is_key_valid(cls, key):
        if not cls._valid_key_pattern.fullmatch(key):
            return False
        return True

    @staticmethod
    def _normalise_key(key):
        if not (isinstance(key, str), isinstance(key, tuple)) or (isinstance(key, tuple) and len(key) > 2):
            raise TypeError
        return ''.join(sorted(tuple(map(str, key)), reverse=True)).lower()

    def _aplly_field_key_rules(method):
        def wrap(self, key, *args, **kwargs):
            key = self._normalise_key(key)
            if not self._is_key_valid(key):
                raise ValueError
            return method(self, key, *args, **kwargs)
        return wrap

    @_aplly_field_key_rules
    def __getitem__(self, key):
        return super().__getitem__(key)

    @_aplly_field_key_rules
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    @_aplly_field_key_rules
    def __delitem__(self, key):
        return super().__delitem__(key)

    @_aplly_field_key_rules
    def __contains__(self, key):
        return super().__contains__(self._normalise_key(key))

    @_aplly_field_key_rules
    def __missing__(self, key):
        return None

    def __iter__(self):
        return super().values().__iter__()

    def __setattr__(self, name, value):
        try:
            self.__setitem__(name, value)
        except (ValueError, TypeError):
            super().__setattr__(name, value)

    def __getattr__(self, name):
        try:
            return self.__getitem__(name)
        except (ValueError, TypeError):
            return super().__getattribute__(name)

    def __delattr__(self, name):
        try:
            self.__delitem__(name)
        except (ValueError, TypeError):
            super().__delattr__(name)



def main():
    field = Field()

    field.a1 = 45
    field.b2 = 228
    field.abcde = "qweqweqwe"
    pprint(field)
    print(field.a1)
    print(field.abcde)
    pprint(field.__dict__)
    del field.a1
    del field.abcde
    print(field)
    print(field.__dict__)


if __name__ == "__main__":
    main()
