
import re
import warnings

_get_option_tmpl = """
set_option(pat, value)

Sets the value of the specified option.

Available options:

{opts_list}

Parameters
----------
pat : str
    Regexp which should match a single option.
    Note: partial matches are supported for convenience, but unless you use 
    the full option name (e.g. x.y.z.option_name), your code may break in 
    future versions if new options with similar names are introduced.
value : object
    New value of option.

Returns
-------
None

Raises
------
KeyError if no such option exists

Notes
-----
The available options with its descriptions:

{opts_desc}
"""
_global_config = {
    'sql': {
        'available_types': ['bigquery', 'postgres'],
        'type': 'bigquery'
    }
}
_registered_options = {
    'sql.available_types': ['bigquery', 'postgres'],
    'sql.type': 'bigquery'
}
_set_option_tmpl = """
set_option(pat, value)

Sets the value of the specified option.

Available options:

{opts_list}

Parameters
----------
pat : str
    Regexp which should match a single option.
    Note: partial matches are supported for convenience, but unless you use
    the full option name (e.g. x.y.z.option_name), your code may break in 
    future versions if new options with similar names are introduced.
value : object
    New value of option.

Returns
-------
None

Raises
------
KeyError if no such option exists

Notes
-----
The available options with its descriptions:

{opts_desc}
"""


class CallableDynamicDoc:
    def __init__(self, func, doc_tmpl):
        self.__doc_tmpl__ = doc_tmpl
        self.__func__ = func

    def __call__(self, *args, **kwargs):
        return self.__func__(*args, **kwargs)
class DictWrapper:
    def __init__(self, d, prefix = ""):
        object.__setattr__(self, "d", d)
        object.__setattr__(self, "prefix", prefix)

    def __setattr__(self, key, val):
        prefix = object.__getattribute__(self, "prefix")
        if prefix:
            prefix += "."
        prefix += key
        if key in self.d and not isinstance(self.d[key], dict):
            _set_option(prefix, val)
        else:
            raise KeyError("Value cannot be set to nonexisting options.")

    def __getattr__(self, key):
        prefix = object.__getattribute__(self, "prefix")
        if prefix:
            prefix += "."
        prefix += key
        try:
            v = object.__getattribute__(self, "d")[key]
        except KeyError:
            raise KeyError("No such option exists.")
        if isinstance(v, dict):
            return DictWrapper(v, prefix)
        else:
            return _get_option(prefix)

    def __dir__(self):
        return list(self.d.keys())    
def _get_option(pat):
    key = _get_single_key(pat)
    root, k = _get_root(key)
    
    return root[k]
def _get_registered_option(key):

    return _registered_options.get(key)
def _get_root(key):
    path = key.split(".")
    cursor = _global_config
    for p in path[:-1]:
        cursor = cursor[p]
    return cursor, path[-1]
def _get_single_key(pat):
    keys = _select_options(pat)
    if len(keys) == 0:
        raise KeyError("No such keys: {pat!r}".format(pat = pat))
    if len(keys) > 1:
        raise KeyError("Pattern matched multiple keys.")
    key = keys[0]
    
    return key
def _select_options(pat):
    if pat in _registered_options:
        return [pat]
    keys = sorted(_registered_options.keys())
    if pat == 'all':
        return keys
    
    return [k for k in keys if re.search(pat, k, re.I)]
def _set_option(*args, **kwargs):
    nargs = len(args)
    if not nargs or nargs % 2 != 0:
        msg = "Must provide an even number of non-keyword arguments."
        raise ValueError(msg)
    silent = kwargs.pop("silent", False)
    if kwargs:
        msg2 = '_set_option() got an unexpected keyword argument "{kwarg}"'
        raise TypeError(msg2.format(list(kwargs.keys())[0]))
    for k, v in zip(args[::2], args[1::2]):
        key = _get_single_key(k, silent)
        o = _get_registered_option(key)
        if o and o.validator:
            o.validator(v)
        
        root, k = _get_root(key)
        root[k] = v

        if o.cb:
            if silent:
                with warnings.catch_warnings(record = True):
                    o.cb(key)
            else:
                o.cb(key)

get_option = CallableDynamicDoc(_get_option, _get_option_tmpl)
options = DictWrapper(_global_config)
set_option = CallableDynamicDoc(_set_option, _set_option_tmpl)
