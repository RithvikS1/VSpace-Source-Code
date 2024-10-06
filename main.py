from vpython import *

angular_velocity = 1
t = 0
dt = .01

sun = sphere(radius=100, color=color.yellow, emissive=True)
scene.title = "*Planets are to scale relative to each other, not relative to the Sun."

mercury_a = 164.13
mercury_eccentricity = .2056
mercury_b = mercury_a * sqrt(1 - mercury_eccentricity ** 2)
mercury = sphere(radius=5, pos=vec(mercury_a, 0, 0), make_trail=True, color=color.gray(0.5))
mercury_label = label(pos=mercury.pos, text='Mercury', xoffset=20, yoffset=20, space=30, height=15, font='sans')

venus_a = 219.84
venus_eccentricity = .0068
venus_b = venus_a * sqrt(1 - venus_eccentricity ** 2)
venus = sphere(radius=12.5, pos=vec(venus_a, 0, 0), make_trail=True, color=color.orange, emmisive=True)
venus_label = label(pos=venus.pos, text='Venus', xoffset=20, yoffset=20, space=30, height=15, font='sans')

earth_a = 248.16
earth_eccentricity = .0167
earth_b = earth_a * sqrt(1 - earth_eccentricity ** 2)
earth = sphere(radius=12.5, pos=vec(earth_a, 0, 0), make_trail=True, texture=textures.earth)
earth_label = label(pos=earth.pos, text='Earth', xoffset=20, yoffset=20, space=30, height=15, font='sans')

mars_a = 266.11
mars_eccentricity = .0935
mars_b = mars_a * sqrt(1 - mars_eccentricity ** 2)
mars = sphere(radius=6.96, pos=vec(mars_a, 0, 0), make_trail=True, color=color.red)
mars_label = label(pos=mars.pos, text='Mars', xoffset=20, yoffset=20, space=30, height=15, font='sans')

jupiter_a = 961.76
jupiter_eccentricity = .0487
jupiter_b = jupiter_a * sqrt(1 - jupiter_eccentricity ** 2)
jupiter = sphere(radius=140, pos=vec(jupiter_a, 0, 0), make_trail=True, color=color.orange)
jupiter_label = label(pos=jupiter.pos, text='Jupiter', xoffset=20, yoffset=20, space=30, height=15, font='sans')

saturn_a = 1685.84
saturn_eccentricity = .0520
saturn_b = saturn_a * sqrt(1 - saturn_eccentricity ** 2)
saturn = sphere(radius=119.43, pos=vec(saturn_a, 0, 0), make_trail=True, color=color.orange)
saturn_label = label(pos=saturn.pos, text='Saturn', xoffset=20, yoffset=20, space=30, height=15, font='sans')

uranus_a = 3275
uranus_eccentricity = .0469
uranus_b = uranus_a * sqrt(1 - uranus_eccentricity ** 2)
uranus = sphere(radius=52, pos=vec(uranus_a, 0, 0), make_trail=True, color=color.cyan)
uranus_label = label(pos=uranus.pos, text='Uranus', xoffset=20, yoffset=20, space=30, height=15, font='sans')

neptune_a = 5000
neptune_eccentricity = .0097
neptune_b = neptune_a * sqrt(1 - neptune_eccentricity ** 2)
neptune = sphere(radius=50.57, pos=vec(neptune_a, 0, 0), make_trail=True, color=color.blue)
neptune_label = label(pos=neptune.pos, text='Neptune', xoffset=20, yoffset=20, space=30, height=15, font='sans')

donaldjohanson_a = 498.94
donaldjohanson_eccentricity = .187
donaldjohanson_b = donaldjohanson_a * sqrt(1 - donaldjohanson_eccentricity ** 2)
donaldjohanson = sphere(radius=5, pos=vec(donaldjohanson_a, 0, 0), make_trail=False, color=color.gray(0.25))
donaldjohanson_label = label(pos=donaldjohanson.pos, text='Donaldjohanson', xoffset=20, yoffset=20, space=30, height=15, font='sans')

psyche_a = 588.43
psyche_eccentricity = .134
psyche_b = psyche_a * sqrt(1 - psyche_eccentricity ** 2)
psyche = sphere(radius=5, pos=vec(psyche_a, 0, 0), make_trail=False, color=color.gray(0.25))
psyche_label = label(pos=psyche.pos, text='16Psyche', xoffset=20, yoffset=20, space=30, height=15, font='sans')

