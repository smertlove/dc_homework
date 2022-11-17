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
        return ''.join(sorted(tuple(map(str, key)))).lower()

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


def main():
    field = Field()

    # field["a1"] =101010
    # field["a2"] =9999
    # field["b1"] =888
    # field["c123"] = 777
    # field["r4"] = 666
    # field["t6"] = 55
    # field["b356"] = 44
    # field["c2"] = 33
    # field["e4"] = 3
    # field["e5"] = 2
    # field["e6"] = 1

    # # pprint(field)
    # print("1a" in field)
    # print(field["a228"])
    # print(field["a228"] is None)
    # del field["1a"]
    # print(field["1a"])
    # for v in field:
    #     print(v)
    field[228, "t", 322] = 555
    pprint(field)

if __name__ == "__main__":
    main()
