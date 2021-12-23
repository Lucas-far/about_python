

"""
Objetivo:
    Uma classe/entidade não importa, o que importa são os atributos ou métodos dela
"""

from typing import Protocol

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 31:45
    """

class Curso(Protocol):  # ao receber herança 'Protocol', aparentemente, a classe torna seu escopo público
    titulo: str

    def __init__(self):
        Curso.titulo = 'Django'  # instanciação inválida, pois há herança: Protocol

def estudar(valor: Curso):
    return f'Estou estudando o curso {valor.titulo}'  # 'titulo' não pôde ser instanciado, então a função não funciona

# Mas esse atributo 'titulo', se chamado em outra classe, pode ser declarado
class BancoDeDados:
    titulo = 'Python'

print([1], estudar(BancoDeDados()))
print([2], objeto := BancoDeDados(), estudar(objeto))
print([3], estudar(Curso()))  # TypeError: Protocols cannot be instantiated

def acesso():
    """
    python / import typing / dir(typing)

    'ABCMeta', 'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager', 'AsyncGenerator', 'AsyncIterable',
    'AsyncIterator', 'Awaitable', 'BinaryIO', 'ByteString', 'CT_co', 'Callable', 'ChainMap', 'ClassVar', 'Collection',
    'Container', 'ContextManager', 'Coroutine', 'Counter', 'DefaultDict', 'Deque', 'Dict', 'EXCLUDED_ATTRIBUTES',
    'Final', 'ForwardRef', 'FrozenSet', 'Generator', 'Generic', 'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator',
    'KT', 'KeysView', 'List', 'Literal', 'Mapping', 'MappingView', 'Match', 'MethodDescriptorType', 'MethodWrapperType',
    'MutableMapping', 'MutableSequence', 'MutableSet', 'NamedTuple', 'NamedTupleMeta', 'NewType', 'NoReturn',
    'Optional', 'OrderedDict', 'Pattern', 'Protocol', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
    'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsIndex', 'SupportsInt', 'SupportsRound', 'T',
    'TYPE_CHECKING', 'T_co', 'T_contra', 'Text', 'TextIO', 'Tuple', 'Type', 'TypeVar', 'TypedDict', 'Union', 'VT',
    'VT_co', 'V_co', 'ValuesView', 'WrapperDescriptorType', '_Final', '_GenericAlias', '_Immutable', '_PROTO_WHITELIST',
    '_ProtocolMeta', '_SPECIAL_NAMES', '_SpecialForm', '_TYPING_INTERNALS', '_TypedDictMeta', '_TypingEllipsis',
    '_TypingEmpty', '_VariadicGenericAlias', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
    '__loader__', '__name__', '__package__', '__spec__', '_alias', '_allow_reckless_class_cheks', '_allowed_types',
    '_check_fails', '_check_generic', '_cleanups', '_collect_type_vars', '_dict_new', '_eval_type', '_get_defaults',
    '_get_protocol_attrs', '_is_callable_members_only', '_is_dunder', '_make_nmtuple', '_no_init', '_normalize_alias',
    '_overload_dummy', '_prohibited', '_remove_dups_flatten', '_special', '_subs_tvars', '_tp_cache', '_type_check',
    '_type_repr', '_typeddict_new', 'abstractmethod', 'cast', 'collections', 'contextlib', 'final', 'functools',
    'get_args', 'get_origin', 'get_type_hints', 'io', 'no_type_check', 'no_type_check_decorator', 'operator',
    'overload', 're', 'runtime_checkable', 'stdlib_re', 'sys', 'types'

    dir(typing.Protocol)

    '__abstractmethods__', '__class__', '__class_getitem__', '__delattr__', '__dir__', '__doc__', '__eq__',
    '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
    '__lt__', '__module__', '__ne__', '__new__', '__parameters__', '__reduce__', '__reduce_ex__', '__repr__',
    '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_abc_impl', '_is_protocol',
    '_is_runtime_protocol'
    """
