
iterations = 28

width = 300
height = 600

transformations = (
    (1,  lambda x, y, z: (0, .16*y, 0)),
    (7,  lambda x, y, z: (.2*x -.26*y, .23*x + .22*y + 1.6, 0)),
    (7,  lambda x, y, z: (-.15*x + .28*y, .26*x + .24*y + .44, 0)),
    (85, lambda x, y, z: (.85*x + .04*y, -.04*x + .85*y + 1.6, 0))
)

