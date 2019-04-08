import numpy as np
from bokeh.models import Slider
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

n_data_points = 1000
sigma = 0.5
X_left = np.random.normal(loc=(-1, 0), scale=sigma, size=(n_data_points,2))
X_right = np.random.normal(loc=(1, 0), scale=sigma, size=(n_data_points, 2))
X = np.concatenate([X_left, X_right])

def update():
    source.data={
        'x': X[:, 0],
        'y': X[:, 1],
        'alpha': [alpha_slider.value]*X.shape[0],
        'size': [size_slider.value]*X.shape[0]
    }

source = ColumnDataSource({
    'x': np.array([]),
    'y': np.array([]),
    'alpha': np.array([]),
    'size': np.array([])
})
plot = figure()
plot.circle(
    x='x',
    y='y',
    fill_alpha='alpha',
    line_alpha='alpha',
    size='size',
    source=source
)
alpha_slider = Slider(title="Alpha", start=0, end=1, step=0.01, value=0.2)
size_slider = Slider(title="Size", start=0, end=50, step=1, value=10)
alpha_slider.on_change('value', lambda attr, old, new: update())
size_slider.on_change('value', lambda attr, old, new: update())
update()
layout = layout([
    [[alpha_slider, size_slider], plot]
])
document = curdoc()
document.add_root(layout)
