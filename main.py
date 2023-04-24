import plotly.graph_objs as go

# Read the room dimensions from the text file
with open('room_dimensions.txt', 'r') as f:
    length = float(f.readline().strip().split(':')[1].strip().split()[0])
    width = float(f.readline().strip().split(':')[1].strip().split()[0])
    height = float(f.readline().strip().split(':')[1].strip().split()[0])

# Create a 3D box representing the room
box = go.Mesh3d(
    x=[0, length, length, 0, 0, length, length, 0],
    y=[0, 0, width, width, 0, 0, width, width],
    z=[0, 0, 0, 0, height, height, height, height],
    color='lightblue'
)

# Define the layout of the plot
layout = go.Layout(
    scene=dict(
        aspectmode='manual',
        aspectratio=dict(x=length, y=width, z=height),
        xaxis=dict(title='Length'),
        yaxis=dict(title='Width'),
        zaxis=dict(title='Height'),
    )
)

# Create a figure and add the box to it
fig = go.Figure(data=[box], layout=layout)

# Show the plot
fig.show()
