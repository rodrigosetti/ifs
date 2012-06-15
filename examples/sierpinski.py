
iterations = 20

width = 1280
height = 640

transformations = (
    (1,  lambda x, y, z: (.5*x, .5*y, 0)),
    (1,  lambda x, y, z: (.5*x + .5, .5*y + .5, 0)),
    (1,  lambda x, y, z: (.5*x + 1, .5*y, 0)),
)


