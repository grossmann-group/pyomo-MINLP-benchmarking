# MINLP written by GAMS Convert at 05/07/21 17:13:05
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       362      140       12      210        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       208      168       40        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       798      762       36
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x2 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x3 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x4 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x5 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x6 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x7 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x8 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x9 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x10 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x11 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x12 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x13 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x14 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x15 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x16 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x17 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x18 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x19 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x20 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,40), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,40), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,40), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,40), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,30), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,30), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,30), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,30), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,None), initialize=0)
m.b169 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b170 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b171 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b172 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b173 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b174 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b175 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b176 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b177 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b178 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b179 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b180 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b181 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b182 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b183 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b184 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b185 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b186 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b187 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b188 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b189 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b190 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b191 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b192 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b193 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b194 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b195 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b196 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b197 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b198 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b199 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b200 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b201 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b202 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b203 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b204 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b205 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b206 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b207 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b208 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=maximize, expr= -m.x21 - m.x22 - m.x23 - m.x24 + 5 *
    m.x45 + 10 * m.x46 + 5 * m.x47 + 10 * m.x48 - 2 * m.x65 - m.x66 - 2 * m.x67
    - m.x68 + 80 * m.x69 + 90 * m.x70 + 120 * m.x71 + 100 * m.x72 + 285 *
    m.x73 + 390 * m.x74 + 350 * m.x75 + 300 * m.x76 + 290 * m.x77 + 405 * m.x78
    + 190 * m.x79 + 340 * m.x80 - 5 * m.b189 - 4 * m.b190 - 6 * m.b191 - 3 *
    m.b192 - 8 * m.b193 - 7 * m.b194 - 6 * m.b195 - 5 * m.b196 - 6 * m.b197 - 9
    * m.b198 - 4 * m.b199 - 3 * m.b200 - 10 * m.b201 - 9 * m.b202 - 5 * m.b203
    - 6 * m.b204 - 6 * m.b205 - 10 * m.b206 - 6 * m.b207 - 9 * m.b208)

m.e1 = Constraint(expr= m.x21 - m.x25 - m.x29 == 0)
m.e2 = Constraint(expr= m.x22 - m.x26 - m.x30 == 0)
m.e3 = Constraint(expr= m.x23 - m.x27 - m.x31 == 0)
m.e4 = Constraint(expr= m.x24 - m.x28 - m.x32 == 0)
m.e5 = Constraint(expr= -m.x33 - m.x37 + m.x41 == 0)
m.e6 = Constraint(expr= -m.x34 - m.x38 + m.x42 == 0)
m.e7 = Constraint(expr= -m.x35 - m.x39 + m.x43 == 0)
m.e8 = Constraint(expr= -m.x36 - m.x40 + m.x44 == 0)
m.e9 = Constraint(expr= m.x41 - m.x45 - m.x49 == 0)
m.e10 = Constraint(expr= m.x42 - m.x46 - m.x50 == 0)
m.e11 = Constraint(expr= m.x43 - m.x47 - m.x51 == 0)
m.e12 = Constraint(expr= m.x44 - m.x48 - m.x52 == 0)
m.e13 = Constraint(expr= m.x49 - m.x53 - m.x57 - m.x61 == 0)
m.e14 = Constraint(expr= m.x50 - m.x54 - m.x58 - m.x62 == 0)
m.e15 = Constraint(expr= m.x51 - m.x55 - m.x59 - m.x63 == 0)
m.e16 = Constraint(expr= m.x52 - m.x56 - m.x60 - m.x64 == 0)
m.e17 = Constraint(expr= (m.x97 / (0.001 + 0.999 * m.b169) - log(m.x81 / (0.001
    + 0.999 * m.b169) + 1)) * (0.001 + 0.999 * m.b169) <= 0)
m.e18 = Constraint(expr= (m.x98 / (0.001 + 0.999 * m.b170) - log(m.x82 / (0.001
    + 0.999 * m.b170) + 1)) * (0.001 + 0.999 * m.b170) <= 0)
m.e19 = Constraint(expr= (m.x99 / (0.001 + 0.999 * m.b171) - log(m.x83 / (0.001
    + 0.999 * m.b171) + 1)) * (0.001 + 0.999 * m.b171) <= 0)
m.e20 = Constraint(expr= (m.x100 / (0.001 + 0.999 * m.b172) - log(m.x84 / (
    0.001 + 0.999 * m.b172) + 1)) * (0.001 + 0.999 * m.b172) <= 0)