temple_a = 626.07
temple_eccentricity = .51
temple_b = temple_a * sqrt(1 - temple_eccentricity ** 2)
temple = sphere(radius=5, pos=vec(temple_a, 0, 0), make_trail=False, color=color.gray(0.25))
temple_label = label(pos=temple.pos, text='Temple1', xoffset=20, yoffset=20, space=30, height=15, font='sans')

gaspra_a = 469.67
gaspra_eccentricity = .173
gaspra_b = gaspra_a * sqrt(1 - gaspra_eccentricity ** 2)
gaspra = sphere(radius=5, pos=vec(gaspra_a, 0, 0), make_trail=False, color=color.gray(0.25))
gaspra_label = label(pos=gaspra.pos, text='Gaspra', xoffset=20, yoffset=20, space=30, height=15, font='sans')

apophis_a = 254.73
apophis_eccentricity = .191
apophis_b = apophis_a * sqrt(1 - apophis_eccentricity ** 2)
apophis = sphere(radius=5, pos=vec(apophis_a, 0, 0), make_trail=False, color=color.gray(0.25))
apophis_label = label(pos=apophis.pos, text='⚠️Apophis', xoffset=20, yoffset=20, space=30, height=15, font='sans')

bennu_a = 289
bennu_eccentricity = .204
bennu_b = bennu_a * sqrt(1 - bennu_eccentricity ** 2)
bennu = sphere(radius=5, pos=vec(bennu_a, 0, 0), make_trail=False, color=color.gray(0.25))
bennu_label = label(pos=bennu.pos, text='Bennu', xoffset=20, yoffset=20, space=30, height=15, font='sans')

ryugu_a = 299
ryugu_eccentricity = .191
ryugu_b = ryugu_a * sqrt(1 - ryugu_eccentricity ** 2)
ryugu = sphere(radius=5, pos=vec(ryugu_a, 0, 0), make_trail=False, color=color.gray(0.25))
ryugu_label = label(pos=ryugu.pos, text='Ryugu', xoffset=20, yoffset=20, space=30, height=15, font='sans')

polymele_a = 967.3
polymele_eccentricity = .097
polymele_b = polymele_a * sqrt(1 - polymele_eccentricity ** 2)
polymele = sphere(radius=7, pos=vec(polymele_a, 0, 0), make_trail=False, color=color.gray(0.25))
polymele_label = label(pos=polymele.pos, text='Polymele', xoffset=20, yoffset=20, space=30, height=15, font='sans')

leucus_a = 988
leucus_eccentricity = .066
leucus_b = leucus_a * sqrt(1 - leucus_eccentricity ** 2)
leucus = sphere(radius=7, pos=vec(leucus_a, 0, 0), make_trail=False, color=color.gray(0.25))
leucus_label = label(pos=leucus.pos, text='Leucus', xoffset=20, yoffset=20, space=30, height=15, font='sans')

borrelly_a = 703.84
borrelly_eccentricity = 0.638
borrelly_b = borrelly_a * sqrt(1 - borrelly_eccentricity ** 2)
borrelly = sphere(radius=7, pos=vec(borrelly_a, 0, 0), make_trail=False, color=color.gray(0.25))
borrelly_label = label(pos=borrelly.pos, text='Borrelly', xoffset=20, yoffset=20, space=30, height=15, font='sans')


