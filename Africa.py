from pygal_maps_world.maps import World
from pygal.style import RotateStyle

wm_style = RotateStyle('#336699')
wm = World(style=wm_style, width=1300)
wm.title = 'The Population of different African Countries in 2010'

population = {
    'dz': 35468000, 'eg': 81121000, 'ly': 6355000, 'ma': 31951000, 'sd': 43552000, 'tn': 10549000,'dj': 889000,
    'er': 5254000, 'et': 82950000, 'so': 9331000, 'bi': 8382000,'ke': 40513000, 'mg': 20714000, 'mw': 14901000,
    'mu': 1281000, 'mz': 23390000, 'rw': 10624000, 'sc': 87000, 'tz': 44841000, 'ug': 33424000, 'zm': 12927000,
    'zw': 12571000, 'ao': 19082000, 'cm': 19599000, 'cf': 4401000, 'td': 11227000, 'cd': 65965000, 'cg': 4043000,
    'gq': 700000, 'ga': 1505000, 'st': 165000, 'bw': 2007000, 'ls': 2171000, 'na': 2283000, 'za': 49991000,
    'sz': 1056000, 'bj': 8850000, 'bf': 16468000, 'cv': 496000, 'gm': 1729000, 'gh': 24392000, 'gn': 9982000,
    'gw': 1515000, 'ci': 19738000, 'lr': 3994000, 'ml': 15370000, 'mr': 3460000, 'ne': 15512000, 'ng': 158423000,
    'sn': 12434000, 'sl': 5867000, 'tg': 6028000
}
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for pop in population.values():
    if pop < 10000000:
        cc_pops_1[pop] = pop
    elif pop < 90000000:
        cc_pops_2[pop] = pop
    else:
        cc_pops_3[pop] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm.add('Africa', population)
wm.add('0-10m', cc_pops_1)
wm.add('10-90m', cc_pops_2)
wm.add('>90m', cc_pops_3)

wm.render_to_file('africa.svg')