m.e21 = Constraint(expr= m.x85 == 0)
m.e22 = Constraint(expr= m.x86 == 0)
m.e23 = Constraint(expr= m.x87 == 0)
m.e24 = Constraint(expr= m.x88 == 0)
m.e25 = Constraint(expr= m.x101 == 0)
m.e26 = Constraint(expr= m.x102 == 0)
m.e27 = Constraint(expr= m.x103 == 0)
m.e28 = Constraint(expr= m.x104 == 0)
m.e29 = Constraint(expr= m.x25 - m.x81 - m.x85 == 0)
m.e30 = Constraint(expr= m.x26 - m.x82 - m.x86 == 0)
m.e31 = Constraint(expr= m.x27 - m.x83 - m.x87 == 0)
m.e32 = Constraint(expr= m.x28 - m.x84 - m.x88 == 0)
m.e33 = Constraint(expr= m.x33 - m.x97 - m.x101 == 0)
m.e34 = Constraint(expr= m.x34 - m.x98 - m.x102 == 0)
m.e35 = Constraint(expr= m.x35 - m.x99 - m.x103 == 0)
m.e36 = Constraint(expr= m.x36 - m.x100 - m.x104 == 0)
m.e37 = Constraint(expr= m.x81 - 40 * m.b169 <= 0)
m.e38 = Constraint(expr= m.x82 - 40 * m.b170 <= 0)
m.e39 = Constraint(expr= m.x83 - 40 * m.b171 <= 0)
m.e40 = Constraint(expr= m.x84 - 40 * m.b172 <= 0)
m.e41 = Constraint(expr= m.x85 + 40 * m.b169 <= 40)
m.e42 = Constraint(expr= m.x86 + 40 * m.b170 <= 40)
m.e43 = Constraint(expr= m.x87 + 40 * m.b171 <= 40)
m.e44 = Constraint(expr= m.x88 + 40 * m.b172 <= 40)
m.e45 = Constraint(expr= m.x97 - 3.71357206670431 * m.b169 <= 0)
m.e46 = Constraint(expr= m.x98 - 3.71357206670431 * m.b170 <= 0)
m.e47 = Constraint(expr= m.x99 - 3.71357206670431 * m.b171 <= 0)
m.e48 = Constraint(expr= m.x100 - 3.71357206670431 * m.b172 <= 0)
m.e49 = Constraint(expr= m.x101 + 3.71357206670431 * m.b169
    <= 3.71357206670431)
m.e50 = Constraint(expr= m.x102 + 3.71357206670431 * m.b170
    <= 3.71357206670431)
m.e51 = Constraint(expr= m.x103 + 3.71357206670431 * m.b171
    <= 3.71357206670431)
m.e52 = Constraint(expr= m.x104 + 3.71357206670431 * m.b172
    <= 3.71357206670431)
m.e53 = Constraint(expr= (m.x105 / (0.001 + 0.999 * m.b173) - 1.2 * log(m.x89
    / (0.001 + 0.999 * m.b173) + 1)) * (0.001 + 0.999 * m.b173) <= 0)
m.e54 = Constraint(expr= (m.x106 / (0.001 + 0.999 * m.b174) - 1.2 * log(m.x90
    / (0.001 + 0.999 * m.b174) + 1)) * (0.001 + 0.999 * m.b174) <= 0)
m.e55 = Constraint(expr= (m.x107 / (0.001 + 0.999 * m.b175) - 1.2 * log(m.x91
    / (0.001 + 0.999 * m.b175) + 1)) * (0.001 + 0.999 * m.b175) <= 0)
m.e56 = Constraint(expr= (m.x108 / (0.001 + 0.999 * m.b176) - 1.2 * log(m.x92
    / (0.001 + 0.999 * m.b176) + 1)) * (0.001 + 0.999 * m.b176) <= 0)