while True:
    rate(100)
    theta = angular_velocity * t

    #Mercury
    mercury_pos_vec = vector(mercury_a * cos(theta), 0, mercury_b * sin(theta))
    mercury.pos = rotate(mercury_pos_vec, angle=-0.122, axis=vec(0, 0, 1))
    mercury_label.pos = mercury.pos

    # Venus
    venus_pos_vec = vector(venus_a * cos(theta), 0, venus_b * sin(theta))
    venus.pos = rotate(venus_pos_vec, angle=-.0592, axis=vec(0, 0, 1))
    venus_label.pos = venus.pos

    # Earth
    earth.pos = vector(earth_a * cos(theta), 0, earth_b * sin(theta))
    earth_label.pos = earth.pos

    #Mars
    mars_pos_vec = vector(mars_a * cos(theta), 0, mars_b * sin(theta))
    mars.pos = rotate(mars_pos_vec, angle=-.0323, axis=vec(0, 0, 1))
    mars_label.pos = mars.pos

    # Jupiter
    jupiter_pos_vec = vector(jupiter_a * cos(theta), 0, jupiter_b * sin(theta))
    jupiter.pos = rotate(jupiter_pos_vec, angle=-.0227, axis=vec(0, 0, 1))
    jupiter_label.pos = jupiter.pos

    #Saturn
    saturn_pos_vec = vector(saturn_a * cos(theta), 0, saturn_b * sin(theta))
    saturn.pos = rotate(saturn_pos_vec, angle=-.0433, axis=vec(0, 0, 1))
    saturn_label.pos = saturn.pos

    # Uranus
    uranus_pos_vec = vector(uranus_a * cos(theta), 0, uranus_b * sin(theta))
    uranus.pos = rotate(uranus_pos_vec, angle=-.0134, axis=vec(0, 0, 1))
    uranus_label.pos = uranus.pos

    #Neptune
    neptune_pos_vec = vector(neptune_a * cos(theta), 0, neptune_b * sin(theta))
    neptune.pos = rotate(neptune_pos_vec, angle=-.0308, axis=vec(0, 0, 1))
    neptune_label.pos = neptune.pos

    #Donaldjohanson
    donaldjohanson_pos_vec = vector(donaldjohanson_a * cos(theta+.3), 0, donaldjohanson_b * sin(theta+.3))
    donaldjohanson.pos = rotate(donaldjohanson_pos_vec, angle=.0582, axis=vec(0, 0, 1))
    donaldjohanson_label.pos = donaldjohanson.pos

    #Psyche
    psyche_pos_vec = vector(psyche_a * cos(theta+.5), 0, psyche_b * sin(theta+.5))
    psyche.pos = rotate(psyche_pos_vec, angle=-.0772, axis=vec(0, 0, 1))
    psyche_label.pos = psyche.pos

    #Temple1
    temple_pos_vec = vector(temple_a * cos(theta+.1), 0, temple_b * sin(theta+.1))
    temple.pos = rotate(temple_pos_vec, angle=0.1827, axis=vec(0, 0, 1))
    temple_label.pos = temple.pos

    #Gaspra
    gaspra_pos_vec = vector(gaspra_a * cos(theta+.4), 0, gaspra_b * sin(theta+.4))
    gaspra.pos = rotate(gaspra_pos_vec, angle=0.0717, axis=vec(0, 0, 1))
    gaspra_label.pos = gaspra.pos

    #Apophis
    apophis_pos_vec = vector(apophis_a * cos(theta+.6), 0, apophis_b * sin(theta+.6))
    apophis.pos = rotate(apophis_pos_vec, angle=-.0582, axis=vec(0, 0, 1))
    apophis_label.pos = apophis.pos

    #Bennu
    bennu_pos_vec = vector(bennu_a * cos(theta+.7), 0, bennu_b * sin(theta+.7))  # Calculate position vector
    bennu.pos = rotate(bennu_pos_vec, angle=.105, axis=vec(0, 0, 1))  # Rotate position
    bennu_label.pos = bennu.pos

    #Ryugu
    ryugu_pos_vec = vector(ryugu_a * cos(theta+.2), 0, ryugu_b * sin(theta+.2))
    ryugu.pos = rotate(ryugu_pos_vec, angle=-0.1023, axis=vec(0, 0, 1))
    ryugu_label.pos = ryugu.pos

    #Polymele
    polymele_pos_vec = vector(polymele_a * cos(theta+.3), 0, polymele_b * sin(theta+.3))
    polymele.pos = rotate(polymele_pos_vec, angle=0.227, axis=vec(0, 0, 1))
    polymele_label.pos = polymele.pos

    #Leucus
    leucus_pos_vec = vector(leucus_a * cos(theta+.5), 0, leucus_b * sin(theta+.5))
    leucus.pos = rotate(leucus_pos_vec, angle=-0.2007, axis=vec(0, 0, 1))
    leucus_label.pos = leucus.pos

    #Borrelly
    borrelly_pos_vec = vector(borrelly_a * cos(theta + 0.5), 0, borrelly_b * sin(theta + 0.5))
    borrelly.pos = rotate(borrelly_pos_vec, angle=-0.5235, axis=vec(0, 0, 1))
    borrelly_label.pos = borrelly.pos

    t += dt
