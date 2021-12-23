

"""
Objetivo:
    clonar dados de um iterável para outro, sem gerar um elo entre os dados envolvidos
"""

# @dict @list @set

"print(1, b := True, 1, b2 := b.copy())"      # AttributeError: 'bool' object has no attribute 'copy'
"print(2, c := 0j, 2, c2 := c.copy())"        # AttributeError: 'complex' object has no attribute 'copy'
print(3, d := {'Nome': 'Juvêncio', 'ciclista': True}, 3, d2 := d.copy())
"print(4, f := 0.0, 4, f2 := f.copy())"       # AttributeError: 'float' object has no attribute 'copy'
"print(5, i := 0, 5, i2 := i.copy())"         # AttributeError: 'int' object has no attribute 'copy'
print(6, l := ['dó', 'ré', 'mi'], 6, l2 := l.copy())
"print(7, n := None, 7, n2 := n.copy())"      # AttributeError: 'NoneType' object has no attribute 'copy'
"print(8, r := range(0), 8, r2 := r.copy())"  # AttributeError: 'range' object has no attribute 'copy'
print(9, cj := {'10', 20, 30.0}, 9, cj2 := cj.copy())
"print(10, s := '_', 10, s2 := s.copy())"     # AttributeError: 'str' object has no attribute 'copy'
"print(11, t := (), 11, t2 := t.copy())"      # AttributeError: 'tuple' object has no attribute 'copy'