m.e57 = Constraint(expr= m.x93 == 0)
m.e58 = Constraint(expr= m.x94 == 0)
m.e59 = Constraint(expr= m.x95 == 0)
m.e60 = Constraint(expr= m.x96 == 0)
m.e61 = Constraint(expr= m.x109 == 0)
m.e62 = Constraint(expr= m.x110 == 0)
m.e63 = Constraint(expr= m.x111 == 0)
m.e64 = Constraint(expr= m.x112 == 0)
m.e65 = Constraint(expr= m.x29 - m.x89 - m.x93 == 0)
m.e66 = Constraint(expr= m.x30 - m.x90 - m.x94 == 0)
m.e67 = Constraint(expr= m.x31 - m.x91 - m.x95 == 0)
m.e68 = Constraint(expr= m.x32 - m.x92 - m.x96 == 0)
m.e69 = Constraint(expr= m.x37 - m.x105 - m.x109 == 0)
m.e70 = Constraint(expr= m.x38 - m.x106 - m.x110 == 0)
m.e71 = Constraint(expr= m.x39 - m.x107 - m.x111 == 0)
m.e72 = Constraint(expr= m.x40 - m.x108 - m.x112 == 0)
m.e73 = Constraint(expr= m.x89 - 40 * m.b173 <= 0)
m.e74 = Constraint(expr= m.x90 - 40 * m.b174 <= 0)
m.e75 = Constraint(expr= m.x91 - 40 * m.b175 <= 0)
m.e76 = Constraint(expr= m.x92 - 40 * m.b176 <= 0)
m.e77 = Constraint(expr= m.x93 + 40 * m.b173 <= 40)
m.e78 = Constraint(expr= m.x94 + 40 * m.b174 <= 40)
m.e79 = Constraint(expr= m.x95 + 40 * m.b175 <= 40)
m.e80 = Constraint(expr= m.x96 + 40 * m.b176 <= 40)
m.e81 = Constraint(expr= m.x105 - 4.45628648004517 * m.b173 <= 0)
m.e82 = Constraint(expr= m.x106 - 4.45628648004517 * m.b174 <= 0)
m.e83 = Constraint(expr= m.x107 - 4.45628648004517 * m.b175 <= 0)
m.e84 = Constraint(expr= m.x108 - 4.45628648004517 * m.b176 <= 0)
m.e85 = Constraint(expr= m.x109 + 4.45628648004517 * m.b173
    <= 4.45628648004517)
m.e86 = Constraint(expr= m.x110 + 4.45628648004517 * m.b174
    <= 4.45628648004517)
m.e87 = Constraint(expr= m.x111 + 4.45628648004517 * m.b175
    <= 4.45628648004517)
m.e88 = Constraint(expr= m.x112 + 4.45628648004517 * m.b176
    <= 4.45628648004517)
m.e89 = Constraint(expr= -0.75 * m.x113 + m.x145 == 0)
m.e90 = Constraint(expr= -0.75 * m.x114 + m.x146 == 0)
m.e91 = Constraint(expr= -0.75 * m.x115 + m.x147 == 0)
m.e92 = Constraint(expr= -0.75 * m.x116 + m.x148 == 0)
m.e93 = Constraint(expr= m.x117 == 0)
m.e94 = Constraint(expr= m.x118 == 0)
m.e95 = Constraint(expr= m.x119 == 0)
m.e96 = Constraint(expr= m.x120 == 0)
m.e97 = Constraint(expr= m.x149 == 0)
m.e98 = Constraint(expr= m.x150 == 0)
m.e99 = Constraint(expr= m.x151 == 0)
m.e100 = Constraint(expr= m.x152 == 0)
m.e101 = Constraint(expr= m.x53 - m.x113 - m.x117 == 0)
m.e102 = Constraint(expr= m.x54 - m.x114 - m.x118 == 0)
m.e103 = Constraint(expr= m.x55 - m.x115 - m.x119 == 0)
m.e104 = Constraint(expr= m.x56 - m.x116 - m.x120 == 0)
m.e105 = Constraint(expr= m.x69 - m.x145 - m.x149 == 0)
m.e106 = Constraint(expr= m.x70 - m.x146 - m.x150 == 0)
m.e107 = Constraint(expr= m.x71 - m.x147 - m.x151 == 0)
m.e108 = Constraint(expr= m.x72 - m.x148 - m.x152 == 0)
m.e109 = Constraint(expr= m.x113 - 4.45628648004517 * m.b177 <= 0)
m.e110 = Constraint(expr= m.x114 - 4.45628648004517 * m.b178 <= 0)
m.e111 = Constraint(expr= m.x115 - 4.45628648004517 * m.b179 <= 0)
m.e112 = Constraint(expr= m.x116 - 4.45628648004517 * m.b180 <= 0)
m.e113 = Constraint(expr= m.x117 + 4.45628648004517 * m.b177
    <= 4.45628648004517)
m.e114 = Constraint(expr= m.x118 + 4.45628648004517 * m.b178
    <= 4.45628648004517)
