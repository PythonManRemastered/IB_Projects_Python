import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Slider, RadioButtons, CheckButtons

phi = (1 + np.sqrt(5)) / 2
a = 1 / phi
b = phi

SOLIDS = {
    "Tetrahedron": (
        [
            (1, 1, 1), (-1, -1, 1),
            (-1, 1, -1), (1, -1, -1)
        ],
        [
            [0, 1, 2], [0, 3, 1],
            [0, 2, 3], [1, 3, 2]
        ]
    ),

    "Cube": (
        [
            (-1, -1, -1), (1, -1, -1),
            (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1),
            (1, 1, 1), (-1, 1, 1)
        ],
        [
            [0, 1, 2, 3], [4, 5, 6, 7],
            [0, 1, 5, 4], [2, 3, 7, 6],
            [1, 2, 6, 5], [3, 0, 4, 7]
        ]
    ),

    "Octahedron": (
        [
            (1, 0, 0), (-1, 0, 0),
            (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1)
        ],
        [
            [0, 2, 4], [2, 1, 4],
            [1, 3, 4], [3, 0, 4],
            [0, 2, 5], [2, 1, 5],
            [1, 3, 5], [3, 0, 5]
        ]
    ),

    "Icosahedron": (
        [
            (-1,  phi,  0), (1,  phi,  0),
            (-1, -phi,  0), (1, -phi,  0),
            (0, -1,  phi), (0,  1,  phi),
            (0, -1, -phi), (0,  1, -phi),
            ( phi,  0, -1), ( phi,  0,  1),
            (-phi,  0, -1), (-phi,  0,  1)
        ],
        [
            [0,11,5],[0,5,1],[0,1,7],[0,7,10],[0,10,11],
            [1,5,9],[5,11,4],[11,10,2],[10,7,6],[7,1,8],
            [3,9,4],[3,4,2],[3,2,6],[3,6,8],[3,8,9],
            [4,9,5],[2,4,11],[6,2,10],[8,6,7],[9,8,1]
        ]
    ),

    "Dodecahedron": (
        [
            (-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),
            (1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1),
            (0,-a,-b),(0,-a,b),(0,a,-b),(0,a,b),
            (-a,-b,0),(-a,b,0),(a,-b,0),(a,b,0),
            (-b,0,-a),(b,0,-a),(-b,0,a),(b,0,a)
        ],
        [
            [0,8,10,2,16],[0,16,18,1,12],[1,18,19,5,9],
            [5,19,7,15,9],[7,15,3,11,13],[3,13,12,1,11],
            [2,10,6,14,16],[6,17,4,14,10],[4,17,19,5,14],
            [2,13,3,6,10],[8,9,15,7,17],[8,12,13,2,10]
        ]
    )
}

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
plt.subplots_adjust(left=0.3, bottom=0.25)

poly = None
labels = []
show_labels = True
current_solid = "Cube"

def draw():
    global poly, labels
    ax.cla()
    labels.clear()

    verts, faces = SOLIDS[current_solid]
    scale = np.array([sx.val, sy.val, sz.val])
    verts = np.array(verts) * scale

    poly3d = [[verts[i] for i in f] for f in faces]
    poly = Poly3DCollection(poly3d, facecolors="lightsteelblue",
                            edgecolors="black", alpha=0.9)
    ax.add_collection3d(poly)

    if show_labels:
        for i, f in enumerate(faces):
            c = verts[f].mean(axis=0)
            labels.append(ax.text(c[0], c[1], c[2], str(i), fontsize=8))

    r = np.ptp(verts, axis=0).max() / 2
    m = verts.mean(axis=0)
    ax.set_xlim(m[0]-r, m[0]+r)
    ax.set_ylim(m[1]-r, m[1]+r)
    ax.set_zlim(m[2]-r, m[2]+r)

    ax.set_title(current_solid)
    ax.set_axis_off()
    fig.canvas.draw_idle()


axcolor = "lightgoldenrodyellow"

sx = Slider(plt.axes([0.3, 0.15, 0.6, 0.03], facecolor=axcolor), "Scale X", 0.3, 2.5, valinit=1)
sy = Slider(plt.axes([0.3, 0.10, 0.6, 0.03], facecolor=axcolor), "Scale Y", 0.3, 2.5, valinit=1)
sz = Slider(plt.axes([0.3, 0.05, 0.6, 0.03], facecolor=axcolor), "Scale Z", 0.3, 2.5, valinit=1)

radio = RadioButtons(plt.axes([0.05, 0.4, 0.2, 0.35]),
                     list(SOLIDS.keys()))

check = CheckButtons(plt.axes([0.05, 0.3, 0.2, 0.08]),
                     ["Show face numbers"], [True])

sx.on_changed(lambda v: draw())
sy.on_changed(lambda v: draw())
sz.on_changed(lambda v: draw())

def change_solid(label):
    global current_solid
    current_solid = label
    draw()

radio.on_clicked(change_solid)

def toggle_labels(label):
    global show_labels
    show_labels = not show_labels
    draw()

check.on_clicked(toggle_labels)

draw()
plt.show()