m.e115 = Constraint(expr= m.x119 + 4.45628648004517 * m.b179
    <= 4.45628648004517)
m.e116 = Constraint(expr= m.x120 + 4.45628648004517 * m.b180
    <= 4.45628648004517)
m.e117 = Constraint(expr= m.x145 - 3.34221486003388 * m.b177 <= 0)
m.e118 = Constraint(expr= m.x146 - 3.34221486003388 * m.b178 <= 0)
m.e119 = Constraint(expr= m.x147 - 3.34221486003388 * m.b179 <= 0)
m.e120 = Constraint(expr= m.x148 - 3.34221486003388 * m.b180 <= 0)
m.e121 = Constraint(expr= m.x149 + 3.34221486003388 * m.b177
    <= 3.34221486003388)
m.e122 = Constraint(expr= m.x150 + 3.34221486003388 * m.b178
    <= 3.34221486003388)
m.e123 = Constraint(expr= m.x151 + 3.34221486003388 * m.b179
    <= 3.34221486003388)
m.e124 = Constraint(expr= m.x152 + 3.34221486003388 * m.b180
    <= 3.34221486003388)
m.e125 = Constraint(expr= (m.x153 / (0.001 + 0.999 * m.b181) - 1.5 * log(m.x121
    / (0.001 + 0.999 * m.b181) + 1)) * (0.001 + 0.999 * m.b181) <= 0)
m.e126 = Constraint(expr= (m.x154 / (0.001 + 0.999 * m.b182) - 1.5 * log(m.x122
    / (0.001 + 0.999 * m.b182) + 1)) * (0.001 + 0.999 * m.b182) <= 0)
m.e127 = Constraint(expr= (m.x155 / (0.001 + 0.999 * m.b183) - 1.5 * log(m.x123
    / (0.001 + 0.999 * m.b183) + 1)) * (0.001 + 0.999 * m.b183) <= 0)
m.e128 = Constraint(expr= (m.x156 / (0.001 + 0.999 * m.b184) - 1.5 * log(m.x124
    / (0.001 + 0.999 * m.b184) + 1)) * (0.001 + 0.999 * m.b184) <= 0)
m.e129 = Constraint(expr= m.x125 == 0)
m.e130 = Constraint(expr= m.x126 == 0)
m.e131 = Constraint(expr= m.x127 == 0)
m.e132 = Constraint(expr= m.x128 == 0)
m.e133 = Constraint(expr= m.x157 == 0)
m.e134 = Constraint(expr= m.x158 == 0)
m.e135 = Constraint(expr= m.x159 == 0)
m.e136 = Constraint(expr= m.x160 == 0)
m.e137 = Constraint(expr= m.x57 - m.x121 - m.x125 == 0)
m.e138 = Constraint(expr= m.x58 - m.x122 - m.x126 == 0)
m.e139 = Constraint(expr= m.x59 - m.x123 - m.x127 == 0)
m.e140 = Constraint(expr= m.x60 - m.x124 - m.x128 == 0)
m.e141 = Constraint(expr= m.x73 - m.x153 - m.x157 == 0)
m.e142 = Constraint(expr= m.x74 - m.x154 - m.x158 == 0)
m.e143 = Constraint(expr= m.x75 - m.x155 - m.x159 == 0)
m.e144 = Constraint(expr= m.x76 - m.x156 - m.x160 == 0)
m.e145 = Constraint(expr= m.x121 - 4.45628648004517 * m.b181 <= 0)
m.e146 = Constraint(expr= m.x122 - 4.45628648004517 * m.b182 <= 0)
m.e147 = Constraint(expr= m.x123 - 4.45628648004517 * m.b183 <= 0)
m.e148 = Constraint(expr= m.x124 - 4.45628648004517 * m.b184 <= 0)
m.e149 = Constraint(expr= m.x125 + 4.45628648004517 * m.b181
    <= 4.45628648004517)
m.e150 = Constraint(expr= m.x126 + 4.45628648004517 * m.b182
    <= 4.45628648004517)
m.e151 = Constraint(expr= m.x127 + 4.45628648004517 * m.b183
    <= 4.45628648004517)
m.e152 = Constraint(expr= m.x128 + 4.45628648004517 * m.b184
    <= 4.45628648004517)
m.e153 = Constraint(expr= m.x153 - 2.54515263975353 * m.b181 <= 0)
m.e154 = Constraint(expr= m.x154 - 2.54515263975353 * m.b182 <= 0)
m.e155 = Constraint(expr= m.x155 - 2.54515263975353 * m.b183 <= 0)
m.e156 = Constraint(expr= m.x156 - 2.54515263975353 * m.b184 <= 0)
m.e157 = Constraint(expr= m.x157 + 2.54515263975353 * m.b181
    <= 2.54515263975353)
m.e158 = Constraint(expr= m.x158 + 2.54515263975353 * m.b182
    <= 2.54515263975353)
m.e159 = Constraint(expr= m.x159 + 2.54515263975353 * m.b183
    <= 2.54515263975353)
m.e160 = Constraint(expr= m.x160 + 2.54515263975353 * m.b184
    <= 2.54515263975353)
m.e161 = Constraint(expr= -m.x129 + m.x161 == 0)
m.e162 = Constraint(expr= -m.x130 + m.x162 == 0)
m.e163 = Constraint(expr= -m.x131 + m.x163 == 0)
m.e164 = Constraint(expr= -m.x132 + m.x164 == 0)
m.e165 = Constraint(expr= -0.5 * m.x137 + m.x161 == 0)
m.e166 = Constraint(expr= -0.5 * m.x138 + m.x162 == 0)
m.e167 = Constraint(expr= -0.5 * m.x139 + m.x163 == 0)
m.e168 = Constraint(expr= -0.5 * m.x140 + m.x164 == 0)
m.e169 = Constraint(expr= m.x133 == 0)
m.e170 = Constraint(expr= m.x134 == 0)
m.e171 = Constraint(expr= m.x135 == 0)
m.e172 = Constraint(expr= m.x136 == 0)
m.e173 = Constraint(expr= m.x141 == 0)
m.e174 = Constraint(expr= m.x142 == 0)
m.e175 = Constraint(expr= m.x143 == 0)
m.e176 = Constraint(expr= m.x144 == 0)
m.e177 = Constraint(expr= m.x165 == 0)
m.e178 = Constraint(expr= m.x166 == 0)
m.e179 = Constraint(expr= m.x167 == 0)
m.e180 = Constraint(expr= m.x168 == 0)
m.e181 = Constraint(expr= m.x61 - m.x129 - m.x133 == 0)
m.e182 = Constraint(expr= m.x62 - m.x130 - m.x134 == 0)
m.e183 = Constraint(expr= m.x63 - m.x131 - m.x135 == 0)
m.e184 = Constraint(expr= m.x64 - m.x132 - m.x136 == 0)
m.e185 = Constraint(expr= m.x65 - m.x137 - m.x141 == 0)
m.e186 = Constraint(expr= m.x66 - m.x138 - m.x142 == 0)
m.e187 = Constraint(expr= m.x67 - m.x139 - m.x143 == 0)
m.e188 = Constraint(expr= m.x68 - m.x140 - m.x144 == 0)
m.e189 = Constraint(expr= m.x77 - m.x161 - m.x165 == 0)
m.e190 = Constraint(expr= m.x78 - m.x162 - m.x166 == 0)
m.e191 = Constraint(expr= m.x79 - m.x163 - m.x167 == 0)
m.e192 = Constraint(expr= m.x80 - m.x164 - m.x168 == 0)
m.e193 = Constraint(expr= m.x129 - 4.45628648004517 * m.b185 <= 0)
m.e194 = Constraint(expr= m.x130 - 4.45628648004517 * m.b186 <= 0)
m.e195 = Constraint(expr= m.x131 - 4.45628648004517 * m.b187 <= 0)
m.e196 = Constraint(expr= m.x132 - 4.45628648004517 * m.b188 <= 0)
m.e197 = Constraint(expr= m.x133 + 4.45628648004517 * m.b185
    <= 4.45628648004517)
m.e198 = Constraint(expr= m.x134 + 4.45628648004517 * m.b186
    <= 4.45628648004517)
m.e199 = Constraint(expr= m.x135 + 4.45628648004517 * m.b187
    <= 4.45628648004517)
m.e200 = Constraint(expr= m.x136 + 4.45628648004517 * m.b188
    <= 4.45628648004517)
m.e201 = Constraint(expr= m.x137 - 30 * m.b185 <= 0)
m.e202 = Constraint(expr= m.x138 - 30 * m.b186 <= 0)
m.e203 = Constraint(expr= m.x139 - 30 * m.b187 <= 0)
m.e204 = Constraint(expr= m.x140 - 30 * m.b188 <= 0)
m.e205 = Constraint(expr= m.x141 + 30 * m.b185 <= 30)
m.e206 = Constraint(expr= m.x142 + 30 * m.b186 <= 30)
m.e207 = Constraint(expr= m.x143 + 30 * m.b187 <= 30)
m.e208 = Constraint(expr= m.x144 + 30 * m.b188 <= 30)
m.e209 = Constraint(expr= m.x161 - 15 * m.b185 <= 0)
m.e210 = Constraint(expr= m.x162 - 15 * m.b186 <= 0)
m.e211 = Constraint(expr= m.x163 - 15 * m.b187 <= 0)
m.e212 = Constraint(expr= m.x164 - 15 * m.b188 <= 0)
m.e213 = Constraint(expr= m.x165 + 15 * m.b185 <= 15)
m.e214 = Constraint(expr= m.x166 + 15 * m.b186 <= 15)
m.e215 = Constraint(expr= m.x167 + 15 * m.b187 <= 15)
m.e216 = Constraint(expr= m.x168 + 15 * m.b188 <= 15)
m.e217 = Constraint(expr= m.x1 + 5 * m.b189 == 0)
m.e218 = Constraint(expr= m.x2 + 4 * m.b190 == 0)
m.e219 = Constraint(expr= m.x3 + 6 * m.b191 == 0)
m.e220 = Constraint(expr= m.x4 + 3 * m.b192 == 0)
m.e221 = Constraint(expr= m.x5 + 8 * m.b193 == 0)
m.e222 = Constraint(expr= m.x6 + 7 * m.b194 == 0)
m.e223 = Constraint(expr= m.x7 + 6 * m.b195 == 0)
m.e224 = Constraint(expr= m.x8 + 5 * m.b196 == 0)
m.e225 = Constraint(expr= m.x9 + 6 * m.b197 == 0)
m.e226 = Constraint(expr= m.x10 + 9 * m.b198 == 0)
m.e227 = Constraint(expr= m.x11 + 4 * m.b199 == 0)
m.e228 = Constraint(expr= m.x12 + 3 * m.b200 == 0)
m.e229 = Constraint(expr= m.x13 + 10 * m.b201 == 0)
m.e230 = Constraint(expr= m.x14 + 9 * m.b202 == 0)
m.e231 = Constraint(expr= m.x15 + 5 * m.b203 == 0)
m.e232 = Constraint(expr= m.x16 + 6 * m.b204 == 0)
m.e233 = Constraint(expr= m.x17 + 6 * m.b205 == 0)
m.e234 = Constraint(expr= m.x18 + 10 * m.b206 == 0)
m.e235 = Constraint(expr= m.x19 + 6 * m.b207 == 0)
m.e236 = Constraint(expr= m.x20 + 9 * m.b208 == 0)
m.e237 = Constraint(expr= m.b169 - m.b170 <= 0)
m.e238 = Constraint(expr= m.b169 - m.b171 <= 0)
m.e239 = Constraint(expr= m.b169 - m.b172 <= 0)
m.e240 = Constraint(expr= m.b170 - m.b171 <= 0)
m.e241 = Constraint(expr= m.b170 - m.b172 <= 0)
m.e242 = Constraint(expr= m.b171 - m.b172 <= 0)
m.e243 = Constraint(expr= m.b173 - m.b174 <= 0)
m.e244 = Constraint(expr= m.b173 - m.b175 <= 0)
m.e245 = Constraint(expr= m.b173 - m.b176 <= 0)
m.e246 = Constraint(expr= m.b174 - m.b175 <= 0)
m.e247 = Constraint(expr= m.b174 - m.b176 <= 0)
m.e248 = Constraint(expr= m.b175 - m.b176 <= 0)
m.e249 = Constraint(expr= m.b177 - m.b178 <= 0)
m.e250 = Constraint(expr= m.b177 - m.b179 <= 0)
m.e251 = Constraint(expr= m.b177 - m.b180 <= 0)
m.e252 = Constraint(expr= m.b178 - m.b179 <= 0)
m.e253 = Constraint(expr= m.b178 - m.b180 <= 0)
m.e254 = Constraint(expr= m.b179 - m.b180 <= 0)
m.e255 = Constraint(expr= m.b181 - m.b182 <= 0)
m.e256 = Constraint(expr= m.b181 - m.b183 <= 0)
m.e257 = Constraint(expr= m.b181 - m.b184 <= 0)
m.e258 = Constraint(expr= m.b182 - m.b183 <= 0)
m.e259 = Constraint(expr= m.b182 - m.b184 <= 0)
m.e260 = Constraint(expr= m.b183 - m.b184 <= 0)
m.e261 = Constraint(expr= m.b185 - m.b186 <= 0)
m.e262 = Constraint(expr= m.b185 - m.b187 <= 0)
m.e263 = Constraint(expr= m.b185 - m.b188 <= 0)
m.e264 = Constraint(expr= m.b186 - m.b187 <= 0)
m.e265 = Constraint(expr= m.b186 - m.b188 <= 0)
m.e266 = Constraint(expr= m.b187 - m.b188 <= 0)
m.e267 = Constraint(expr= m.b189 + m.b190 <= 1)
m.e268 = Constraint(expr= m.b189 + m.b191 <= 1)
m.e269 = Constraint(expr= m.b189 + m.b192 <= 1)
m.e270 = Constraint(expr= m.b189 + m.b190 <= 1)
m.e271 = Constraint(expr= m.b190 + m.b191 <= 1)
m.e272 = Constraint(expr= m.b190 + m.b192 <= 1)
m.e273 = Constraint(expr= m.b189 + m.b191 <= 1)
m.e274 = Constraint(expr= m.b190 + m.b191 <= 1)
m.e275 = Constraint(expr= m.b191 + m.b192 <= 1)
m.e276 = Constraint(expr= m.b189 + m.b192 <= 1)
m.e277 = Constraint(expr= m.b190 + m.b192 <= 1)
m.e278 = Constraint(expr= m.b191 + m.b192 <= 1)
m.e279 = Constraint(expr= m.b193 + m.b194 <= 1)
m.e280 = Constraint(expr= m.b193 + m.b195 <= 1)
m.e281 = Constraint(expr= m.b193 + m.b196 <= 1)
m.e282 = Constraint(expr= m.b193 + m.b194 <= 1)
m.e283 = Constraint(expr= m.b194 + m.b195 <= 1)
m.e284 = Constraint(expr= m.b194 + m.b196 <= 1)
m.e285 = Constraint(expr= m.b193 + m.b195 <= 1)
m.e286 = Constraint(expr= m.b194 + m.b195 <= 1)
m.e287 = Constraint(expr= m.b195 + m.b196 <= 1)
m.e288 = Constraint(expr= m.b193 + m.b196 <= 1)
m.e289 = Constraint(expr= m.b194 + m.b196 <= 1)
m.e290 = Constraint(expr= m.b195 + m.b196 <= 1)
m.e291 = Constraint(expr= m.b197 + m.b198 <= 1)
m.e292 = Constraint(expr= m.b197 + m.b199 <= 1)
m.e293 = Constraint(expr= m.b197 + m.b200 <= 1)
m.e294 = Constraint(expr= m.b197 + m.b198 <= 1)
m.e295 = Constraint(expr= m.b198 + m.b199 <= 1)
m.e296 = Constraint(expr= m.b198 + m.b200 <= 1)
m.e297 = Constraint(expr= m.b197 + m.b199 <= 1)
m.e298 = Constraint(expr= m.b198 + m.b199 <= 1)
m.e299 = Constraint(expr= m.b199 + m.b200 <= 1)
m.e300 = Constraint(expr= m.b197 + m.b200 <= 1)
m.e301 = Constraint(expr= m.b198 + m.b200 <= 1)
m.e302 = Constraint(expr= m.b199 + m.b200 <= 1)
m.e303 = Constraint(expr= m.b201 + m.b202 <= 1)
m.e304 = Constraint(expr= m.b201 + m.b203 <= 1)
m.e305 = Constraint(expr= m.b201 + m.b204 <= 1)
m.e306 = Constraint(expr= m.b201 + m.b202 <= 1)
m.e307 = Constraint(expr= m.b202 + m.b203 <= 1)
m.e308 = Constraint(expr= m.b202 + m.b204 <= 1)
m.e309 = Constraint(expr= m.b201 + m.b203 <= 1)
m.e310 = Constraint(expr= m.b202 + m.b203 <= 1)
m.e311 = Constraint(expr= m.b203 + m.b204 <= 1)
m.e312 = Constraint(expr= m.b201 + m.b204 <= 1)
m.e313 = Constraint(expr= m.b202 + m.b204 <= 1)
m.e314 = Constraint(expr= m.b203 + m.b204 <= 1)
m.e315 = Constraint(expr= m.b205 + m.b206 <= 1)
m.e316 = Constraint(expr= m.b205 + m.b207 <= 1)
m.e317 = Constraint(expr= m.b205 + m.b208 <= 1)
m.e318 = Constraint(expr= m.b205 + m.b206 <= 1)
m.e319 = Constraint(expr= m.b206 + m.b207 <= 1)
m.e320 = Constraint(expr= m.b206 + m.b208 <= 1)
m.e321 = Constraint(expr= m.b205 + m.b207 <= 1)
m.e322 = Constraint(expr= m.b206 + m.b207 <= 1)
m.e323 = Constraint(expr= m.b207 + m.b208 <= 1)
m.e324 = Constraint(expr= m.b205 + m.b208 <= 1)
m.e325 = Constraint(expr= m.b206 + m.b208 <= 1)
m.e326 = Constraint(expr= m.b207 + m.b208 <= 1)
m.e327 = Constraint(expr= m.b169 - m.b189 <= 0)
m.e328 = Constraint(expr= -m.b169 + m.b170 - m.b190 <= 0)
m.e329 = Constraint(expr= -m.b169 - m.b170 + m.b171 - m.b191 <= 0)
m.e330 = Constraint(expr= -m.b169 - m.b170 - m.b171 + m.b172 - m.b192 <= 0)
m.e331 = Constraint(expr= m.b173 - m.b193 <= 0)
m.e332 = Constraint(expr= -m.b173 + m.b174 - m.b194 <= 0)
m.e333 = Constraint(expr= -m.b173 - m.b174 + m.b175 - m.b195 <= 0)
m.e334 = Constraint(expr= -m.b173 - m.b174 - m.b175 + m.b176 - m.b196 <= 0)
m.e335 = Constraint(expr= m.b177 - m.b197 <= 0)
m.e336 = Constraint(expr= -m.b177 + m.b178 - m.b198 <= 0)
m.e337 = Constraint(expr= -m.b177 - m.b178 + m.b179 - m.b199 <= 0)
m.e338 = Constraint(expr= -m.b177 - m.b178 - m.b179 + m.b180 - m.b200 <= 0)
m.e339 = Constraint(expr= m.b181 - m.b201 <= 0)
m.e340 = Constraint(expr= -m.b181 + m.b182 - m.b202 <= 0)
m.e341 = Constraint(expr= -m.b181 - m.b182 + m.b183 - m.b203 <= 0)
m.e342 = Constraint(expr= -m.b181 - m.b182 - m.b183 + m.b184 - m.b204 <= 0)
m.e343 = Constraint(expr= m.b185 - m.b205 <= 0)
m.e344 = Constraint(expr= -m.b185 + m.b186 - m.b206 <= 0)
m.e345 = Constraint(expr= -m.b185 - m.b186 + m.b187 - m.b207 <= 0)
m.e346 = Constraint(expr= -m.b185 - m.b186 - m.b187 + m.b188 - m.b208 <= 0)
m.e347 = Constraint(expr= m.b169 + m.b173 == 1)
m.e348 = Constraint(expr= m.b170 + m.b174 == 1)
m.e349 = Constraint(expr= m.b171 + m.b175 == 1)
m.e350 = Constraint(expr= m.b172 + m.b176 == 1)
m.e351 = Constraint(expr= m.b169 + m.b173 - m.b177 >= 0)
m.e352 = Constraint(expr= m.b170 + m.b174 - m.b178 >= 0)
m.e353 = Constraint(expr= m.b171 + m.b175 - m.b179 >= 0)
m.e354 = Constraint(expr= m.b172 + m.b176 - m.b180 >= 0)
m.e355 = Constraint(expr= m.b169 + m.b173 - m.b181 >= 0)
m.e356 = Constraint(expr= m.b170 + m.b174 - m.b182 >= 0)
m.e357 = Constraint(expr= m.b171 + m.b175 - m.b183 >= 0)
m.e358 = Constraint(expr= m.b172 + m.b176 - m.b184 >= 0)
m.e359 = Constraint(expr= m.b169 + m.b173 - m.b185 >= 0)
m.e360 = Constraint(expr= m.b170 + m.b174 - m.b186 >= 0)
m.e361 = Constraint(expr= m.b171 + m.b175 - m.b187 >= 0)
m.e362 = Constraint(expr= m.b172 + m.b176 - m.b188 >= 0)
